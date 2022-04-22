from flask import request, abort
from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SQLAlchemyAutoSchemaOpts
from marshmallow import fields
from marshmallow import validate
from marshmallow import ValidationError, validates
from marshmallow_sqlalchemy import auto_field
from marshmallow_sqlalchemy.fields import Related

from game_shop_api import models


ma = Marshmallow()


class AutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        dump_only = ('id', 'created_at', 'updated_at')

    def load_from_request(self, **kwargs):
        """Возвращает JSON документ, полученный из объекта запроса."""
        if request.json is None:
            abort(400, 'Invalid input data.')
        return self.load(request.json, **kwargs)

    def populate_obj(self, data, obj):
        """Обновляет объект переданными данными."""
        for attr, value in data.items():
            setattr(obj, attr, value)


class GenreSchema(AutoSchema):
    class Meta(AutoSchema.Meta):
        model = models.Genre

    name = auto_field(validate=validate.Length(min=1, max=30))


class GameSchema(AutoSchema):
    class Meta(AutoSchema.Meta):
        model = models.Game

    title = auto_field(validate=validate.Length(min=1, max=500))
    cost = auto_field(validate=validate.Range(min=0))
    genre_id = auto_field(load_only=True)
    genre = Related('name', dump_only=True)

    @validates('genre_id')
    def validate_genre_id(self, genre_id):
        if not models.Genre.query.get(genre_id):
            raise ValidationError(['Genre does not exists.'])


class UserSchema(AutoSchema):
    class Meta(AutoSchema.Meta):
        model = models.User
        exclude = ('_password', 'balance')
        dump_only = AutoSchema.Meta.dump_only + ('is_active', 'is_admin')

    email = auto_field(field_class=fields.Email)
    password = auto_field(
        '_password',
        validate=validate.Length(min=8),
        load_only=True,
        attribute='password'
    )

    @validates('email')
    def validate_email(self, email):
        user = self.context.get('user')

        if user is None or user.email != email:
            if self.opts.model.get_by_email(email):
                raise ValidationError(
                    ['E-Mail is already in use by another user.']
                )


class BalanceSchema(AutoSchema):
    """Баланс пользователя."""
    balance = fields.Integer(validate=validate.Range(min=1))
