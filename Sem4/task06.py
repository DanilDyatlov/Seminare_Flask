# Задание №6.
# Создать программу, которая будет производить подсчет количества слов
# в каждом файле в указанной директории и выводить результаты в консоль.
# Используйте асинхронный подход.

import os
import asyncio
from time import time

tasks = []
PATH = 'parsed/'
count_all_words = 0


async def count_words_in_file(file_path: str) -> None:
    global count_all_words
    with (open(file_path, encoding='UTF-8') as file_in):
        count = len(file_in.read().split())
        print(f'Слов в файле "{file_path}": {count}')
        count_all_words += count


async def main(directory: str):
    for f in os.listdir(os.path.abspath(directory)):
        path = os.path.abspath(f'{directory}/{f}')
        tasks.append(asyncio.create_task(count_words_in_file(path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time()
    asyncio.run(main(PATH))
    print(f'Всего слов во всех файлах директории "{os.path.abspath(PATH)}": {count_all_words}')
    print(f'Завершено за {time() - start_time:.2f} сек')