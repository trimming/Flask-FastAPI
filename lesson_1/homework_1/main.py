# Задание:
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка»,
# используя базовый шаблон.

from flask import Flask, render_template
from products import products
print(products)
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    clothes_list = []
    for product in products:
        if product['category'] == 'clothes':
            clothes_list.append(product)
    return render_template('clothes.html', clothes=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes_list = []
    for product in products:
        if product['category'] == 'shoes':
            shoes_list.append(product)
    return render_template('shoes.html', shoes=shoes_list)


@app.route('/accessories/')
def accessories():
    accessories_list = []
    for product in products:
        if product['category'] == 'accessories':
            accessories_list.append(product)
    return render_template('accessories.html', accessories=accessories_list)


@app.route('/<int:product_id>/')
def cards(product_id):
    card = []
    for product in products:
        if product['id'] == product_id:
            card.append(product)
    return render_template('card.html', cards=card)


if __name__ == '__main__':
    app.run(debug=True)
