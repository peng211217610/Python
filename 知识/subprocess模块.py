#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''subprocess可调用外部程序'''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg


import subprocess

#os.system('dir') 这个命令也可以调用外部程序，但是返回的只有返回码。

ret = subprocess.check_output('dir',shell=True,encoding='gbk')

#shell=True的意思是掉用cmd.exe的shell模式（就是不用打开cmd）

ret_2 = subprocess.Popen(args=['mspaint',r'e:\1.jpg','encoding="utf8"'])

#Shell = True表示用shell执行，args是字符串，例如：'mspaint e:\1.jpg'
#shell = False表示非shell执行，args是一个列表
#check_output默认是shell，Popen默认是非shell
#check_output需要程序退出才会继续执行下面的代码，而Popen不需要

#获取输出
p = subprocess.Popen(
    'dir c:',
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    encoding='gbk'
)

output,err = p.communicate()
print(output)

#如上，stdout可以将输出内容写入到PIPE中，output变量取所有输出内容


#获取输入
popen2 = subprocess.Popen(
    'python s4_1.py',
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    encoding='gbk'
)
#由于s4_1.py中包含input命令，需要手动输入，可以通过communicate传入
inputList = ['3','4','5','6']
out,err2 = popen2.communicate('\n'.join(inputList))







