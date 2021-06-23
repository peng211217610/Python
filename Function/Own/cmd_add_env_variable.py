#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''批量添加环境变量'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from random import randint
import subprocess


#先查看存在哪些环境变量
def find_all_variable():
    popen = subprocess.Popen(
        'wmic ENVIRONMENT get name,VariableValue',
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        encoding='gbk'
    )
    # output,err=popen.communicate()
    # print(output)
    # contentList = output.replace(' ','')
    # print(contentList)
    input = popen.stdout.read()
    print(input)










if __name__=="__main__":
    find_all_variable()