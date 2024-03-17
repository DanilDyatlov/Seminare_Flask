# Код из прикрепленных к семинару решений.

from asyncio import ensure_future, gather, run
from random import randint
from time import time

start_time = time()
tasks = []

arr = [randint(1, 100) for _ in range(5_000_000)]


async def arr_sum(arg):
    res = sum(arg)
    print(f"{res} calculated in {time() - start_time:.2f} seconds")


async def main():
    for i in range(5):
        task = ensure_future(arr_sum(arr))
        tasks.append(task)
    await gather(*tasks)


if __name__ == '__main__':
    print(f"{'-' * 20} ASynchronized {'-' * 20}")
    run(main())

# -------------------- ASynchronized --------------------
# 252637572 calculated in 2.15 seconds
# 252637572 calculated in 2.18 seconds
# 252637572 calculated in 2.20 seconds
# 252637572 calculated in 2.22 seconds
# 252637572 calculated in 2.24 seconds