#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''paramiko库远程操作Linux'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
import paramiko



#操作Linux
def paramiko_operate_linux(remoteServer,cmd):
    ssh = paramiko.SSHClient()
    # 调用方法，表示没有存储远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname,port,username,password = remoteServer
    ssh.connect(hostname,port,username,password)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    print(stdout.read())
    ssh.close()



if __name__ == '__main__':
    #先定义cmd变量
    cmd = '''cd /'''
    paramiko_operate_linux(cfg.remoteServer,cmd)