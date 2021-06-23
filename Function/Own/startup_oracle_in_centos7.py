#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''开启远程Oracle数据库'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'

#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from Own.paramiko_To_Linux import paramiko_operate_linux



cmd ='''#!/usr/bin/bash
su - oracle -c "lsnrctl start;sqlplus / as sysdba" << EOF
startup
EOF
'''



if __name__=="__main__":
    paramiko_operate_linux(cfg.remoteServer,cmd)