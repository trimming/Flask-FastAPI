import secrets
import hashlib
from flask import Flask, render_template, request
from task.models import db, User
from task.forms import RegisterForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = secrets.token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/login/', methods=['GET', 'POST'])
def log_in():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        pass_hash = hashlib.new('md5')
        password = form.password.data
        pass_hash.update(password.encode())
        user = User(first_name=first_name, last_name=last_name, email=email,
                    password=pass_hash.hexdigest())
        db.session.add(user)
        db.session.commit()
        return f'Вы зарегистрированы!'
    else:
        return render_template('login.html', form=form)

