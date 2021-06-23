#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg
import socket
import threading
import time

ip_port = ('127.0.0.1',9999)

'''
服务器可能有多块网卡，可以绑定到某一块网卡的ip上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址
127.0.0.1是一个特殊的ip地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说外部计算机无法连接进来
'''

#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#绑定监听地址和端口
s.bind(ip_port)


#启动监听
#引入参数5代表等待连接的最大数量
s.listen(5)


#定义连接时，该线程的操作
'''
连接建立后，服务器首先发送一条欢迎消息，然后等待客户端数据，加上hello再发给客户端，如果客户端发送了exit字符串，就直接关闭连接。
'''
def tcplink(sock,addr):
    print('Accept new connection from %s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf8') == 'exit':
            break
        sock.send(('hello,%s' % data.decode('utf8')).encode('utf8'))
    sock.close()
    print('Connection from %s closed.' % addr)





#服务器程序通过永久循环接收来自客户端的连接，使用accept()函数，等待并返回一个客户端连接
while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()






























if __name__ == "__main__":
    pass