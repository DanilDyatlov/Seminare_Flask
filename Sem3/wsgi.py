# from task01 import app
# from task02 import app
# from task03 import app
# from task04 import app
from task05 import app


if __name__ == "__main__":
    app.run(debug=True)


# WSGI (англ. Web Server Gateway Interface)
# — стандарт взаимодействия между Python-программой,
# выполняющейся на стороне сервера, и самим веб-сервером, например Apache.

# Запуск из командной строки:
# 'flask run' или 'flask run --debug'