#!/usr/bin/python3
# -*- coding: utf-8 -*-
#备注
remark = r'''初始化webdriver，驱动放在：Tools'''


#引入相关包
from Function.Oppty.function_oppty_common import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Remote
from selenium.common.exceptions import InvalidArgumentException


class Driver:

    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            if browser == "Chrome":
                from selenium.webdriver.chrome.service import Service
                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches",['enable-automation'])#禁用浏览器正在被自动化程序控制的提示
                options.add_experimental_option("detach", True)#保持浏览器的打开状态
                service = Service(os.path.join(tool_dir,'chromedriver.exe'))
                cls.driver = webdriver.Chrome(options=options,service=service)
            elif browser == "Edge":
                from selenium.webdriver.edge.service import Service
                options = webdriver.EdgeOptions()
                options.add_experimental_option("excludeSwitches",['enable-automation'])#禁用浏览器正在被自动化程序控制的提示
                options.add_experimental_option("detach", True)#保持浏览器的打开状态
                service = Service(os.path.join(tool_dir,'msedgedriver.exe'))
                cls.driver = webdriver.Edge(options=options,service=service)
            else:
                cls.driver = webdriver.Ie()
            #驱动设置
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            # return cls.driver
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None





#选择浏览器并对浏览器做设置
def init_webdriver(brower):
    # global driver
    if brower == "Chrome":
        #引入相关库
        from selenium.webdriver.chrome.service import Service
        options = webdriver.ChromeOptions()
        # options.add_argument(r'--user-data-dir=C:\Users\peng2\AppData\Local\Google\Chrome\User Data')#加载用户数据
        # options.add_argument(r'--user-data-dir="C:\Users\peng2\AppData\Local\Google\Chrome\User Data2"')#加载用户数据
        # options.add_argument("--disable-popup-blocking")
        # options.add_argument("no-default-browser-check")
        # options.add_argument("no-sandbox")
        #最大化窗口
        options.add_argument("--start-maximized")
        # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # 连接到远程调试端口
        options.add_experimental_option("prefs",{"credentials_enable_service":False,"profile.password_manager_enabled":False,"download.default_directory":r"E:\TDdownload\下载"})#关闭保存密码提示框,#设置下载地址
        options.add_experimental_option("excludeSwitches",['enable-automation'])#禁用浏览器正在被自动化程序控制的提示
        #重新打开弹出窗口阻止程序
        # options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        #添加扩展
        # options.add_extension(extension_file_path)
        options.add_experimental_option("detach", True)#保持浏览器的打开状态
        service = Service(os.path.join(tool_dir,'chromedriver.exe'))
        driver = webdriver.Chrome(options=options,service=service)
    elif brower == "Edge":
        from selenium.webdriver.edge.service import Service
        # from webdriver_manager.microsoft import EdgeChromiumDriverManager
        # from selenium.webdriver.edge.options import Options
        options = webdriver.EdgeOptions()
        options.add_argument(r'--user-data-dir=C:\Users\peng2\AppData\Local\Microsoft\Edge\User Data2')#加载用户数据
        options.add_argument("--start-maximized")#最大化窗口
        options.add_experimental_option("prefs",{"credentials_enable_service":False,"profile.password_manager_enabled":False,"download.default_directory":r"E:\TDdownload\下载"})#关闭保存密码提示框,#设置下载地址
        options.add_experimental_option("excludeSwitches",['enable-automation'])#禁用浏览器正在被自动化程序控制的提示
        options.add_experimental_option("detach", True)  # 让浏览器脱离驱动控制，脚本结束后不关闭
        service = Service(os.path.join(tool_dir,'msedgedriver.exe'))
        driver = webdriver.Edge(options=options,service=service)
    elif brower == "Firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    #驱动设置
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver




# driver=init_webdriver(browser)





#句柄相关操作
class Handle:

    def __init__(self,driver):
        self.driver = driver
        #用window_handles[0]而不是current_window_handle是为了避免在打开多个窗口的时候才实例化Handle导致获取错误的main_handle
        self.main_handle = self.driver.window_handles[0]

    # 切换到最新的句柄
    def switch_to_the_latest_handle(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # 打开新窗口并切换到最新的句柄(废除，selenium4可以直接打开)
    def open_window_and_switch_to_the_latest_handle(self):
        self.driver.execute_script('window.open()')
        self.switch_to_the_latest_handle()

    # 把最新窗口设置为主窗口，并关闭其他窗口
    def set_latest_handle_to_main_handle(self):
        self.switch_to_the_latest_handle()
        self.main_handle = self.driver.current_window_handle
        self.close_all_and_switch_back_to_main_handle()

    # 关闭主窗口之外的所有窗口，并切会主窗口
    def close_all_and_switch_back_to_main_handle(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.main_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(self.main_handle)

    # 关闭当前操作窗口并切换到跳转之前的窗口
    def close_current_window_and_switch_back_to_former_handle(self):
        handles = self.driver.window_handles
        if len(handles) >= 2:
            self.driver.switch_to.window(handles[-1])
            self.driver.close()
            self.driver.switch_to.window(handles[-2])
        else:
            raise RuntimeError("当前窗口数量不足，无法执行关闭操作！")

    # 打开多个空白窗口
    def open_new_handle(self, count):
        for _ in range(count):
            self.driver.execute_script('window.open()')
            self.switch_to_the_latest_handle()


# main_handle=driver.current_window_handle#获取初始句柄
# handle = Handle()



#谷歌页面提示“您的连接不是私密连接”
def chrome_you_link_not_privite():
    driver.find_element_by_xpath('//button[contains(text(),"高级")]').click()
    driver.find_element_by_xpath('//a[@id="proceed-link"]').click()








if __name__=="__main__":
    pass