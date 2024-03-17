# Форма должна содержать следующие поля:
#   ○ Имя пользователя (обязательное поле)
#   ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
#   ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
#   ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)

from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])