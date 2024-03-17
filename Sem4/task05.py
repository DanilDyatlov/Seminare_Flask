# Задание №5.
# Создать программу, которая будет производить подсчет количества слов
#   в каждом файле в указанной директории и выводить результаты в консоль.
# Используйте процессы.


import os
from multiprocessing import Process, Value
from time import time

processes = []
PATH = 'parsed/'
count_all_words = Value('i', 0)


def print_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print(f'Finished in {time() - start_time:.2f} seconds')

    return wrapper


def count_words_in_file(word_counter: Value, file_path: str) -> None:
    with (open(file_path, encoding='UTF-8') as file_in):
        with word_counter.get_lock():
            count = len(file_in.read().split())
            print(f'Слов в файле "{file_path}": {count}')
            word_counter.value += count


@print_time
def main(directory: str):
    for f in os.listdir(os.path.abspath(directory)):
        path = os.path.abspath(f'{directory}/{f}')
        process = Process(target=count_words_in_file, args=(count_all_words, path))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main(PATH)
    print(f'Всего слов во всех файлах директории "{os.path.abspath(PATH)}": {count_all_words}')