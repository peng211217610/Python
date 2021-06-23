#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''初始化移动端驱动'''

#引入相关包
from appium import webdriver



# apk=("com.xueqiu.android","com.xueqiu.android.view.WelcomeActivityAlias")#雪球

# apk=("com.tencent.mobileqq","com.tencent.mobileqq.activity.SplashActivity")#qq
apk=("com.chaoxing.mobile",".activity.SplashActivity")#学习通

desired_caps={
    "platformName":"Android",
    "platformVersion":'9.0',
    "deviceName":"Mate-9",
    "browserName":"",
    "appPackage":apk[0],
    "appActivity":apk[1],
    "noReset":True,
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)











if __name__=="__main__":
    pass