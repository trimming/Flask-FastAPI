# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/news/')
def news():
    news = [
        {
            'title': 'Главное событие дня!',
            'description': 'Все что происходит должно было случится, этого никто не смог предположить...',
            'date': '10.05.2024'
        },
        {
            'title': 'Главное событие дня!',
            'description': 'Все что происходит должно было случится, этого никто не смог предположить...',
            'date': '10.05.2024'
        },
        {
            'title': 'Главное событие дня!',
            'description': 'Все что происходит должно было случится, этого никто не смог предположить...',
            'date': '10.05.2024'
        },
        {
            'title': 'Главное событие дня!',
            'description': 'Все что происходит должно было случится, этого никто не смог предположить...',
            'date': '10.05.2024'
        },
    ]
    return render_template('news2.html', news=news)


@app.route('/students/')
def students_info():
    students = [
        {
            'name': 'Alexey',
            'last_name': 'Golikov',
            'age': '42',
            'range': '4.0'
        },
        {
            'name': 'Sergio',
            'last_name': 'Ramos',
            'age': '28',
            'range': '7.2'
        },
        {
            'name': 'James',
            'last_name': 'Milner',
            'age': '38',
            'range': '6.5'
        },
    ]

    return render_template('std.html', students=students)



@app.route('/base/')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)