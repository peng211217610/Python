#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''用Python脚本在Linux上安装Python3'''

'''
注意：CentOS的/usr/bin/yum是使用Python2.7的，尽量不要卸载旧版本，直接安装新版本即可

思路：
准备阶段：
需要设置信任关系-----------OK
判断D:\TDdownload\Software有没有安装包，安装包名字是变量，写在配置里
如果有安装包，打开securecrt，登陆Linux环境，环境信息写在配置里
如果没有安装包，则分情况：1.Linux可以上网。2.Linux不能上网，谷歌浏览器可以。3.都不能上网。
Linux可上网：直接用weget命令
Linux不能上网，用selenium登陆网址下载
都不能上网，系统终止。从别的地方获取安装包放到路径下再重新执行
登陆上去以后，卸载
'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
import Own.pscp_transfer as pscp
import Own.paramiko_To_Linux as po


window_path = r'D:\TDdownload\Software\%s' % cfg.Python_version
linux_path = '/usr/local'


#通过Windows向Linux传Python安装包，传到/usr/local
if os.path.isfile(window_path):
    pscp.Window_to_Linux_File(cfg.remoteServer,window_path,linux_path)
else:
    print('这个目录下没有Python安装包！')
    sys.exit()

#如果没有Python安装包，通过selenium获取

#通过weget命令获取安装包，传到/usr/local
# cmd = '''cd /usr/local
# wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
# '''
#
# po.paramiko_operate_linux(cmd)


#安装到/usr/bin/python3下

#1.上传shell脚本并赋权限、执行
pscp.Window_to_Linux_File(cfg.remoteServer,r'D:\TDdownload\Document\Shell\backup_common\install_python3_to_linux.sh','/home')

cmd = '''cd /home
chmod +x /home/install_python3_to_linux.sh
./install_python3_to_linux.sh %s;
''' % cfg.Python_version

po.paramiko_operate_linux(cfg.remoteServer,cmd)