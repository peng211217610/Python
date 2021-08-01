#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''初始化webdriver，驱动放在：C:\Myprograms\Y-qita\Python，设置PYTHONPATH，D:\TDdownload\Document\Python'''

#引入相关包
from Config.common_variable import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Remote
from selenium.webdriver.chrome import options
from selenium.common.exceptions import InvalidArgumentException

#重写remote类，一次执行使用同一个session
class ReuseChrome(Remote):

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = options.Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False


#选择浏览器并对浏览器做设置
def init_webdriver(browser_choice):
    global driver
    if browser_choice == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        # options.add_argument(r'--user-data-dir=C:\User\pwx1049557\AppData\Local\Google\Chrome\User Data\automation')#加载用户数据
        options.add_experimental_option("excludeSwitches",['enable-automation'])#禁用浏览器正在被自动化程序控制的提示
        # options.add_argument("--disable-popup-blocking")
        # options.add_argument("no-default-browser-check")
        # options.add_argument("no-sandbox")
        options.add_experimental_option("prefs",{"credentials_enable_service":False,"profile.password_manager_enabled":False})#关闭保存密码提示框
        #使用已打开的浏览器操作
        # options.add_experimental_option("debuggerAddress","127.0.0.1:8881")
        driver = webdriver.Chrome(options=options)
    elif browser_choice == "Firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver

open_browser = init_webdriver(browser_choice)
executor_url = open_browser.command_executor._url
session_id = open_browser.session_id
driver = ReuseChrome(executor_url,session_id)
driver.maximize_window()
driver.implicitly_wait(25)


#句柄相关操作
handle=driver.current_window_handle#获取初始句柄
class Handle():

    def __init__(self):
        pass

    # 切换到最新的句柄
    def switch_to_the_latest_handle(self):
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

    # 打开新窗口并切换到最新的句柄
    def open_window_and_switch_to_the_latest_handle(self):
        driver.execute_script('window.open()')
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

    # 关闭当前窗口并切换到最新窗口，并把最新窗口设置为初始窗口
    def close_current_window_and_switch_to_the_latest_handle(self):
        global handle
        handles = driver.window_handles
        for one in handles:
            driver.switch_to.window(one)
            if one != handles[-1]:
                driver.close()
            else:
                handle = driver.current_window_handle

    # 关闭当前窗口并返回初始句柄
    def close_current_window_and_swtich_back_to_initial_handle(self):
        handles = driver.window_handles
        [driver.close() for one in handles if one != handle]
        driver.switch_to.window(handle)

    # 关闭当前操作窗口并切换到跳转之前的窗口
    def close_current_window_and_switch_back_to_former_handle(self,former_handle):
        handles = driver.window_handles
        [driver.close() for one in handles if one != handle]
        driver.switch_to.window(former_handle)

    # 打开多个空白窗口
    def open_new_handle(self,i):
        one = 1
        while one <= i:
            self.switch_to_the_latest_handle()
            driver.execute_script('window.open()')
            one += 1

#谷歌页面提示“您的连接不是私密连接”
def chrome_you_link_not_privite():
    driver.find_element_by_xpath('//button[contains(text(),"高级")]').click()
    driver.find_element_by_xpath('//a[@id="proceed-link"]').click()




if __name__=="__main__":
    pass