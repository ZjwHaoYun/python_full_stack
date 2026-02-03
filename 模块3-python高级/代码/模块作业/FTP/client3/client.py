import json
import os.path
import socket
import struct
import time
from hashlib import md5


class FTPClient(object):

    def __init__(self):
        # (1) 构建客户端套接字对象
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        # (2) 连接服务器
        self.sock.connect(("127.0.0.1", 8888))

    def run(self):
        while 1:
            inp = input("【get 文件或者 put 文件】")
            inp_list = inp.split(" ")
            cmd = inp_list[0]
            local_path = inp.split(" ")[1]

            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(local_path)

    def put(self, local_path):
        # (1) 将文件信息上传给服务器

        file_size = os.path.getsize(local_path)
        file_name = os.path.basename(local_path)
        params = {"file_name": file_name, "file_size": file_size, "cmd": "put"}
        data = json.dumps(params).encode()
        self.sock.send(struct.pack("i", len(data)))
        self.sock.send(data)

        # (2)  将文件数据包上传给服务器
        md5_obj = md5()
        with open(local_path, "rb") as f:
            for line in f:
                self.sock.send(line)

                md5_obj.update(line)

        md5_val = md5_obj.hexdigest()
        print("md5_val:::", md5_val)

        self.sock.send(md5_val.encode())
        print("文件上传成功！")

    def get(self, filename):
        # (1) 将文件信息上传给服务器

        params = {"file_name": filename, "cmd": "get"}
        data = json.dumps(params).encode()
        self.sock.send(struct.pack("i", len(data)))
        self.sock.send(data)

        # (2) 循环接受文件大数据

        file_params_head = self.sock.recv(4)  # 阻塞函数
        data_json_bytes_len = struct.unpack("i", file_params_head)[0]

        data_json_bytes = self.sock.recv(data_json_bytes_len)  # 阻塞函数
        params = json.loads(data_json_bytes.decode())

        is_file = params.get("is_file")
        if not is_file:
            print("该文件不存在！")
            return
        file_name = params.get("file_name")
        file_size = params.get("file_size")

        with open(f"./user/{file_name}", "wb") as f:
            receive_data_len = 0
            while receive_data_len < file_size:
                t = self.sock.recv(1024)
                f.write(t)
                receive_data_len += len(t)
                self.show_progress(receive_data_len, file_size)

        print("文件下载成功！")

    @staticmethod
    def show_progress(current, total):
        bar_length = 100
        filled_length = int(bar_length * current / total)
        percent = round(100.0 * current / total, 1)

        bar = "=" * filled_length + "-" * (bar_length - filled_length)
        progress_msg = f"\r[{bar}{percent}]"
        print(progress_msg, end="")


ftp_client = FTPClient()
ftp_client.run()
