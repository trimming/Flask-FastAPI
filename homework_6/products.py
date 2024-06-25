from fastapi import APIRouter, HTTPException
from db import database, products
from models import Product, ProductIn

router = APIRouter()


@router.get('/products/', response_model=list[Product])
async def get_products():
    products_ = products.select()
    return await database.fetch_all(products_)


@router.post('/products/')
async def create_product(product: ProductIn):
    query = products.insert().values(**product.dict())
    await database.execute(query)
    return {'msg': 'Product added'}


@router.get('/products/{id}', response_model=Product)
async def get_product(id: int):
    query = products.select().where(products.c.id == id)
    res = await database.fetch_one(query)
    if res:
        return res
    raise HTTPException(status_code=404, detail='Product not found')


@router.put('/products/{id}', response_model=ProductIn)
async def update_product(id: int, product: ProductIn):
    query = products.update().where(products.c.id == id).values(**product.dict())
    res = await database.execute(query)
    if res:
        return {**product.dict(), 'id': id}
    raise HTTPException(status_code=404, detail='Product not found')


@router.delete('/products/')
async def delete_product(id: int):
    query = products.delete().where(products.c.id == id)
    res = await database.execute(query)
    if res:
        return {'message': 'Product deleted'}
    raise HTTPException(status_code=404, detail='Product not found')