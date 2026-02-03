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


# 创建了一个协程（coroutine）对象
# print(task(1)) # coroutine

start = time.time()
# (1) 构建事件循环对象
loop = asyncio.get_event_loop()
# (2) 构建协程（coroutine）对象

works = [
    asyncio.ensure_future(work(1)),
    asyncio.ensure_future(work(2)),
]

# print(work(1))
# task01 = asyncio.ensure_future(work(1))
# print(works[0].done())  # 是否完成
# print(works[0].result())


# 给任务1对象绑定一个回调函数
works[0].add_done_callback(task01_callback)

# (3) 收集任务并等待
loop.run_until_complete(asyncio.wait(works))  # 像join

# print(works[0].done())  # 是否完成
# print(works[0].result())

# for work in works:
#     print(work.result())

end = time.time()
print("cost timer:", end - start)
