from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Literal


class UserIn(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=30)
    last_name: str = Field(..., min_length=2, max_length=30)
    email: str = EmailStr
    password: str = Field(..., min_length=8, max_length=30)


class User(UserIn):
    id: int


class ProductIn(BaseModel):
    product_name: str = Field(..., min_length=2, max_length=30)
    description: str = Field(..., max_length=250)
    price: float


class Product(ProductIn):
    id: int


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: date
    status: Literal['cancelled', 'done', 'in progress']


class Order(BaseModel):
    id: int
    product: Product
    user: User
    order_date: date
    status: Literal['cancelled', 'done', 'in progress']
