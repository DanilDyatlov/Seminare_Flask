# Задание №7.
# Создать RESTful API для управления списком задач.
# Приложение должно использовать FastAPI и поддерживать следующие функции:
#   ○ Получение списка всех задач.
#   ○ Получение информации о задаче по её ID.
#   ○ Добавление новой задачи.
#   ○ Обновление информации о задаче по её ID.
#   ○ Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля:
#   ID (целое число),
#   Название (строка),
#   Описание (строка),
#   Статус (строка): "todo", "in progress", "done".
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте функцию get_tasks для получения списка всех задач (метод GET).
# Создайте функцию get_task для получения информации о задаче по её ID (метод GET).
# Создайте функцию create_task для добавления новой задачи (метод POST).
# Создайте функцию update_task для обновления информации о задаче по её ID (метод PUT).
# Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).
#
from enum import Enum
from random import choice

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from uvicorn import run as uvi_run

app = FastAPI()
ID = 0
tasks = []


def _get_id() -> int:
    global ID
    ID += 1
    return ID


class Status(str, Enum):
    TODO = 'todo'
    PROG = 'in progress'
    DONE = 'done'


class TaskIn(BaseModel, use_enum_values=True):
    title: str
    description: str
    status: Status


class Task(TaskIn, use_enum_values=True):
    id: int


def _generate_tasks(qty: int = 10) -> None:
    tasks.extend([Task(id=_get_id(), title=f'Title_{i}', description=f'desc_{i}', status=choice(list(Status)))
                  for i in range(1, qty + 1)])


@app.get('/', response_class=HTMLResponse)
async def index():
    return '<h3>Главная страница</h3>'


@app.get('/tasks/', response_model=list[Task])
async def get_tasks():
    if len(tasks) == 0:
        _generate_tasks()
    return tasks


@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    found = [t for t in tasks if t.id == task_id]
    if len(found) == 1:
        return found[0]
    raise HTTPException(status_code=404, detail='Task not found')


@app.post('/tasks/', response_model=Task)
async def create_task(query: TaskIn):
    new_task = Task(id=_get_id(), title=query.title, description=query.description, status=query.status)
    tasks.append(new_task)
    return new_task


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, query: TaskIn):
    found = [t for t in tasks if t.id == task_id]
    task = found[0] if len(found) == 1 else None
    if task:
        task.title = query.title
        task.description = query.description
        task.status = query.status
        return task
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete('/tasks/{task_id}', response_model=dict)
async def delete_task(task_id: int):
    found = [t for t in tasks if t.id == task_id]
    if len(found) == 1:
        tasks.remove(found[0])
        return {'message': 'Successful task deletion'}
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    uvi_run('task07:app', host='127.0.0.1', port=8000, reload=True)