import socket
import time

# (1) 构建客户端套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# (2) 连接服务器
sock.connect(("127.0.0.1", 9999))

while 1:
    cmd = input("请输入远程执行命令:")
    # (3) 发消息: 网络传输的数据一定是字节串
    sock.send(cmd.encode())
    #  客户端退出
    if cmd == "quit":
        break
    # (4) 接受来自服务的响应消息
    # res = sock.recv(1000000)
    # 接受数据长度
    time.sleep(5)
    cmd_ret_length_bytes = sock.recv(3)
    print("cmd_ret_length_bytes:::", cmd_ret_length_bytes)

    total_size = int(cmd_ret_length_bytes.decode())

    recv_size = 0
    while recv_size < total_size:
        data = sock.recv(1024)
        print(data.decode())
        recv_size += len(data)
    print("recv_size:", recv_size)
    # print("来自于服务器的响应结果：", res.decode(), len(res))
