#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''基础配置'''

#引入相关包
from Function.Common.function_common import *

#JS操作滚动条位置
up="document.documentElement.scrollTop=0"
middle="document.documentElement.scrollTop=1500"
down="document.documentElement.scrollTop=10000"
# up="window.scrollTo(0,0)"
# down="window.scrollTo(0,document.body.scrollHeight)"

#时间戳
now_time=myTime().mytimestamp()#int类型
mytimestamp=str(now_time)#转换成str型

#Linux远程主机登陆地址
#remoteServer = ('192.168.145.128',22,'root','huawei')
#remoteServer = ('192.168.145.129',22,'root','Winovs12')
remoteServer = ('192.168.145.130',22,'root','Winovs12')

#Oracle连接地址
oracleInfo = 'phm/Winovs12@192.168.145.130:1521/orcl'

#常用文件夹地址
python_dir = get_python_dir()
Document_dir = os.path.dirname(python_dir)
td_dir=os.path.dirname(Document_dir)
testfile_dir = os.path.join(Document_dir,'TestFile')

#字符变量
greece="αβγδεζηθικλμνξοπρστυφχψω"
fangxiang="←↑→↓↖↙↗↘↕"

#划线
line1="================================================================================================================"
line2="========================================================"
line3="============================"


