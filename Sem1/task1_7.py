from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about/")
def about():
    return "about"


@app.route("/contact/")
def contact():
    return "contact"


@app.route("/<int:num_1>/<int:num_2>")
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route("/word/<string:word>/")
def word_count(word: str) -> str:
    return str(len(word))


@app.route("/context/")
def context():
    return render_template("index.html")


@app.route("/students/")
def students():
    head = {
        "firstname": "Имя",
        "lastname": "Фамилия",
        "age": "Возраст",
        "rating": "Средний балл",
    }

    students_list = [
        {"firstname": "Иван", "lastname": "Иванов", "age": 18, "rating": 4},
        {"firstname": "Петр", "lastname": "Петров", "age": 19, "rating": 3},
        {"firstname": "Семен", "lastname": "Семенов", "age": 20, "rating": 5},
    ]

    return render_template("index.html", **head, students_list=students_list)


@app.route("/news/")
def news():
    news_block = [
        {
            "title": "новость_1",
            "description": "описание_1",
            "create_at": datetime.now().strftime("%H:%M - %m.%d.%Y года"),
        },
        {
            "title": "новость_2",
            "description": "описание_2",
            "create_at": datetime.now().strftime("%H:%M - %m.%d.%Y года"),
        },
        {
            "title": "новость_3",
            "description": "описание_3",
            "create_at": datetime.now().strftime("%H:%M - %m.%d.%Y года"),
        },
    ]

    return render_template("news.html", news_block=news_block)


if __name__ == "__main__":
    app.run(debug=True)