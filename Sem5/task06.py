# Задание №6.
# Создать веб-страницу для отображения списка пользователей.
# Приложение должно использовать шаблонизатор Jinja
#   для динамического формирования HTML страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей.
#   Шаблон должен содержать заголовок страницы,
#   таблицу со списком пользователей
#   и кнопку для добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from uvicorn import run as uvi_run
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
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


def _generate_users(qty: int = 10) -> None:
    users.extend([User(id=_get_id(), name=f'User{i}', email=f'user{i}@mail.ru', password=f'User{i}pwd')
                  for i in range(1, qty + 1)])


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'title': 'Главная'})


@app.get('/users/', response_class=HTMLResponse)
async def get_users_list(request: Request):
    if len(users) == 0:
        _generate_users(20)
    return templates.TemplateResponse('users.html',
                                      {'request': request, 'title': 'Список пользователей', 'users': users})


@app.get('/users/create/', response_class=HTMLResponse)
async def create_user(request: Request):
    return templates.TemplateResponse('create_user.html',
                                      {'request': request, 'title': 'Создание пользователя', 'users': users})


if __name__ == '__main__':
    uvi_run('task06:app', host='127.0.0.1', port=8000, reload=True)