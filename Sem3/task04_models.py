# Форма должна содержать следующие поля:
#   ○ Имя пользователя (обязательное поле)
#   ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
#   ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
#   ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# Дополнительно:
#   добавьте проверку на уникальность имени пользователя и электронной почты в базе данных.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"