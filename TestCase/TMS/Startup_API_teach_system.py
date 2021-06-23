#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
教管系统相关说明
1.系统包放在D:\TDdownload\Document\Python\test\API，包名：restapi-teach6.zip
2.如果包遗失，到https://github.com/jcyrss/songqin-testdev/raw/master/webapi/code/restapi-teach6.zip下载
3.解压双击运行install.bat，安装必要的库
4.最后双击run.bat即可运行该web系统。
5.如果端口占用，修改C:\Myprograms\Y-qita\RestAPI\restapi-teach\backend\project\cherrypy_startup.py
6.http://localhost:port/mgr/login/login.html(修改端口号)
7:管理员用户名auto，密码为 sdfsdfsdf
'''
run_bat = r'C:\Myprograms\Y-qita\RestAPI\restapi-teach'

import os
print(os.getcwd())
os.chdir(run_bat)
os.system('run.bat')

