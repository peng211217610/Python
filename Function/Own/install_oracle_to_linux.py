#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''Linux上安装Oracle'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg


import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.145.129',22,'root','Winovs12')
sftp = ssh.open_sftp()

sftp.put(r'D:\TDdownload\系统镜像\linuxx64_12201_database.zip','/home')


ssh.close()



if __name__ == "__main__":
    pass