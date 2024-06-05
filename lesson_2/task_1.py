# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
from pathlib import PurePath, Path

# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('block_button.html')


@app.route('/hello')
def hello():
    return f"Hello, friend!"


@app.route('/upload_img', methods=['GET', 'POST'])
def upload_img():
    if request.method == "POST":
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name} был загружен на сервер'
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
