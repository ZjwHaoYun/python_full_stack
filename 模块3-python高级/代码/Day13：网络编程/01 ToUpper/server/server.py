import socket
from loguru import logger

# (1) 构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 服务端三件套：bind listen accept
sock.bind(("127.0.0.1", 8899))
sock.listen(5)
logger.info("服务器启动")
while 1:
    logger.info("等待新连接...")
    conn, addr = sock.accept()  # 阻塞函数
    # print(f"conn：{conn}，addr：{addr}")
    logger.info(f"来自于客户端{addr}的请求成功")

    while 1:
        # (3) 收消息
        data_bytes = conn.recv(1024)  # 阻塞函数
        print("data:", data_bytes.decode())

        if data_bytes == "quit".encode() or len(data_bytes) == 0:
            logger.info(f"来自于{addr}客户端退出！")
            break

        # (4) 处理数据并发送
        data = data_bytes.decode()
        res = data.upper()
        conn.send(res.encode())
