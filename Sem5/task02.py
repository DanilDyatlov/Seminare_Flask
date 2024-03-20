# Задание №2.
# Создать API для получения списка фильмов по жанру.
# Приложение должно иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
#
from enum import Enum

from uvicorn import run as uvi_run
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
movies = []
ID = 0


def _get_id() -> int:
    global ID
    ID += 1
    return ID


class Genre(str, Enum):
    ACTION = 'боевик'
    COMEDY = 'комедия'
    THRILLER = 'триллер'


class MovieIn(BaseModel, use_enum_values=True):
    title: str
    description: Optional[str]
    genre: Genre


class Movie(MovieIn, use_enum_values=True):
    id: int


@app.get('/', response_class=HTMLResponse)
async def index():
    return '<h1>Главная страница</h1>'


@app.post('/movies/create', response_model=Movie)
async def create_movie(query: MovieIn):
    new_movie = Movie(
        id=_get_id(),
        title=query.title,
        description=query.description,
        genre=str(query.genre))
    movies.append(new_movie)
    return new_movie


@app.get('/movies/', response_model=list[Movie])
async def get_movies():
    return movies


@app.get('/movies/{genre}', response_model=list[Movie])
async def get_movies_by_genre(genre: Genre):
    return [m for m in movies if m.genre == genre]


if __name__ == '__main__':
    uvi_run('task02:app', host='127.0.0.1', port=8000, reload=True)