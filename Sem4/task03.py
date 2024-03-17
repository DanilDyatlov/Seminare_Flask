# Задание №3.
# Написать программу, которая считывает список из 10 URL адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте асинхронный подход.
import asyncio
import os
from time import time

from asyncio import gather
from aiohttp import ClientSession

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://ru.wikipedia.org/',
        'https://ru.hexlet.io/',
        'https://megaseller.shop/',
        'https://linux.org',
        'https://metanit.com/',
        ]


async def download(url):
    # async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:  # для macOS
    async with ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()

    os.makedirs(os.path.abspath('parsed/'), exist_ok=True)
    filename = 'parsed/async_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
    print(f"Downloaded {url} in {time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await gather(*tasks)


start_time = time()

if __name__ == '__main__':
    asyncio.run(main())