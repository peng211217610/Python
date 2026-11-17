#!/usr/bin/python3
# -*- coding: utf-8 -*-
#备注
remark = '''初始化移动端驱动'''

#引入相关包
from Function.Oppty.function_oppty_common import *
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


# apk=("com.xueqiu.android","com.xueqiu.android.view.WelcomeActivityAlias")#雪球
# apk=("com.tencent.mobileqq","com.tencent.mobileqq.activity.SplashActivity")#qq
# apk=("com.chaoxing.mobile",".activity.SplashActivity")#学习通
# apk=("io.manong.developerdaily","io.toutiao.android.ui.activity.LaunchActivity")#头条
apk=("com.android.settings",".Settings")#设置

#apk也写成配置，从文件读取，用应用名称作为键名然后在这里设置全局变量appPackage和appActivity


desired_caps={
    "platformName":"Android",
    "appium:deviceName":"2TP6R22217004013",
    "appium:automationName":"UiAutomator2",
    "appium:appPackage":apk[0],# APK包名
    "appium:appActivity":apk[1],# APK包名
    "appium:noReset":True,
    "resetKeyboard":False,
    "appium:newCommandTimeout":300,
    "appium:autoGrantPermissions":True
}










'''
Appium输入中文
需要在启动参数中添加2个参数
# 启用Unicode输入法，设置为true可以输入中文字符，默认为false
"unicodeKeyboard":True,
# 在设定了`unicodeKeyboard`关键字运行Unicode测试结束后，将键盘重置为其原始状态
"resetKeyboard":True


"app":r'd:\apk\toutiao.apk' #如果没有安装，可以给移动端安装APP
'newCommandTimeout': 6000,
'''


class Driver:

    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            optiton = UiAutomator2Options().load_capabilities(desired_caps)
            cls.driver = webdriver.Remote("http://127.0.0.1:4723",options=optiton)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None





# driver=webdriver.Remote("http://127.0.0.1:4723",options=UiAutomator2Options().load_capabilities(desired_caps))
# driver.implicitly_wait(10)











if __name__=="__main__":
    pass