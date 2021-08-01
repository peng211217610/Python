from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'd:\apk\HiSpace.apk'
desired_caps['appPackage'] = 'com.huawei.appmarket'
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity' #app默认Activity
# desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:
    # ------------------------------

    code = 'new UiSelector().resourceId("com.huawei.appmarket:id/tabLayout").childSelector(new UiSelector().text("排行"))'
    driver.find_element_by_android_uiautomator(code).click()

    javaCode = 'new UiSelector().text("总榜").resourceId("com.huawei.appmarket:id/ItemTitle")'
    ele = driver.find_element_by_android_uiautomator(javaCode)
    destPosY = ele.location['y']
    xPos = ele.location['x']

    driver.implicitly_wait(0.5)
    while True:
        driver.swipe(xPos, destPosY, xPos, destPosY - 100, 1000)
        javaCode = 'new UiSelector().text("口碑最佳").resourceId("com.huawei.appmarket:id/ItemTitle")'
        eles = driver.find_elements_by_android_uiautomator(javaCode)

        # 口碑最佳 还没出现
        if not eles:
            continue

        # 口碑最佳出现了,将当前位置移到 目标位置
        driver.swipe(xPos, eles[0].location['y'], xPos, destPosY, 3000)
        break

    driver.implicitly_wait(10)

    textList = []
    eles = driver.find_elements_by_class_name('android.widget.TextView')
    for ele in eles:
        text = ele.text
        print(text)
        textList.append(text)

    # 查到口碑最佳的 元素位置
    startPos = textList.index('口碑最佳')
    # 去掉口碑最佳前面的内容，
    # 防止后面根据id取内容的时候，取到前面的
    textList = textList[startPos:]

    def getName(No):
        noIndex = textList.index(No)
        return  textList[noIndex + 1]

    for i in range(1,6):
        print(getName(str(i)))


# ------------------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()

