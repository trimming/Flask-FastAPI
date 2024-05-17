# Задание:
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка»,
# используя базовый шаблон.

from flask import Flask, render_template
from products.py import products

app = Flask(__name__)


@app.route('/main/')
def main():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    clothes = []
    for product in products:
        if product.category == 'clothes':
            clothes.append(product)
    return render_template('clothes.html', clothes=clothes)


@app.route('/shoes/')
def shoes():
    shoes = []
    for product in products:
        if product.category == 'shoes':
            shoes.append(product)
    return render_template('shoes.html', shoes=shoes)


@app.route('/accessories/')
def accessories():
    accessories = []
    for product in products:
        if product.category == 'accessories':
            accessories.append(product)
    return render_template('accessories.html', accessories=accessories)


if __name__ == '__main__':
    app.run(debug=True)
