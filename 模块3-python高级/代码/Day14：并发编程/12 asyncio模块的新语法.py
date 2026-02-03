import asyncio
import time


def task01_callback(obj):
    print("obj:", obj)
    print("hello task01 finished")
    print(obj.done(), obj.result())


async def work(i):
    print(f"task {i} start")
    await asyncio.sleep(i)  # 模拟IO事件
    print(f"task {i} end")

    return i ** 2


async def main():
    start = time.time()

    works = [
        asyncio.create_task(work(1)),
        asyncio.create_task(work(2)),
        asyncio.create_task(work(3)),
    ]

    # 给任务1对象绑定一个回调函数
    works[0].add_done_callback(task01_callback)
    # (3) 收集任务并等待
    ret = await  asyncio.gather(*works)  # 像join

    print("ret:", ret)

    end = time.time()
    print("cost timer:", end - start)


asyncio.run(main())
