import json
import os.path
import socket

# (1) 构建客户端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 连接服务器
sock.connect(("127.0.0.1", 8899))

while 1:
    inp = input("命令【put a.png】")

    # (1) 将文件信息上传给服务器
    local_path = inp.split(" ")[1]
    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)
    file_params = {"file_name": file_name, "file_size": file_size}
    sock.send(json.dumps(file_params).encode())

    # (2)  将文件数据包上传给服务器

    with open(local_path, "rb") as f:
        for line in f:
            sock.send(line)

    print("文件上传成功！")
