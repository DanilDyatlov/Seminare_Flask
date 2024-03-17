# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# В дополнение (Задача №3):
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(35), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(7), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return (f"Student('{self.firstname}', '{self.lastname}', "
                f"{self.age}, '{self.gender}', {self.group}, {self.faculty_id})")


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f"Faculty('{self.faculty}')"


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    students = db.relationship('Student', backref='grades', lazy=True)

    def __repr__(self):
        return f"Grade('{self.subject}', {self.value})"