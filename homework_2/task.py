# Задание
#
# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти»,
# при нажатии на которую будет удалён cookie-файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.

import secrets
from pathlib import PurePath, Path
from flask import Flask, render_template, redirect, url_for, request, abort, flash, make_response, session
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('home', name=name)))
        response.set_cookie(name, email)
        return response
    return render_template('form.html')


@app.route('/home/<name>', methods=['GET', 'POST'])
def home(name):
    if request.method == 'POST':
        res = make_response(redirect(url_for('index')))
        res.delete_cookie(name)
        return res
    return render_template('home.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
