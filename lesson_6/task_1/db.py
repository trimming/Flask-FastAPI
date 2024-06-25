import databases
import sqlalchemy
from fastapi import FastAPI

from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_name', sqlalchemy.String(30)),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('password', sqlalchemy.String)
)    


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)

