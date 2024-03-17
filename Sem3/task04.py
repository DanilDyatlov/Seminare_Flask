# Задание №4.
# Создайте форму регистрации пользователя с использованием Flask-WTF.
# Форма должна содержать следующие поля:
#   ○ Имя пользователя (обязательное поле)
#   ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
#   ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
#   ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)

# После отправки формы данные должны сохраняться в базе данных
#   (можно использовать SQLite) и выводиться сообщение об успешной регистрации.

# Если какое-то из обязательных полей не заполнено или данные не прошли валидацию,
#   то должно выводиться соответствующее сообщение об ошибке.

# Дополнительно:
#   добавьте проверку на уникальность имени пользователя и электронной почты в базе данных.
# Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.


from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import CSRFProtect

from task04_forms import RegistrationForm
from task04_models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c56cd00d1a08c65029f644cdba4002dc308eee2506f963bb6c7d88281fc2e229'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3task4.db'
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
        # Обработка данных из формы
        username = form.username.data
        email = form.email.data
        if User.query.filter_by(username=username).first():
            message = f'Пользователь с таким именем уже существует.'
            flash(message, 'error')
            return redirect(url_for('registration'))
        if User.query.filter_by(email=email).first():
            message = f'Пользователь с таким email адресом уже существует.'
            flash(message, 'error')
            return redirect(url_for('registration'))
        password = form.password.data

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        message = f'Пользователь {username} успешно зарегистрирован.'
        flash(message, 'success')

    return render_template('task04_registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)