import json
import os.path
import socket
import struct


def get(sock, filename):
    # (1) 将文件信息上传给服务器

    params = {"file_name": filename, "cmd": "get"}
    data = json.dumps(params).encode()
    sock.send(struct.pack("i", len(data)))
    sock.send(data)

    # (2) 循环接受文件大数据

    file_params_head = sock.recv(4)  # 阻塞函数
    data_json_bytes_len = struct.unpack("i", file_params_head)[0]

    data_json_bytes = sock.recv(data_json_bytes_len)  # 阻塞函数
    params = json.loads(data_json_bytes.decode())

    file_name = params.get("file_name")
    file_size = params.get("file_size")

    with open(f"./user/{file_name}", "wb") as f:
        receive_data_len = 0
        while receive_data_len < file_size:
            t = sock.recv(1024)
            f.write(t)
            receive_data_len += len(t)

        print("文件下载成功！")


def put(sock, local_path):
    # (1) 将文件信息上传给服务器

    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)
    params = {"file_name": file_name, "file_size": file_size, "cmd": "put"}
    data = json.dumps(params).encode()
    sock.send(struct.pack("i", len(data)))
    sock.send(data)

    # (2)  将文件数据包上传给服务器

    with open(local_path, "rb") as f:
        for line in f:
            sock.send(line)

    print("文件上传成功！")


def main():
    # (1) 构建客户端套接字对象
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # (2) 连接服务器
    sock.connect(("127.0.0.1", 9999))

    while 1:
        inp = input("命令【put media/红唇.jpg】")
        cmd = inp.split(" ")[0]
        local_path = inp.split(" ")[1]

        if cmd == "get":
            get(sock, local_path)

        elif cmd == "put":
            put(sock, local_path)
        else:
            print('错误命令！')


if __name__ == '__main__':
    main()
