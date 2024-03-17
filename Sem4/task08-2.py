# Задание №8.
# Напишите программу,
#   которая будет скачивать страницы из списка URL-адресов и сохранять их в отдельные файлы на диске.
# В списке может быть несколько сотен URL-адресов.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# Представьте три варианта решения.

# Код из прикрепленных к семинару решений.

from multiprocessing import Process
from time import time

from pywebcopy import save_website

processes = []
start_time = time()
urls = ['https://ya.ru/', 'https://www.google.com/', 'https://megaseller.shop/', ]


def website(url, folder='saved_sites/'):
    name = 'proc_' + url.replace('https://', '').replace('.', '_').replace('/', '')
    save_website(
        url=url,
        project_folder=folder,
        project_name=name,
        bypass_robots=True,
        debug=True,
        delay=None,
    )
    print(f"Downloaded {url} in {time() - start_time:.2f} seconds")


if __name__ == '__main__':
    for url in urls:
        process = Process(target=website, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()