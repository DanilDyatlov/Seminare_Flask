from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    """
    Основные поля для настройки. Задаем длину пароля и сообщения для вывода
    """
    pass_len = 8
    regexp = '(?=.*[a-zA-Zа-яА-Я])(?=.*[0-9])[A-Za-zа-яА-Я\\d]{8,}'
    password_main_message = (f'Пароль должен содержать не менее {pass_len} символов.'
                             f'Он должен состоять хотя бы из одной буквы и одной цифры')
    password_secondary_message = f'Подтверждение должно совпадать с паролем.'

    """
    Задаем основные поля Имя, Фамилия, Email, Пароль
    Передается валидатор DataRequired()
    Также передаем сообщения для пароля
    """
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    firstname = StringField('Имя', validators=[DataRequired(), Length(max=30)])
    lastname = StringField('Фамилия', validators=[DataRequired(), Length(max=30)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=pass_len),
                                                   Regexp(regexp, message=password_main_message)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(),
                                                                         EqualTo('password',
                                                                                 message=password_secondary_message)])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')