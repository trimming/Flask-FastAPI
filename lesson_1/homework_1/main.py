# Задание:
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка»,
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        'id': 101,
        'category': 'clothes',
        'name': 'Футболка',
        'description': 'Унисекс, модный принт, свободный покрой',
        'price': '980- P'
    },
    {
        'id': 102,
        'category': 'clothes',
        'name': 'Брюки мужские',
        'description': 'Строгие брюки для свободного стиля. Натуральная шерсть',
        'price': '5880- P'
    },
    {
        'id': 103,
        'category': 'clothes',
        'name': 'Рубашка женская',
        'description': 'Большая цветовая гамма, грудной карман.Хлопок',
        'price': '1580- P'
    },
    {
        'id': 104,
        'category': 'clothes',
        'name': 'Короткие шорты женские',
        'description': 'Низкая талия, удобная молния. Чистый хлопок.',
        'price': '1950- P'
    },
]


@app.route('/main/')
def main():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html', clothes=products)


if __name__ == '__main__':
    app.run(debug=True)
