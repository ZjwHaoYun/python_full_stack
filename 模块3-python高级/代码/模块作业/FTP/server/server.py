import json
import socket
import struct
import threading
import time
from loguru import logger
import os
from hashlib import md5


class FTPServer(object):

    def __init__(self):
        # (1) 构建服务端套接字对象
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        # (2) 服务端三件套：bind listen accept
        self.sock.bind(("127.0.0.1", 8888))
        self.sock.listen(5)

    def run(self):
        logger.info("服务器启动")
        while 1:
            logger.info("等待新连接...")
            conn, addr = self.sock.accept()  # 阻塞函数
            # print(f"conn：{conn}，addr：{addr}")
            logger.info(f"来自于客户端{addr}的请求成功")

            t = threading.Thread(target=self.conn_handler, args=(conn,))
            t.start()

    def conn_handler(self, conn):
        while 1:
            # time.sleep(10)
            # (1) 接受的文件信息
            file_params_head = conn.recv(4)  # 阻塞函数
            if not file_params_head: break
            data_json_bytes_len = struct.unpack("i", file_params_head)[0]

            data_json_bytes = conn.recv(data_json_bytes_len)  # 阻塞函数
            params = json.loads(data_json_bytes.decode())

            cmd = params.get("cmd")

            if hasattr(self, cmd):
                cmd_func = getattr(self, cmd)
                cmd_func(conn, params)

    def put(self, conn, params):
        file_size = params.get("file_size")
        file_name = params.get("file_name")

        # (2) 循环接受文件大数据
        md5_obj = md5()
        with open(f"./uploads/{file_name}", "wb") as f:
            receive_data_len = 0
            while receive_data_len < file_size:
                t = conn.recv(1024)
                f.write(t)
                md5_obj.update(t)
                receive_data_len += len(t)
        md5_server_val = md5_obj.hexdigest()
        print("md5_server_val:", md5_server_val)
        md5_client_val_bytes = conn.recv(1024)
        print("md5_client_val_bytes:", md5_client_val_bytes)
        if md5_client_val_bytes.decode() == md5_server_val:
            print("文件上传成功！")
        else:
            print("上传文件不完整！")

    def get(self, conn, params):
        # (1) 将文件信息上传给服务器

        file_name = params.get("file_name")
        local_path = f"./uploads/{file_name}"

        # 文件是否存在
        is_file = os.path.isfile(local_path)
        params = {}
        if is_file:
            file_size = os.path.getsize(local_path)
            file_name = os.path.basename(local_path)
            params["file_size"] = file_size
            params["file_name"] = file_name
            params["is_file"] = True
        else:
            params["is_file"] = False

        data = json.dumps(params).encode()
        conn.send(struct.pack("i", len(data)))
        conn.send(data)

        # (2)  将文件数据包上传给服务器

        if is_file:
            with open(local_path, "rb") as f:
                for line in f:
                    conn.send(line)
            print("文件下载成功！")


ftp_server = FTPServer()
ftp_server.run()
