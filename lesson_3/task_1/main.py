from flask import Flask, render_template
from task_1.models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill_tables')
def fill_tables():
    for i in range(5):
        faculty = Faculty(name=f'faculty_{i}')
        db.session.add(faculty)
        for j in range(5):
            student = Student(first_name=f'student{j}_{i}', last_name=f'Student_{i}_{j}', age=18,
                              gender='male', group=4, faculty_id=i+1)
            db.session.add(student)
    db.session.commit()


@app.route('/students/')
def all_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)