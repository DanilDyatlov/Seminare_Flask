# Код из прикрепленных к семинару решений.

from random import randint
from threading import Thread
from time import time

print(f"{'-' * 20} Multithreading {'-' * 20}")

start_time = time()
threads = []

arr = [randint(1, 100) for _ in range(5_000_000)]


def arr_sum(arg):
    res = sum(arg)
    print(f"{res} calculated in {time() - start_time:.2f} seconds")


for i in range(5):
    t = Thread(target=arr_sum, args=[arr], daemon=True)
    threads.append(t)
    t.start()

if __name__ == '__main__':
    for t in threads:
        t.join()

# -------------------- Multithreading --------------------
# 252445686 calculated in 2.16 seconds
# 252445686 calculated in 2.18 seconds
# 252445686 calculated in 2.20 seconds
# 252445686 calculated in 2.22 seconds
# 252445686 calculated in 2.24 seconds