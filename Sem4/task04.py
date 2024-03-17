# Задание №4.
# Создать программу, которая будет производить подсчет количества слов в каждом файле
#   в указанной директории и выводить результаты в консоль.
# Используйте потоки.
import os
import threading
from time import time

threads = []
PATH = 'parsed/'
count_all_words = 0


def print_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print(f'Finished in {time() - start_time:.2f} seconds')

    return wrapper


def count_words_in_file(file_path: str) -> None:
    global count_all_words
    with (open(file_path, encoding='UTF-8') as file_in):
        count = len(file_in.read().split())
        print(f'Слов в файле "{file_path}": {count}')
        count_all_words += count


@print_time
def main(directory: str):
    for f in os.listdir(os.path.abspath(directory)):
        path = os.path.abspath(f'{directory}/{f}')
        thread = threading.Thread(target=count_words_in_file, args=(path,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main(PATH)
    print(f'Всего слов во всех файлах директории "{os.path.abspath(PATH)}": {count_all_words}')