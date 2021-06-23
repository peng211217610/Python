#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''BeautifulSoup4的用法'''


#导入库的写法，如下
from bs4 import BeautifulSoup
import html5lib

with open('bs4.html',encoding='utf8') as f:
    html_doc = f.read()


#下面这句话是重点
soup = BeautifulSoup(html_doc,'html5lib')


#在soup内容里找出包含a的，注意find的用法
tag = soup.find('a')








