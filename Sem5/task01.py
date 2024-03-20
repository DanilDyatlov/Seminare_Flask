# Задание №1.
# Создать API для управления списком задач.
#   Приложение должно иметь возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
from uvicorn import run as uvi_run
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
ID = 0
tasks = []


def _get_id() -> int:
    global ID
    ID += 1
    return ID


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: str


class Task(TaskIn):
    id: int


@app.get('/')
async def index():
    return {'message': 'Главная страница'}


@app.get('/tasks/', response_model=list[Task])
async def root():
    return tasks


@app.post('/tasks/', response_model=list[Task])
async def create_task(query: TaskIn):
    tasks.append(Task(id=_get_id(),
                      title=query.title,
                      description=query.description,
                      status=query.status))
    return tasks


@app.put('/tasks/', response_model=Task)
async def edit_task(id: int, query: TaskIn):
    found = [t for t in tasks if t.id == id]
    task = found[0] if len(found) == 1 else None
    if task:
        task.title = query.title
        task.description = query.description
        task.status = query.status
        return task
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete('/tasks/', response_model=dict)
async def remove_task(id: int):
    found = [t for t in tasks if t.id == id]
    task = found[0] if len(found) == 1 else None
    if task:
        tasks.remove(task)
        return {'message': 'Successful task deletion'}
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    uvi_run('task01:app', host='127.0.0.1', port=8000, reload=True)