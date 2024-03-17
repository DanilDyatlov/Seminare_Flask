# Задание №1.
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
from random import choice, randint

from flask import Flask, render_template
from task01_models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3task1.db'

db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    faculties = []

    # Создаем факультеты
    # f"Faculty('{self.faculty}')"
    for n in range(1, 8):
        fac = Faculty(title=f'Факультет{n}')
        faculties.append(fac)
        db.session.add(fac)

    # Создаем студентов
    # f"Student('{self.firstname}', '{self.lastname}',
    #            {self.age}, '{self.gender}', {self.group}, {self.faculty_id})"
    for n in range(1, 40):
        gender = choice(['мужской', 'женский'])
        age = randint(16, 21)
        group = randint(1, 7)
        faculty = choice(faculties)
        std = Student(firstname=f'Имя{n}', lastname=f'Фамилия{n}',
                      age=age, gender=gender, group=group, faculty=faculty)
        db.session.add(std)

    # Передаем в БД
    db.session.commit()


# db.drop_all() == "DROP TABLE xx"
# table.delete() == "TRUNCATE TABLE xx"
@app.cli.command("clear-db")
def clear_data():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Очищена таблица: {table}')
        db.session.execute(table.delete())
    db.session.commit()


@app.route('/std_list/')
def std_list():
    students = Student.query.all()
    context = {'students': students}
    return render_template('task01_students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)