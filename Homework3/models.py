from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

"""
Заполняем таблицу
Создаем функции для установление и проверки пароля
"""


class User(db.Model):
    def __init__(self, email: str, firstname: str, lastname: str):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)