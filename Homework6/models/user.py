# Таблица пользователей должна содержать следующие поля:
# id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    username: str
    email: str = Field(max_length=128)
    password: str = Field(min_length=6)


class User(BaseModel):
    id: int
    username: str
    email: str = Field(max_length=128)