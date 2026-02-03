import queue
import threading
import time
import random

order_queue = queue.Queue()


# 生成订单消息的函数
def generate_order():
    # 在实际应用中可根据需求生成订单号
    order_id = str(int(time.time()))
    customer_name = random.choice(["John Doe", "Mike", "Tom"])
    # 生成订单总金额
    total_amount = random.choice([100, 99, 123, 78, 56, 199])

    order = {
        'order_id': order_id,
        'customer_name': customer_name,
        'total_amount': total_amount
    }

    return order


def producer():
    while 1:
        # 时间间隔
        inter = random.randint(1, 5)
        print(f"{inter}秒后下一个订单就来了！")
        time.sleep(inter)

        # 生成订单
        order = generate_order()
        # 将订单放入队列
        order_queue.put(order)
        print(f"订单 {order['order_id']} 已生成")


def consumer():
    while 1:
        # 从队列中获取订单
        order = order_queue.get()
        # 处理订单消息（发送短信通知）
        # 在实际应用中可根据需求发送短信通知
        print(f"向顾客 {order['customer_name']} 发送短信通知：您的订单 {order['order_id']} 已支付成功，请耐心等待配送。")
        print(f"订单 {order['order_id']} 已处理")
        print("=" * 80)


p = threading.Thread(target=producer)
p.start()
c = threading.Thread(target=consumer)
c.start()
