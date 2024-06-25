from typing import List

from fastapi import APIRouter, HTTPException
from datetime import date

from sqlalchemy import select

from db import database, users, orders, products
from models import User, UserIn, Order, OrderIn, Product

router = APIRouter()


@router.get('/orders/', response_model=List[Order])
async def get_orders():
    query = select(orders.c.id, orders.c.order_date, orders.c.status,
                   products.c.id.label('product_id'), products.c.product_name,
                   products.c.description, products.c.price,
                   users.c.id.label('user_id'), users.c.first_name, users.c.last_name,
                   users.c.email, users.c.password).join(products).join(users)
    rows = await database.fetch_all(query)
    return [Order(id=row.id,
                  order_date=row.order_date,
                  status=row.status,
                  user=User(id=row.user_id,
                            first_name=row.first_name,
                            last_name=row.last_name,
                            password=row.password,
                            email=row.email),
                  product=Product(id=row.product_id,
                                  product_name=row.product_name,
                                  description=row.description,
                                  price=row.price)) for row in rows]


@router.get('/orders/{order_id}', response_model=Order)
async def get_order(order_id: int):
    order = await database.fetch_one(orders.select().where(orders.c.id == order_id))
    user = await database.fetch_one(users.select().where(users.c.id == order.user_id))
    user = User(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email,
                password=user.password)
    product = await database.fetch_one(products.select().where(products.c.id == order.product_id))
    product = Product(id=product.id, product_name=product.product_name, description=product.description,
                      price=product.price)
    return Order(product=product, user=user, id=order.id, order_date=order.order_date, status=order.status)


@router.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id, status=order.status,
                                   order_date=date.today())
    last_record_id = await database.execute(query)
    return await get_order(last_record_id)


@router.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(user_id=order.user_id, product_id=order.product_id,
                                                                  status=order.status, order_date=date.today())
    last_record_id = await database.execute(query)
    if last_record_id:
        return await get_order(last_record_id)
    raise HTTPException(status_code=404, detail='Order not found')


@router.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    last_record_id = await database.execute(query)
    if last_record_id:
        return {'message': 'Order deleted'}
    raise HTTPException(status_code=404, detail='Order not found')