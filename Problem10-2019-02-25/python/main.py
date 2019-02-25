#!/usr/bin/env python3

from asyncio import run, Queue, gather, create_task, sleep
from random import randint


async def job_producer(q, n):
    for iteration in range(100):
        await sleep(0)

        async def f(x):
            print(f"[Producer {n}] X is {x}")
            x**x
        print("push")
        await q.put((f, randint(1, 5)))
    print("done")


async def run_job(f, n, q):
    print(f"sleeping {n}ms")
    await sleep(float(n/100))
    print("run!")
    await f(n)
    q.task_done()


async def job_consumer(np, q):
    while True:
        await sleep(0)

        (f, n) = await q.get()
        print('received')
        t = create_task(run_job(f, n, q))
        await t


async def main():
    q = Queue()
    schedulers = [create_task(job_consumer(3, q))]
    producers = [create_task(job_producer(q, n)) for n in range(3)]

    print("waiting")
    await gather(*producers)
    await q.join()

    for s in schedulers:
        s.cancel()
    print("done")


if __name__ == '__main__':
    run(main())
