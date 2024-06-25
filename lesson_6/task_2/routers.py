from fastapi import APIRouter, HTTPException
from db import database, users
from models import User, UserIn

router = APIRouter()


@router.get('/users/', response_model=list[User])
async def get_users():
    users_ = users.select()
    return await database.fetch_all(users_)


@router.post('/users/')
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    await database.execute(query)
    return {'msg': 'User added'}


@router.get('/users/{id}', response_model=User)
async def get_user(id: int):
    query = users.select().where(users.c.id == id)
    res = await database.fetch_one(query)
    if res:
        return res
    raise HTTPException(status_code=404, detail='User not found')


@router.put('/users/{id}', response_model=UserIn)
async def update_user(id: int, user: UserIn):
    query = users.update().where(users.c.id == id).values(**user.dict())
    res = await database.execute(query)
    if res:
        return {**user.dict(), 'id': id}
    raise HTTPException(status_code=404, detail='User not found')


@router.delete('/users/')
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    res = await database.execute(query)
    if res:
        return {'message': 'User deleted'}
    raise HTTPException(status_code=404, detail='User not found')