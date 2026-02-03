import queue

# q = queue.Queue(0)
q = queue.Queue(3)

# FIFO：先入先出
# 插入元素：put

q.put(100)
q.put(200)
q.put(300)
# q.put(400)  # 当队列已经满了，默认阻塞
# q.put(400, block=False)
print(q.qsize())
print(q.get())
print(q.get())
print(q.empty())
print(q.qsize())
print(q.get())
print(q.empty())

# print(q.get())  # 当队列empty，默认阻塞
# print(q.get(block=False))  # 当队列empty，报错
