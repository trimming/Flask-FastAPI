# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
import logging
import math
import secrets
from pathlib import PurePath, Path

# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from flask import Flask, render_template, redirect, url_for, request, abort, flash
from markupsafe import escape
from werkzeug.utils import secure_filename

# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


app = Flask(__name__)
logger = logging.getLogger(__name__)
app.secret_key = secrets.token_hex()



@app.route('/')
def index():
    return render_template('block_button.html')


@app.route('/hello/')
def hello():
    return f"Hello, friend!"


@app.route('/upload_img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == "POST":
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name} был загружен на сервер'
    return render_template('upload.html')


@app.route('/login/', methods=['GET', 'POST'])
def log_in():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        if login == 'login' and password == 'password':
            return f'Welcome, {login}!'
        return f'Error! You need authorisation!'
    return render_template('login.html')


@app.route('/send-text/', methods=['GET', 'POST'])
def send_text():
    if request.method == "POST":
        text = request.form.get('text')
        return f'Количество слов в Вашем тексте: {len(text.split())}.'
    return render_template('send_txt.html')


@app.route('/calc/', methods=['GET', 'POST'])
def calculate():
    if request.method == "POST":
        num_1 = int(request.form.get('num_1'))
        num_2 = int(request.form.get('num_2'))
        operation = request.form.get('operation')
        if operation == 'add':
            return f'Результат: {num_1 + num_2}.'
        elif operation == 'sub':
            return f'Результат: {num_1 - num_2}.'
        elif operation == 'multiply':
            return f'Результат: {num_1 * num_2}.'
        else:
            return f'Результат: {num_1 / num_2}.'
    return render_template('calculate.html')


@app.route('/check-age/', methods=['GET', 'POST'])
def check_age():
    if request.method == "POST":
        age = int(request.form.get('age'))
        name = request.form.get('name')
        if age >= 18:
            return f'Добро пожаловать, {name}!'
        else:
            abort(403)
    return render_template('check-age.html')


@app.errorhandler(403)
def access(e):
    logger.warning(e)
    return render_template('error-age.html'), 403


@app.route('/get-square/', methods=['GET', 'POST'])
def get_square():
    if request.method == "POST":
        num = int(request.form.get('num'))
        return redirect(url_for('result', num=num))
    return render_template('square.html')


@app.route('/result/<int:num>')
def result(num):
    return f'Результат: {num ** 2}'


@app.route('/get-name/', methods=['GET', 'POST'])
def get_name():
    if request.method == "POST":
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('get_name'))
    return render_template('flash.html')

# @app.route('/text/<str:name>')
# def result(name):
#     return f'Результат: {num ** 2}'


if __name__ == '__main__':
    app.run(debug=True)
