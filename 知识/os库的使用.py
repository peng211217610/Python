#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''os库的使用'''

# 引入包
import os

#返回当前工作目录
print(os.getcwd())

#组合路径
os.path.join('a','b','c')

#创建文件夹
os.makedirs(os.path.join(os.getcwd(),'dirname1','dirname2'))
os.mkdir('dirname')

#切换工作目录,path是目标路径
os.chdir(path)

#返回路径字符串
os.path.abspath('.')
os.path.abspath('..')


path=r'E:\TDdownload\a.txt'

#获取文件名
filename=os.path.basename(path)

#获取路径
dirname=os.path.dirname(path)

#获取文件路径、文件名元组
os.path.split(path)

#获取文件按字节计算的大小
os.path.getsize(path)

#查看文件夹下所有文件，返回文件列表
os.listdir('dir')

#判断文件或文件夹是否存在
os.path.exists(path)

os.path.isfile(path)

os.path.isdir(path)






if __name__ == "__main__":
    pass
