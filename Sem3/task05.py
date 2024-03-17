# Отправная точка -> Задача №4, остальные задания также выполнены в рамках task05.
# ----- Задание №5. --------------------------------------------------------------
# Создать форму регистрации для пользователя.
# Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением),
# дата рождения, согласие на обработку персональных данных.
# Валидация должна проверять, что все поля заполнены корректно
# (например, дата рождения должна быть в формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.
# ----- Задание №6. --------------------------------------------------------------
# Дополняем прошлую задачу.
# Создайте форму для регистрации пользователей в вашем веб-приложении.
# Форма должна содержать следующие поля: имя пользователя, электронная почта, пароль и подтверждение пароля.
# Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
# После отправки формы, выведите успешное сообщение об успешной регистрации.
# ----- Задание №7. --------------------------------------------------------------
# Создайте форму регистрации пользователей в приложении Flask.
# Форма должна содержать поля: имя, фамилия, email, пароль и подтверждение пароля.
# При отправке формы данные должны валидироваться на следующие условия:
#   ○ Все поля обязательны для заполнения.
#   ○ Поле email должно быть валидным email адресом.
#   ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
#   ○ Поле подтверждения пароля должно совпадать с полем пароля.
#   ○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
#   ○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.
# ----- Задание №8. --------------------------------------------------------------
# Задание ушло в ДЗ.
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
# --------------------------------------------------------------------------------
import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import CSRFProtect

from task05_forms import RegistrationForm, LoginForm
from task05_models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c56cd00d1a08c65029f644cdba4002dc308eee2506f963bb6c7d88281fc2e229'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3task5.db'
db.init_app(app)


# ------------ Функции для работы с БД из командной строки ------------


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


# --------------------------------------------------------------------

@app.route('/')
def index():
    return 'Hi!'


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate():
        username = form.username.data
        birthday = form.birthday.data
        consent = form.consent.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first():
            message = f'Пользователь с таким именем уже существует.'
            flash(message, 'error')
            return redirect(url_for('registration'))
        if User.query.filter_by(email=email).first():
            message = f'Пользователь с таким email адресом уже существует.'
            flash(message, 'error')
            return redirect(url_for('registration'))

        user = User(username=username, birthday=birthday, consent=consent, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        message = f'Пользователь {username} успешно зарегистрирован.'
        flash(message, 'success')

    return render_template('task05_registration.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        if (User.query.filter_by(username=username).first()
                and User.query.filter_by(username=username).first().password == password):
            message = f'Добро пожаловать, {username}!'
            flash(message, 'success')
        else:
            message = f'Пользователь с таким именем или паролем не найден.'
            flash(message, 'error')
            return redirect(url_for('login'))

    return render_template('task05_login.html', form=form)


if __name__ == '__main__':
    # Если БД не существует, необходимо повторно запустить приложение после создания БД
    if 'sem3task5.db' not in os.listdir(os.path.abspath('instance/')):
        init_db()
    app.run(debug=True)