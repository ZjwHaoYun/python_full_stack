# 服务端

import socket
import time

s = socket.socket()
s.bind(("127.0.0.1", 9999))
s.listen(5)

client, addr = s.accept()
time.sleep(10)
data = client.recv(1024)
print(data)

client.send(data)
