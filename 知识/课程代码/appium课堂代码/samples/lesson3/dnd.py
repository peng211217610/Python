from appium import webdriver
import  time
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '7'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分

# 怎么打开桌面？
# 可以用命令 adb shell dumpsys activity recents | find "intent={"
# 查看
desired_caps['appPackage'] = 'com.miui.home'  #app package名
desired_caps['appActivity'] = '.launcher.Launcher' #app默认Activity
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

# 长按某个应用图标
time.sleep(3)

from appium.webdriver.common.touch_action import TouchAction
action = TouchAction()

input('**** Press to quit..')
driver.quit()