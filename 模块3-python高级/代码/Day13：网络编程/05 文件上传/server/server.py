import json
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
        # (1) 接受的文件信息
        data_json_bytes = conn.recv(1024)  # 阻塞函数
        file_params = json.loads(data_json_bytes.decode())
        file_size = file_params.get("file_size")
        file_name = file_params.get("file_name")

        # (2) 循环接受文件大数据

        with open(f"./uploads/{file_name}", "wb") as f:
            receive_data_len = 0
            while receive_data_len < file_size:
                t = conn.recv(1024)
                f.write(t)
                receive_data_len += len(t)

            print("文件上传成功！")
