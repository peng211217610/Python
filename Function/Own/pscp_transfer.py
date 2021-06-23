#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''Windows和Linux互相传文件和文件夹'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'

#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg



def Window_to_Linux_File(remoteServer,window_path,linux_path):
    cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} {window_path} {username}@{linux_ip}:{linux_path}'.format(
        password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0], linux_path=linux_path
    )
    os.system(cmd)


def Window_to_Linux_Dir(remoteServer,window_path,linux_path):
    cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} -r {window_path} {username}@{linux_ip}:{linux_path}'.format(
        password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0], linux_path=linux_path
    )
    os.system(cmd)


def Linux_to_Window_File(remoteServer,linux_path,window_path):
    cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} {username}@{linux_ip}:{linux_path} {window_path}'.format(
        password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0], linux_path=linux_path
    )
    os.system(cmd)


def Linux_to_Window_Dir(remoteServer,linux_path,window_path):
    cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} -r {username}@{linux_ip}:{linux_path} {window_path}'.format(
        password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0], linux_path=linux_path
    )
    os.system(cmd)


if __name__ == '__main__':
    Window_to_Linux_File(cfg.remoteServer,r'D:\TDdownload\Document\Python\test\memory.py','/home')
    # Window_to_Linux_Dir(cfg.remoteServer,r'D:\TDdownload\Software', '/home')
    # Linux_to_Window_File(cfg.remoteServer,'/home/aaa.txt', r'D:\TDdownload\Software')
    # Linux_to_Window_Dir(cfg.remoteServer,'/home/phm', r'D:\TDdownload\Software')