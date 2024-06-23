import uvicorn
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[bool] = False


tasks = []


@app.get('/tasks/', response_model=list[Task])
async def get_tasks():
    return tasks


@app.get('/tasks/{id}', response_model=list[Task])
async def get_task(id: int):
    for i in range(len(tasks)):
        if tasks[i].id == id:
            return tasks[i]
    raise HTTPException(status_code=404, detail='Task not found')


@app.post('/tasks/', response_model=Task)
async def create_task(task: Task):
    if [t for t in tasks if t.id == task.id]:
        raise HTTPException(status_code=409, detail='Task already exist')
    tasks.append(task)
    return task


@app.put('/tasks/')
async def update_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i].status = True
            return tasks[i]
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete('/tasks/{id}')
async def delete_task(id: int):
    for i in range(len(tasks)):
        if tasks[i].id == id:
            tasks.pop(i)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    uvicorn.run('task:app', host='localhost', port=8000, reload=True)
