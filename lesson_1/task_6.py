# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/info/')
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

    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
