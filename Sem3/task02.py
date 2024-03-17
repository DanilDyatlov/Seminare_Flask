# Задание №2.
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
#   количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
#   указанием их авторов.
from random import randint
from flask import Flask, render_template
from task02_models import db, Author, Book, AuthorBook

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem3task2.db'

db.init_app(app)


# ------------ Функции для работы с БД из командной строки ------------


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    authors = []
    books = []

    # Создаем авторов
    # f"Author('{self.firstname}', '{self.lastname}')"
    for n in range(1, 101):
        author = Author(firstname=f'Имя{n}', lastname=f'Фамилия{n}')
        authors.append(author)
        db.session.add(author)

    # Создаем книги
    # f"Book('{self.title}', {self.year}, {self.qty}, {self.author_id})"
    for n in range(1, 201):
        book = Book(title=f'Название{n}', year=randint(1400, 2024), qty=randint(0, 100))
        books.append(book)
        db.session.add(book)

    # Создаем связи Авторы <-> Книги
    for n in range(1, 101):
        author_book = AuthorBook(author_id=randint(1, len(authors)), book_id=randint(1, len(books)))
        db.session.add(author_book)

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


@app.route('/books/')
def std_list():
    books = Book.query.all()
    context = {'books': books}
    return render_template('task02_books.html', **context)


if __name__ == '__main__':
    app.run(debug=True)