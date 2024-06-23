# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Request
import logging

from fastapi.params import Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []


@app.get('/users/')
async def get_users(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'users': users})


@app.post('/users/')
async def add_user(
        request: Request,
        id: Annotated[int, Form()],
        name: Annotated[str, Form()],
        email: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    users.append(User(id=id, name=name, email=email, password=password))
    return templates.TemplateResponse('index.html', {'request': request, 'users': users})


if __name__ == '__main__':
    uvicorn.run('task_6:app', host='localhost', port=8000, reload=True)
