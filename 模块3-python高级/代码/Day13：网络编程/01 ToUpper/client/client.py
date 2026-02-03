import socket

# (1) 构建客户端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 连接服务器
sock.connect(("127.0.0.1", 8899))

while 1:
    name = input("请输入转换的姓名(英文):")

    # (3) 发消息: 网络传输的数据一定是字节串
    sock.send(name.encode())

    #  # 客户端退出
    if name == "quit":
        break

    # (4) 接受来自于服务的响应消息
    res = sock.recv(1024)

    print("来自于服务的响应消息：", res.decode())
