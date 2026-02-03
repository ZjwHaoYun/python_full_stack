import time
import multiprocessing


def foo():
    print("foo start...")
    time.sleep(5)
    print("foo end...")


def bar():
    print("bar start...")
    time.sleep(3)
    print("bar end...")


if __name__ == '__main__':
    start = time.time()
    # 创建子进程对象
    p1 = multiprocessing.Process(target=foo, args=())
    p1.start()
    p2 = multiprocessing.Process(target=bar, args=())
    p2.start()

    p1.join()
    p2.join()
    print("finished!")

    end = time.time()

    print("cost timer:", end - start)
