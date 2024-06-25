from fastapi import APIRouter, HTTPException
from db import database, tasks
from models import Task, TaskIn

router = APIRouter()


@router.get('/tasks/', response_model=list[Task])
async def get_tasks():
    tasks_ = tasks.select()
    return await database.fetch_all(tasks_)


@router.post('/tasks/')
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.dict())
    await database.execute(query)
    return {'msg': 'Task added'}


@router.get('/tasks/{id}', response_model=Task)
async def get_task(id: int):
    query = tasks.select().where(tasks.c.id == id)
    res = await database.fetch_one(query)
    if res:
        return res
    raise HTTPException(status_code=404, detail='Task not found')


@router.put('/tasks/{id}', response_model=TaskIn)
async def update_task(id: int, task: TaskIn):
    query = tasks.update().where(tasks.c.id == id).values(**task.dict())
    res = await database.execute(query)
    if res:
        return {**task.dict(), 'id': id}
    raise HTTPException(status_code=404, detail='Task not found')


@router.delete('/tasks/')
async def delete_task(id: int):
    query = tasks.delete().where(tasks.c.id == id)
    res = await database.execute(query)
    if res:
        return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')