"""
Домашнее задание:
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""

import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import CSRFProtect

from forms import RegistrationForm, LoginForm
from models import db, User

"""

"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'development_secret_key'
csrf = CSRFProtect(app)
DB_NAME = 'hw3.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

"""
Создаем функции для работы с БД из командной строки
init_db для инициализации 
clear_data для очистки таблицы
"""


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("clear-db")
def clear_data():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Очищена таблица: {table}')
        db.session.execute(table.delete())
    db.session.commit()


"""
Создаем функции для обработки из формы 
Для этого получаем данные из request и проводим их валидацию с помощью метода validate() 
"""


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    # Происходит обработка данных из формы
    if request.method == 'POST' and form.validate():
        email = form.email.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        password = form.password.data

        """
        Проверка на существования пользователя
        Для этого вызывается метод query запроса в бд, которая вызывает метод filter_by
        filter_by используется для простых случаях
        Если пользователь уже существует вызывает флеш сообщение 
        """
        if User.query.filter_by(email=email).first():
            message = f'Пользователь с таким email уже существует.'
            flash(message, 'error')
            return redirect(url_for('registration'))

        # Используем методы по установлению пароля
        user = User(firstname=firstname, lastname=lastname, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        message = f'Пользователь {email} успешно зарегистрирован.'
        flash(message, 'success')

    return render_template('registration.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        # Используем метод для проверки пароля
        if user and user.check_password(password):
            message = f'Добро пожаловать, {email}!'
            flash(message, 'success')
        else:
            message = f'Пользователь с таким email или паролем не найден.'
            flash(message, 'error')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


if __name__ == '__main__':
    # Если БД не существует, необходимо повторно запустить приложение после создания БД
    if DB_NAME not in os.listdir(os.path.abspath('instance/')):
        init_db()
    app.run(debug=True)