import asyncio
import aiohttp
import time
from Homework4.urls import urls

"""
Асинхронный код — это подход к многозадачности, при котором программа может
выполнять несколько задач одновременно без создания отдельных процессов или
потоков. Вместо этого задачи выполняются в рамках одного потока выполнения, но
с использованием механизмов событий и обратных вызовов.
"""


async def download(url):
    """
    Мы создаем функцию download, которая использует aiohttp для получения html-страницы и сохранения ее в файл.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image = await response.read()
            filename = url.replace("https://", "").split("/")[-1]
        with open(f"images/{filename}", "wb") as f:
            f.write(image)
            print(f"Загрузка {url} завершилась за {time.time() - start_time:.2f} секунд")


async def main():
    """
    Мы создаем асинхронную функцию main, которая запускает функцию download для каждого сайта из списка urls и
    ожидает их завершения с помощью метода gather. Мы запускаем функцию main с помощью цикла событий asyncio.
    Функция asyncio.gather(), которая позволяет запускать несколько задач параллельно и ожидать их завершения.
    """
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


start_time = time.time()
if __name__ == "__main__":
    asyncio.run(main())