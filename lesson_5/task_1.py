import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[bool] = False


tasks = []


@app.get('/task/', response_model=list[Task])
async def get_tasks():
    return [task for task in tasks if not task.status]


@app.get('/task/{id}', response_model=list[Task])
async def get_task(id: int):
    for i in range(len(tasks)):
        if tasks[i].id == id:
            return tasks[i]
    raise HTTPException(status_code=404, detail='Task not found')


@app.post('/task/', response_model=Task)
async def create_task(task: Task):
    if [t for t in tasks if t.id == task.id]:
        raise HTTPException(status_code=409, detail='Task already exist')
    tasks.append(task)
    return task


@app.put('/task/', response_model=Task)
async def update_task(task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task.id:
            tasks[i] = task
            return tasks[i]
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete('/task/{id}')
async def delete_task(id: int):
    for i in range(len(tasks)):
        if tasks[i].id == id:
            tasks.pop(i)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    uvicorn.run('task_1:app', host='localhost', port=8000, reload=True)
