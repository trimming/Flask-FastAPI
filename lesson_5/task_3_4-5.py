import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [User(id=1, name='test', email='test@example.com', password='GSBssdgsddgsg')]


@app.get('/users/', response_model=list[User])
async def get_users():
    return users


@app.get('/users/{id}', response_model=list[User])
async def get_user(id: int):
    for i in range(len(users)):
        if users[i].id == id:
            return users[i]
    raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/', response_model=User)
async def create_task(user: User):
    if [t for t in users if t.id == user.id]:
        raise HTTPException(status_code=409, detail='User already exist')
    users.append(user)
    return user


@app.put('/user/', response_model=User)
async def update_user(user: User):
    for i in range(len(users)):
        if users[i].id == user.id:
            users[i] = user
            return users[i]
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{id}')
async def delete_user(id: int):
    for i in range(len(users)):
        if users[i].id == id:
            users.pop(i)
            return {'message': 'User deleted'}
    raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run('task_3_4_5:app', host='localhost', port=8000, reload=True)
