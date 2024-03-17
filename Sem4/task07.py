# Задание №7.
# Напишите программу на Python,
#   которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.
#
# Примечание из семинара: Поделить массив пополам на два среза и запустить подсчет в отдельных потоках.
#
import asyncio
from random import randint
from time import time

from threading import Thread
from multiprocessing import Process
from asyncio import create_task, gather

threads = []
processes = []
tasks = []

start_time = time()
arr = [randint(1, 100) for _ in range(10_000_000)]


def slow_arr_sum_count(a: list) -> None:
    res = 0
    for i in a:
        res += i
    print(f"Сумма = {res}.")


async def async_slow_arr_sum_count(a: list) -> None:
    res = 0
    for i in a:
        res += i
    print(f"Сумма = {res}.")


def synchronized_main():
    slow_arr_sum_count(arr[:int(len(arr) / 2)])
    slow_arr_sum_count(arr[int(len(arr) / 2):])


def multithreading_main(procs: int):
    for _ in range(int(procs / 2)):
        t = Thread(target=slow_arr_sum_count, args=(arr[:int(len(arr) / 2)],), daemon=True)
        threads.append(t)
        t.start()
    for _ in range(int(procs / 2)):
        t = Process(target=slow_arr_sum_count, args=(arr[int(len(arr) / 2):],), daemon=True)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def multiprocessing_main(procs: int):
    for _ in range(int(procs / 2)):
        p = Process(target=slow_arr_sum_count, args=(arr[:int(len(arr) / 2)],), daemon=True)
        processes.append(p)
        p.start()
    for _ in range(int(procs / 2)):
        p = Process(target=slow_arr_sum_count, args=(arr[int(len(arr) / 2):],), daemon=True)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


async def async_main(procs: int):
    for _ in range(int(procs / 2)):
        task = create_task(async_slow_arr_sum_count(arr[:int(len(arr) / 2)],))
        tasks.append(task)
    for _ in range(int(procs / 2)):
        task = create_task(async_slow_arr_sum_count(arr[int(len(arr) / 2):],))
        tasks.append(task)
    await gather(*tasks)


if __name__ == '__main__':
    print(f"{'-' * 20} Synchronized {'-' * 20}")
    start_time = time()
    synchronized_main()
    print(f"Рассчитано за {time() - start_time:.2f} сек.")

    print(f"{'-' * 20} Multithreading {'-' * 20}")
    start_time = time()
    multithreading_main(4)
    print(f"Рассчитано за {time() - start_time:.2f} сек.")

    print(f"{'-' * 20} Multiprocessing {'-' * 20}")
    start_time = time()
    multiprocessing_main(4)
    print(f"Рассчитано за {time() - start_time:.2f} сек.")

    print(f"{'-' * 20} ASynchronized {'-' * 20}")
    start_time = time()
    asyncio.run(async_main(4))
    print(f"Рассчитано за {time() - start_time:.2f} сек.")