# coding=utf-8
from socket import *

HOST = '127.0.0.1'
SERVER_PORT = 21567
BUFSIZ = 1024
SERVER_ADDR = (HOST, SERVER_PORT)

#创建socket，指明协议
tcpCliSock = socket(AF_INET, SOCK_STREAM)

#连接远程地址和端口，发送syn，等待 syn ack，也是阻塞式的
tcpCliSock.connect(SERVER_ADDR)

while True:
    data = input('>> ')
    if  data =='':
        break
    #     发送消息，必须是 bytes类型
    tcpCliSock.send(data.encode())

    # 阻塞式等待接收消息
    data = tcpCliSock.recv(BUFSIZ)
    # 当对方关闭连接的时候，返回空字符串
    if not data:
        break
    # 解码打印字符串
    print(data.decode())

tcpCliSock.close()