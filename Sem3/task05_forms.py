# ----- Задание №4. --------------------------------------------------------------
# ----- Задание №5. --------------------------------------------------------------
# ----- Задание №6. --------------------------------------------------------------
# ----- Задание №7. --------------------------------------------------------------
# Общие условия -> насколько я понял авторов, хотя это не указано явно, но следует
# из прикрепленной работы на семинаре, необходимо создать две формы, а именно -
# регистрации и логина:
# 1. Регистрация:
#   ○ Все поля обязательны для заполнения:
#       ○ Псевдоним (уникальный username).
#       ○ Дата рождения (в формате дд.мм.гггг).
#       ○ Согласие на обработку персональных данных.
#       ○ Электронная почта (с валидацией на корректность ввода email).
#       ○ Пароль (с валидацией => не менее 8 символов, включая хотя бы одну букву и одну цифру).
#       ○ Подтверждение пароля (с валидацией на совпадение с паролем).
# 2. Аутентификация:
#   ○ Все поля обязательны для заполнения:
#       ○ Псевдоним (username).
#       ○ Пароль.


from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    # настройки
    pass_len = 8
    regexp = '(?=.*[a-zA-Zа-яА-Я])(?=.*[0-9])'
    password_main_message = (f'Пароль должен содержать не менее {pass_len} символов, '
                             f'включая хотя бы одну букву и одну цифру.')
    password_secondary_message = f'Подтверждение должно совпадать с паролем.'

    # поля
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(max=30)])
    birthday = DateField('День рождения', format='%Y-%m-%d')
    consent = BooleanField('Согласие на обработку персональных данных')
    email = StringField('Адрес электронной почты', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль',
                             validators=[DataRequired(), Length(min=pass_len),
                                         Regexp(regexp, message=password_main_message)])
    confirm_password = PasswordField('Подтверждение пароля',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message=password_secondary_message)])


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])