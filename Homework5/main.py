"""
Задание
Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""
from enum import Enum
from random import choice

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from uvicorn import run as uvi_run

app = FastAPI()
ID = 0
tasks = []

"""
Фрагменты с семинара
"""
def _get_id() -> int:
    global ID
    ID += 1
    return ID


class Status(str, Enum):
    TODO = 'не выполнена'
    DONE = 'выполнена'


class TaskIn(BaseModel):
    title: str
    description: str
    status: Status


class Task(TaskIn):
    id: int


"""
Метод GET используется для получения ресурсов с сервера.
Метод POST используется для отправки данных на сервер.
Метод PUT используется для обновления данных на сервере.
Метод DELETE используется для удаления данных на сервере. 
"""

"""
Метод по созданию заданий 
"""


def _generate_tasks(qty: int = 10) -> None:
    tasks.extend([Task(id=_get_id(),
                       title=f'Задание:{i}',
                       description=f'Описание: {i}',
                       status=choice(list(Status)))
                  for i in range(1, qty + 1)])


"""
Используя response_model мы определяем тип возвращаемого объекта
HTMLResponse устанавливает для заголовка Content-Type значение text/html
"""


@app.get('/', response_class=HTMLResponse)
async def index():
    return '<h3>Главная страница</h3>'


@app.get('/tasks', response_model=list[Task])
async def get_tasks():
    if len(tasks) == 0:
        _generate_tasks()
    return tasks


@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task


@app.post('/tasks', response_model=Task)
async def create_task(query: TaskIn):
    tasks.append(Task(id=_get_id(),
                      title=query.title,
                      description=query.description,
                      status=query.status))
    return tasks


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, query: TaskIn):
    for task in tasks:
        if task.id == task_id:
            task.title = query.title
            task.description = query.description
            task.status = query.status
            return task
    raise HTTPException(status_code=404, detail='Задача не найдена')


@app.delete('/tasks/{task_id}', response_model=dict)
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {'message': 'Успешное удаление задачи'}
    raise HTTPException(status_code=404, detail='Задача не найдена')


if __name__ == '__main__':
    uvi_run('main:app', host='127.0.0.1', port=8000, reload=True)