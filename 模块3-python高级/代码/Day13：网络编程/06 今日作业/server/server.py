import json
import socket
import struct
import time

from loguru import logger
import os


def get(conn, params):
    # (1) 将文件信息上传给服务器

    file_name = params.get("file_name")
    local_path = f"./uploads/{file_name}"
    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)
    params = {"file_name": file_name, "file_size": file_size}
    data = json.dumps(params).encode()
    conn.send(struct.pack("i", len(data)))
    conn.send(data)

    # (2)  将文件数据包上传给服务器

    with open(local_path, "rb") as f:
        for line in f:
            conn.send(line)

    print("文件下载成功！")


def put(conn, params):
    file_size = params.get("file_size")
    file_name = params.get("file_name")

    # (2) 循环接受文件大数据

    with open(f"./uploads/{file_name}", "wb") as f:
        receive_data_len = 0
        while receive_data_len < file_size:
            t = conn.recv(1024)
            f.write(t)
            receive_data_len += len(t)

        print("文件上传成功！")


def main():
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
            # time.sleep(10)
            # (1) 接受的文件信息
            file_params_head = conn.recv(4)  # 阻塞函数
            data_json_bytes_len = struct.unpack("i", file_params_head)[0]

            data_json_bytes = conn.recv(data_json_bytes_len)  # 阻塞函数
            params = json.loads(data_json_bytes.decode())

            cmd = params.get("cmd")
            if cmd == "put":
                put(conn, params)
            elif cmd == "get":
                get(conn, params)
            else:
                print("错误命令")
                break


if __name__ == '__main__':
    main()
