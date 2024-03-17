# В таблице "Книги" должны быть следующие поля: id, название, год издания,
#   количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(35), nullable=False)
    books = db.relationship('Book', secondary='author_book', backref='authors', lazy=True)

    def __repr__(self):
        return f"Author('{self.firstname}', '{self.lastname}')"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, default=0)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return f"Book('{self.title}', {self.year}, {self.qty}, {self.author_id})"


class AuthorBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))