#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

# 引入包



'''
和burpsuite类似mitmproxy默认只能拦截http，想要拦截https那就需要安装证书。

安装的时候提示输入密码，输入任意字符都会提示密码错误。不输入可以下一步。

首先到$PYTHON_HOME/Scripts目录下运行一下mitmdump，完成之后在用户家目录下的.mitmproxy文件夹下即会生成证书，传到手机点击安装即可。
Windows安装证书：双击mitmproxy-ca-cert.p12----全部默认直接点“下一步”直到安装完成。

 Android安装证书：把mitmproxy-ca-cert.cer通过usb复制到手机上----点击使用证书安装器安装证书（通过qq发送到手机上时提示无法读取证书不懂什么原因）
'''


if __name__ == "__main__":
    pass
