import requests
import time
import threading
from Homework4.urls import urls
"""
Здесь мы создаем функцию download, которая загружает html-страницу и сохраняет
ее в файл. Затем мы создаем по одному потоку для каждого сайта из списка urls,
передавая функцию download в качестве целевой функции для каждого потока. Мы
запускаем каждый поток и добавляем его в список threads. В конце мы ждем
завершения всех потоков с помощью метода join.

"""


def download(url):
    response = requests.get(url)
    filename = url.replace("https://", "").split("/")[-1]
    with open(f"images/{filename}", "wb") as f:
        f.write(response.content)
    print(f"Загрузка {url} завершилась за {time.time() - start_time:.2f} секунд")


threads = []
start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()