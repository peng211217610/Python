#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''登陆电影天堂'''

#变量


#引入相关包
from Config.env_variable import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pywin





#选择浏览器
if browser == 'Chrome':
    opt = webdriver.ChromeOptions()
# elif browser == 'Firefox':
#     opt = webdriver.()
else:
    opt = webdriver.Ie()


opt.add_experimental_option('w3c',False)
open_browser=webdriver.Chrome(options=opt)

executor_url = open_browser.command_executor._url
session_id = open_browser.session_id

open_browser.implicitly_wait(10)
open_browser.maximize_window()

driver=ReuseChrome(command_executor=executor_url, session_id=session_id)




#打开网页
def open_url(url):
    driver.get(url)


#等待元素展示



#点击鼠标右键，图片另存为
'''
移动到图片上，点击鼠标右键，输入键盘字母v，定位到窗口，修改文件名，点击保存
'''
def right_click_and_save_picture_to():
    pass






#关闭标签页或浏览器
def close_url(mode):
    if mode=='close':
        driver.close()
    else:
        driver.quit()




if __name__=="__main__":
    pass