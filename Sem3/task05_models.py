#   ○ Все поля обязательны для заполнения:
#       ○ Псевдоним (уникальный username).
#       ○ Дата рождения (в формате дд.мм.гггг).
#       ○ Согласие на обработку персональных данных.
#       ○ Электронная почта (уникальная, с валидацией на корректность ввода email).
#       ○ Пароль

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    consent = db.Column(db.Boolean)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"