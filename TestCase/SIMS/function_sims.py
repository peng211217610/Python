#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''学生信息管理系统'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
from configure import *
from random import randint
from Project.SIMS.function_menu import *            #引入菜单函数

#主函数
def main():
    ctrl = True                                     #标记是否退出系统，只有登录状态才能操作
    while ctrl:
        menu()                                      #显示菜单
        option = input('请选择：')










if __name__=="__main__":
    pass