# Задание №3.
# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными
#   нового пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
# Задание №4.
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
#   пользователей и обновлять их в базе данных.
# Задание №5.
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
#   удалять информацию о пользователе из базы данных
#
from pydantic import BaseModel
from uvicorn import run as uvi_run
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
users = []
ID = 0


def _get_id() -> int:
    global ID
    ID += 1
    return ID


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class User(UserIn):
    id: int


@app.get('/', response_class=HTMLResponse)
async def index():
    return '<h1>Главная страница</h1>'


@app.get('/users/', response_model=list[User])
async def get_users():
    return users


@app.post('/users/', response_model=User)
async def create_user(query: UserIn):
    new_user = User(
        id=_get_id(),
        name=query.name,
        email=query.email,
        password=query.password,
    )
    users.append(new_user)
    return new_user


@app.put('/users/', response_model=User)
async def edit_user(id: int, query: UserIn):
    found = [u for u in users if u.id == id]
    user = found[0] if len(found) == 1 else None
    if user:
        user.name = query.name,
        user.email = query.email,
        user.password = query.password,
        return user
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/users/', response_model=dict)
async def remove_user(id: int):
    found = [u for u in users if u.id == id]
    user = found[0] if len(found) == 1 else None
    if user:
        users.remove(user)
        return {'message': 'Successful user deletion'}
    raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvi_run('task03:app', host='127.0.0.1', port=8000, reload=True)