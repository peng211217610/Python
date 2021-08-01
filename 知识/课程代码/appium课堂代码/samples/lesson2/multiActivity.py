from appium import webdriver
import time,traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'd:\apk\toutiao.apk'
desired_caps['appPackage'] = 'com.huawei.appmarket'
desired_caps['appActivity'] = '.MarketActivity'
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000


# desired_caps['automationName'] = 'uiautomator2'
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)


input('**** Press to quit..')
driver.quit()


