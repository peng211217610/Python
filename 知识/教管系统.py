#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

# 引入包

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

if __name__ == "__main__":
    pass
