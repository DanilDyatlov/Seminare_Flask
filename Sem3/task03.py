# Задание №3.
# Доработаем задачу про студентов.
# --------------------------------------------------------------------------
# Отправная точка -> код Задачи №1.
# --------------------------------------------------------------------------
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.


from random import choice, randint

from flask import Flask, render_template
from task03_models import db, Student, Faculty, Grade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3task3.db'

db.init_app(app)


# ------------ Функции для работы с БД из командной строки ------------


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    faculties, students, subjects = [], [], []
    # Создаем факультеты
    for n in range(1, 8):
        fac = Faculty(title=f'Факультет{n}')
        faculties.append(fac)
        db.session.add(fac)
    # Создаем студентов
    for n in range(1, 40):
        gender = choice(['мужской', 'женский'])
        age = randint(16, 21)
        group = randint(1, 7)
        faculty = choice(faculties)
        std = Student(firstname=f'Имя{n}', lastname=f'Фамилия{n}',
                      age=age, gender=gender, group=group, faculty=faculty)
        students.append(std)
        db.session.add(std)
    # Создаем предметы и оценки к ним
    for n in range(1, 15):
        subjects.append(f'Предмет{n}')
    for n in range(1, 100):
        subject = choice(subjects)
        value = randint(3, 5)
        student_id = choice(range(1, len(students)))
        grade = Grade(subject=subject, value=value, student_id=student_id)
        db.session.add(grade)
    # Передаем в БД
    db.session.commit()


@app.cli.command("clear-db")
def clear_data():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Очищена таблица: {table}')
        db.session.execute(table.delete())
    db.session.commit()


# --------------------------------------------------------------------

@app.route('/')
def index():
    return 'Hi!'


@app.route('/std_list/')
def std_list():
    students = Student.query.all()
    context = {'students': students}
    return render_template('task01_students.html', **context)


@app.route('/std_grades_list/')
def std_grades_list():
    students = Student.query.all()
    grades = Grade.query.all()
    context = {'students': students, 'grades': grades}
    return render_template('task03_student_grades.html', **context)


if __name__ == '__main__':
    app.run(debug=True)