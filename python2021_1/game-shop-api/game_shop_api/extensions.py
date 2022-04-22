import base64
from functools import wraps

from flask import current_app, abort
from flask_login import LoginManager, current_user

from game_shop_api.models import User


login_manager = LoginManager()


@login_manager.request_loader
def load_user(request):
    """Аутентифицирует пользователя по заголовку Authorization и возвращает экземпляр."""
    auth = request.headers.get('Authorization')

    if auth:
        _, auth = auth.rsplit(' ', 1)

        try:
            email, password = base64.b64decode(auth).decode().split(':')
        except (TypeError, ValueError):
            return None

        user = User.get_by_email(email)

        if user and user.check_password(password):
            return user

    return None


def admin_required(func):
    """Входная точка требует от пользователя быть администратором."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()

        if not current_user.is_admin:
            abort(403)

        return func(*args, **kwargs)
    return wrapper
