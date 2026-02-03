import queue
import threading
import time

q = queue.Queue()


def producer():
    for i in range(1, 11):
        q.put(i)
        time.sleep(3)
        print(f"生产者生产了消息{i}")


def consumer():
    while 1:
        val = q.get()
        time.sleep(6)
        print(f"消费者消费的值：{val}")

        if val == 10:
            break


p = threading.Thread(target=producer)
p.start()
c = threading.Thread(target=consumer)
c.start()
