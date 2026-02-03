import asyncio
import time


async def execute_query(query):
    # 模拟数据库查询，这里可以替换为实际的数据库查询操作
    # 这里使用time.sleep来模拟查询的阻塞操作
    import time
    await asyncio.sleep(1)
    return f"Result for query: {query}"


async def main():
    queries = [
        "SELECT * FROM table1",
        "SELECT * FROM table2",
        "SELECT * FROM table3"
    ]

    tasks = []

    for query in queries:
        task = asyncio.create_task(execute_query(query))
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    print(results)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("cost timer:", end - start)
