# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'test'
desired_caps['browserName'] = 'Chrome'
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC

driver.implicitly_wait(10)
try:

    driver.get('http://www.baidu.com')

    driver.find_element_by_id('index-kw').send_keys('松勤')

    driver.find_element_by_id('index-bn').click()

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()