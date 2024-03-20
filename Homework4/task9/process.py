import requests
from multiprocessing import Process
import time
from Homework4.urls import urls
from treads import download
"""
Мы используем модуль multiprocessing для создания процессов вместо потоков.
"""

processes = []
start_time = time.time()
if __name__ == "__main__":
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()