import databases
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(30)),
    Column('last_name', String(30)),
    Column('email', String(50)),
    Column('password', String)
)

products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('product_name', String(30)),
    Column('description', String(250)),
    Column('price', Integer)
)

orders = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('order_date', Date()),
    Column('status', String),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('product_id', Integer, ForeignKey('products.id'), nullable=False),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)
