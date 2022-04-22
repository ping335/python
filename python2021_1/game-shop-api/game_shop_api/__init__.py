from flask import Flask
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from game_shop_api.extensions import login_manager
from game_shop_api.models import db, bcrypt
from game_shop_api.schemas import ma
from game_shop_api import views


def create_app(config_file=None):
    # 1. Создать экземпляр приложения
    app = Flask(__name__, instance_relative_config=True)

    # 2. Прочитать конфигурационные параметры
    app.config.from_pyfile('config.py', silent=True)

    if config_file is not None:
        app.config.from_pyfile(config_file, silent=True)
    else:
        app.config.from_envvar('FLASK_CONFIG', silent=True)

    # 3. Инициализация расширений
    db.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)

    # 4. Регистрация Blueprint-ов
    app.register_blueprint(views.bp)

    # Создает все таблицы в БД (по хорошему это делается консольной командой)
    db.create_all(app=app)

    @app.errorhandler(HTTPException)
    def http_exception_handler(err):
        return {'message': err.description}, err.code

    @app.errorhandler(ValidationError)
    def validation_error_handler(err):
        return {'message': err.messages}, 422

    return app
