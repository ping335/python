from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()
bcrypt = Bcrypt()


class TimestampMixin:
    """Примесь добавляет атрибуты с временем создания и последнего редактирования сущности."""
    created_at = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, nullable=False
    )
    updated_at = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


user_games = db.Table('user_games', db.Model.metadata,
    db.Column('user_id', db.ForeignKey('user.id'), primary_key=True),
    db.Column('game_id', db.ForeignKey('game.id'), primary_key=True)
)


class Genre(db.Model, TimestampMixin):
    """Жанр игры"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, comment='Название жанра игры')


class Game(db.Model, TimestampMixin):
    """Игра"""
    id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.ForeignKey('genre.id'), nullable=False)
    genre = relationship('Genre', backref='games')
    title = db.Column(db.String(500), nullable=False, comment='Название игры')
    cost = db.Column(db.Float, nullable=False, comment='Стоимость игры')
    description = db.Column(db.Text, default='', nullable=False, comment='Описание игры')


class User(db.Model, TimestampMixin, UserMixin):
    """Пользователь"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False, comment='Используется как логин')
    _password = db.Column(db.String(100), name='password', nullable=False, comment='Хешированный пароль')
    is_active = db.Column(db.Boolean, default=True, nullable=False, comment='Аккаунт не заблокирован')
    is_admin = db.Column(db.Boolean, default=False, nullable=False, comment='Аккаунт администратора')
    display_name = db.Column(db.String(255), default='', nullable=False, comment='Отображаемое имя вместо E-Mail')
    balance = db.Column(db.Float, default=0, nullable=False, comment='Баланс кошелька')
    games = relationship('Game', secondary=user_games, backref='users', lazy='dynamic')

    def change_password(self, password):
        """Изменяет пароль для текущего пользователя."""
        self._password = bcrypt.generate_password_hash(password).decode()

    # user.password = '123'
    password = property(fset=change_password)

    def check_password(self, password):
        """Возвращает истину, если пароль верный, иначе ложь."""
        return bcrypt.check_password_hash(self._password, password)

    def get_id(self):
        """Возвращает идентификатор пользователя, требует UserMixin."""
        return self.id

    def buy_game(self, game):
        """Осуществляет покупку указанной игры."""
        if self.balance < game.cost:
            raise RuntimeError('Not enough money to buy.')

        self.games.append(game)
        self.balance -= game.cost

    def is_purchased(self, game):
        """
        Возвращает истину, если игра уже куплена.

        user_games.c - атрибут таблиц SQLAlchemy, которые не определены как модели.
        Для этих таблиц колонки отображаются как субатрибуты атрибута "c".
        """
        q = self.games.filter(user_games.c.game_id == game.id)
        return db.session.query(q.exists()).scalar()

    @classmethod
    def get_by_email(cls, email):
        """Возвращает пользователя с указанным E-Mail, либо None."""
        return cls.query.filter_by(email=email).first()
