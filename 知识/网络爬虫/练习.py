#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''网络爬虫练习'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from random import randint


import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}

url = 'http://www.santostang.com'

r = requests.get(url,headers=headers)

#print(r.text)

soup = BeautifulSoup(r.text,'lxml')

title = soup.find("h1",class_="post-title").a.text.strip()

print(title)


if __name__=="__main__":
    pass