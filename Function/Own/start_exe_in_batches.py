#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''批量启动软件'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from random import randint


def start_exe_in_batches(exeList):
    exe = exeList.splitlines()[1:]
    for one in exe:
        os.startfile(one)
        time.sleep(1)


#要打开的程序列表
exeList = r'''
C:\Myprograms\J-计算机\UltraEdit\uedit64.exe
'''


if __name__=="__main__":
    start_exe_in_batches(exeList)