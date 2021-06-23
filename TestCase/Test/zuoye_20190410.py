#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''
先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。

http://docs.python-requests.org/zh_CN/latest/user/quickstart.html


然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容

http://mirrors.163.com/centos/6/isos/x86_64/README.txt
http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt

主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中

'''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys
import requests
sys.path.append(pythonPath)
import configure as cfg
import threading

def get_first_content():
    url = 'http://mirrors.163.com/centos/6/isos/x86_64/README.txt'
    r = requests.get(url)
    global str1
    str1 = r.text


def get_second_content():
    url = 'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt'
    r = requests.get(url)
    global str2
    str2 = r.text



if __name__ == "__main__":
    t1 = threading.Thread(target=get_first_content())
    t2 = threading.Thread(target=get_second_content())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    with open(r'D:\TDdownload\readme89.txt','w') as re:
        re.write(str1+str2)
