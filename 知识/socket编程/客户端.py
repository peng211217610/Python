#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''客户端操作'''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg

import socket

#要连接的服务
ip_port = ('127.0.0.1',9999)


#创建一个socket对象
'''
创建socket时，AF_INET指定使用IPV4协议，如果要用IPV6，就指定为AF_INET6.SOCK_STREAM指定使用面向流的TCP协议。这样，一个socket对象
就创建成功，但是还没有建立连接。
'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#建立连接
'''
标准服务端口：SMTP服务是25端口，FTP服务是21端口，Web服务是80端口，端口号小于1024的是Internet标准服务端口，端口号大于1024的，可以任意使用。
'''
s.connect(ip_port)


#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
'''
接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此在一个while循环中反复接收，知道recv()返回空数据，表示接收完毕，退出循环。
'''
buffer = []
while True:
    #每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)


#关闭连接
s.close()


#对返回内容处理
'''
接收到的数据包括http头部和网页本身，我们只需要把http头部和网页分离一下，把http头部打印出来，网页内容保存到文件
'''
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf8'))
with open('sina.html','wb') as f:
    f.write(html)
















if __name__ == "__main__":
    pass