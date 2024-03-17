# Задание №8.
# Напишите программу,
#   которая будет скачивать страницы из списка URL-адресов и сохранять их в отдельные файлы на диске.
# В списке может быть несколько сотен URL-адресов.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# Представьте три варианта решения.

# Код из прикрепленных к семинару решений.

from threading import Thread
from time import time

from pywebcopy import save_website

threads = []
start_time = time()
urls = ['https://ya.ru/', 'https://www.google.com/', 'https://megaseller.shop/', ]


def website(url, folder='saved_sites/'):
    name = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '')
    save_website(
        url=url,
        project_folder=folder,
        project_name=name,
        bypass_robots=True,
        debug=True,
        delay=None,
    )
    print(f"Downloaded {url} in {time() - start_time:.2f} seconds")


for url in urls:
    thread = Thread(target=website, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()