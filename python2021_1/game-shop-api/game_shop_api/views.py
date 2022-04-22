from flask import Blueprint, jsonify, abort
from flask.views import MethodView
from flask_login import login_required, current_user

from game_shop_api.extensions import admin_required
from game_shop_api.models import db, Genre, Game, User
from game_shop_api.schemas import GenreSchema, GameSchema, UserSchema, BalanceSchema


bp = Blueprint('api', __name__)


class GenreCollection(MethodView):
    def get(self):
        return jsonify(
            GenreSchema(many=True).dump(Genre.query.all())
        )

    @admin_required
    def post(self):
        schema = GenreSchema()
        data = schema.load_from_request()

        genre = Genre(**data)
        db.session.add(genre)
        db.session.commit()

        return schema.dump(genre), 201


class GenreItem(MethodView):
    def get(self, genre_id):
        return GenreSchema().dump(
            Genre.query.get_or_404(genre_id)
        )

    @admin_required
    def put(self, genre_id):
        genre = Genre.query.get_or_404(genre_id)
        schema = GenreSchema()
        data = schema.load_from_request()
        schema.populate_obj(data, genre)
        db.session.commit()
        return schema.dump(genre)

    @admin_required
    def delete(self, genre_id):
        genre = Genre.query.get_or_404(genre_id)
        db.session.delete(genre)
        db.session.commit()
        return '', 204


class GamesCollection(MethodView):
    def get(self):
        return jsonify(
            GameSchema(many=True).dump(Game.query.all())
        )

    @admin_required
    def post(self):
        schema = GameSchema()
        data = schema.load_from_request()

        game = Game(**data)
        db.session.add(game)
        db.session.commit()

        return schema.dump(game), 201


class GamesItem(MethodView):
    def get(self, game_id):
        return GameSchema().dump(
            Game.query.get_or_404(game_id)
        )

    @admin_required
    def put(self, game_id):
        game = Game.query.get_or_404(game_id)
        schema = GameSchema()
        data = schema.load_from_request()
        schema.populate_obj(data, game)
        db.session.commit()
        return schema.dump(game)

    @admin_required
    def delete(self, game_id):
        game = Game.query.get_or_404(game_id)
        db.session.delete(game)
        db.session.commit()
        return '', 204


class UsersCollection(MethodView):
    def post(self):
        schema = UserSchema()
        data = schema.load_from_request()

        user = User(**data)
        db.session.add(user)
        db.session.commit()

        return schema.dump(user), 201


class UserGames(MethodView):
    """Игры, которые приобрел пользователь."""

    decorators = [login_required]

    def get(self):
        return jsonify(GameSchema(many=True).dump(current_user.games))


class Purchase(MethodView):
    """Пользователь совершает покупку игры."""

    decorators = [login_required]

    def put(self, game_id):
        """
        PUT может быть использован для создания ресурса, в случае,
        когда идентификатор ресурса выбирает клиент а не сервер.

        Или, если перефразировать - при отправке PUT запроса по адресу,
        содержащему не существующий идентификатор ресурса.
        Опять же, стоит помнить,
        что тело запроса должно быть модификацией оригинального ресурса.
        Многие считают это запутанным и не понятным.
        Соответственно, данную возможность метода PUT стоит использовать с осторожностью.
        Да и при крайней необходимости.
        """
        game = Game.query.get_or_404(game_id)

        if current_user.is_purchased(game):
            abort(409, 'You have already purchased this game.')

        try:
            current_user.buy_game(game)
            db.session.commit()
        except RuntimeError as err:
            abort(412, err)

        return '', 201


class Balance(MethodView):
    """Пополнение баланса пользователем."""

    decorators = [login_required]

    def get(self):
        return BalanceSchema().dump({'balance': current_user.balance})

    def post(self):
        schema = BalanceSchema()
        data = schema.load_from_request()
        current_user.balance += data['balance']
        db.session.commit()
        return schema.dump({'balance': current_user.balance})


class Profile(MethodView):
    """Профиль пользователя."""

    decorators = [login_required]

    def get(self):
        return UserSchema().dump(current_user)

    def put(self):
        schema = UserSchema()
        schema.context['user'] = current_user
        data = schema.load_from_request()
        schema.populate_obj(data, current_user)
        db.session.commit()
        return schema.dump(current_user)


genres_api = GenreCollection.as_view('genres_api')
genres_item_api = GenreItem.as_view('genres_item_api')
games_api = GamesCollection.as_view('games_api')
games_item_api = GamesItem.as_view('games_item_api')
users_api = UsersCollection.as_view('users_api')
users_games = UserGames.as_view('user_games')
purchase_api = Purchase.as_view('purchase_api')
balance_api = Balance.as_view('balance_api')
profile_api = Profile.as_view('profile_api')

bp.add_url_rule('/genres/', view_func=genres_api)
bp.add_url_rule('/genres/<int:genre_id>', view_func=genres_item_api)
bp.add_url_rule('/games/', view_func=games_api)
bp.add_url_rule('/games/<int:game_id>', view_func=games_item_api)
bp.add_url_rule('/users/', view_func=users_api)
bp.add_url_rule('/user', view_func=profile_api)
bp.add_url_rule('/user/games/', view_func=users_games)
bp.add_url_rule('/user/games/<int:game_id>', view_func=purchase_api)
bp.add_url_rule('/user/balance', view_func=balance_api)
