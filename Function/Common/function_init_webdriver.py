#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''初始化webdriver，驱动放在：C:\Myprograms\Y-qita\Python，设置PYTHONPATH，D:\TDdownload\Document\Python'''

#引入相关包
from selenium import webdriver
from Config.common_variable import *
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


#选择浏览器，并对浏览器做初始化设置
def get_driver(browser_choice):
    if browser_choice == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        init_driver = webdriver.Chrome(options=options)
    elif browser_choice == "Firefox":
        init_driver = webdriver.Firefox()
    else:
        init_driver = webdriver.Ie()
    executor_url = init_driver.command_executor._url
    session_id = init_driver.session_id
    driver = ReuseChrome(command_executor=executor_url, session_id=session_id)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

driver=get_driver(browser_choice)


#句柄相关操作
handle=driver.current_window_handle#获取初始句柄
class myhandle():

    def __init__(self):
        pass

    # 切换到最新的句柄
    def switch_to_the_latest_handle(self):
        pass

    # 打开新窗口并切换到最新的句柄
    def open_window_and_switch_to_the_latest_handle(self):
        pass

    # 关闭当前窗口并切换到最新的句柄
    def close_current_window_and_switch_to_the_latest_handle(self):
        pass

    # 关闭当前窗口并返回初始句柄
    def close_current_window_and_swtich_back_to_initial_handle(self):
        pass






if __name__=="__main__":
    pass