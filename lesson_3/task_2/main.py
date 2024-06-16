from flask import Flask, render_template
from task_2.models import db, Author, Book, BookAuthor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/books/')
def all_students():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)