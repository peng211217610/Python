from appium import webdriver
import time


desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7',
    'deviceName': 'xxx',
    # 'app': r'd:\apk\HiSpace.apk',
    'appPackage': 'com.ibox.calculators',
    'appActivity': 'com.ibox.calculators.SplashActivity',
    'noReset': True,
    'newCommandTimeout': 6000,
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)


driver.find_element_by_xpath(
    '//*[@resource-id="com.ibox.calculators:id/digit3"]').click()
driver.find_element_by_id('plus').click()
driver.find_element_by_id('digit9').click()
equal = driver.find_element_by_id('equal')
equal.click()
driver.find_element_by_id('mul').click()
driver.find_element_by_id('digit5').click()
equal.click()

xpath='//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]'

result = driver.find_element_by_xpath(xpath)

if result.text == '60':
    print('计算正确')
else:
    print('计算错误')