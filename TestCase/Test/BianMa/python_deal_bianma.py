#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''下载附件cfiles.zip（见附件cfiles.zip）

解压该压缩包，里面 包含了两个文件。 一个叫 'gbk编码.txt',
该文件是gbk编码的。
另一个文件叫 'utf8编码.txt', 该文件是utf8编码的。
两个文件里面的内容都包含中文。

要求大家编写一个python程序，该程序做到以下2点

1. 将两个文件内容读出， 合并内容到一个字符串中，
   并能用print语句将合并后的内容正确显示
   
2. 然后，程序用中文提示用户“请输入 新文件的名称”，
   用户输入文件名可以包含中文
   将上面合并后的内容存储到一个新文件中，以utf8格式编码。
   新文件的文件名就是上面用户输入的名字。'''


import os, sys

gbk_file_dir = os.getcwd() + r'\cfiles\gbk编码.txt'
utf_file_dir = os.getcwd() + r'\cfiles\utf8编码.txt'
new_file_dir = r'D:\TDdownload\Document\Python\test\BianMa'


#用什么编码的文件，就用什么格式encoding
with open(gbk_file_dir,'r',encoding='gbk') as gf:
    g_content = gf.read()



with open(utf_file_dir,'r',encoding='utf8') as uf:
    u_content = uf.read()


content = g_content + u_content
print(content)

new_name = input('请输入新文件的名称：')

with open('%s/%s.txt' % (new_file_dir,new_name),'w',encoding='utf8') as nf:
    nf.write(content)


