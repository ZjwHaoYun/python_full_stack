import socket
from loguru import logger
import struct
import subprocess

# (1) 构建服务端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 服务端三件套：bind listen accept
sock.bind(("127.0.0.1", 9999))
sock.listen(5)
logger.info("服务器启动")
while 1:
    logger.info("等待新连接...")
    conn, addr = sock.accept()  # 阻塞函数
    # print(f"conn：{conn}，addr：{addr}")
    logger.info(f"来自于客户端{addr}的请求成功")

    while 1:
        # (3) 收消息
        cmd_bytes = conn.recv(1024)  # 阻塞函数
        print("cmd:", cmd_bytes.decode())

        if cmd_bytes == "quit".encode() or len(cmd_bytes) == 0:
            logger.info(f"来自于{addr}客户端退出！")
            break

        # (4) 处理数据并发送
        cmd_ret = subprocess.getoutput(cmd_bytes)
        if not cmd_ret:
            cmd_ret = "执行完毕！"

        print("cmd_ret的长度", len(cmd_ret.encode()))

        # 发送数据的长度
        cmd_ret_length = len(cmd_ret.encode())

        cmd_ret_length_bytes = struct.pack("i", cmd_ret_length)
        conn.send(cmd_ret_length_bytes)

        # 发送数据
        conn.send(cmd_ret.encode())
