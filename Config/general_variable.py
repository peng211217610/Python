#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''基础配置'''

#引入相关包
import os,sys,time,shutil,json
from random import randint,choice,uniform
import pytest,pytest_html,pytest_parallel,pytest_rerunfailures
from Function.Common.function_common import myTime

#selenium驱动地址
ChromeDriver_path = r'D:\TDdownload\Document\Python\chromedriver.exe'
FirefoxDriver_path = r'D:\TDdownload\Document\Python\geckodriver.exe'

#JS操作滚动条位置
up="document.documentElement.scrollTop=0"
middle="document.documentElement.scrollTop=1500"
down="document.documentElement.scrollTop=10000"

#时间戳
now_time=myTime().mytimestamp()

#Linux远程主机登陆地址
#remoteServer = ('192.168.145.128',22,'root','huawei')
#remoteServer = ('192.168.145.129',22,'root','Winovs12')
remoteServer = ('192.168.145.130',22,'root','Winovs12')

#mysql连接地址，依次为：ip,端口，数据库用户名，密码，数据库名，编码方式
mysqlInfo = json.loads('''{"host":"XXXX","port":3306,"user":"dbAdmin","passwd":"Pr0d1234","database":"service4sit","charset":"utf-8"}''')

#Oracle连接地址
oracleInfo = 'phm/Winovs12@192.168.145.130:1521/orcl'

#常用文件夹地址
python_dir = r'D:\TDdownload\Document\Python'

#接口常用
#【谷歌浏览器】User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

#字符变量
greece="αβγδεζηθι ℩κλμνξοπρφχψω"
fangxiang="←↑→↓↖↙↗↘↕"

#划线
line1="================================================================================================================================"
line2="================================================================"
line3="================================"

#教管系统
host = 'http://localhost:8080'
url = 'http://localhost:8080/mgr/login/login.html'
teachUserInfo = (url,'auto','sdfsdfsdf')

#教管系统使用mysql数据库
'''
#用户名songqin,密码songqin
CREATE USER 'songqin'@'localhost' IDENTIFIED BY 'songqin';
CREATE USER 'songqin'@'%' IDENTIFIED BY 'songqin';
#给songqin授予建数据库权限
GRANT ALL ON *.* TO 'songqin'@'localhost';
GRANT ALL ON *.* TO 'songqin'@'%';
#导入SQL文件（完成建表导入数据库）
plesson.sql文件在TMS下面
#将教管系统的数据库连到mysql上去
修改C:\Myprograms\Y-qita\RestAPI\restapi-teach\backend\project\settings.py
把第二个DATABASES的注释去掉，修改ip等
#由于mysql版本的问题，需要修改setting.py中DATABASES的storage_engine为default_storage_engine
如果不修改会报错：django.db.utils.OperationalError: (1193, "Unknown system variable 'storage_engine'")
'''
