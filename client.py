import socket
sk = socket.socket()           # 创建客户套接字
sk.connect(('41r6s98972.wicp.vip',33516))    # 尝试连接服务器
sk.send(b'hello!')
ret = sk.recv(1024)         # 对话(发送/接收)
print(ret)
sk.close()            # 关闭客户套接字
