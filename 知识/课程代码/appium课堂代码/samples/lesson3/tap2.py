from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 测试平台
desired_caps['platformVersion'] = '7'  # 平台版本,不能写错
desired_caps['deviceName'] = 'test'  # 设备名称，多设备时需区分
# desired_caps['app'] = r'd:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'  # app package名
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'  # app默认Activity
desired_caps['unicodeKeyboard'] = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动Remote RPC
driver.implicitly_wait(10)
print(driver.session_id)

# 不得不用sleep
import time
time.sleep(10)

from cfg import cfg_phone_resolution,coordinates

coordinate = coordinates[cfg_phone_resolution]


driver.tap([coordinate['首页_+']], 300)
time.sleep(2)


driver.tap([coordinate['登录页_邮箱图标']], 300)
time.sleep(1)

driver.tap([coordinate['登录页_邮箱地址']], 300)
time.sleep(1)

# 没有WebElement对象 ，如何输入字符？
# adb shell input text "<your string>"

import os
os.system('adb shell input text "jcyrss@163.com"')
#注意，如果要输入中文，需要下载一个adb键盘应用，
# 参考 https://blog.csdn.net/slimboy123/article/details/54140029

time.sleep(1)

driver.tap([coordinate['登录页_邮箱密码']], 300)
time.sleep(1)
os.system('adb shell input text "sdfsdf"')

driver.tap([coordinate['登录页_登录按钮']], 300)

input('**** Press to quit..')
driver.quit()