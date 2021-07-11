#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''登陆成功'''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg
from selenium import webdriver


url,username,password = cfg.teachUserInfo


class login:
    className = 'login'
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def login(self):
        #设置driver为global变量，才可以使该方法执行完以后，driver不退出。
        global driver
        driver = webdriver.Chrome()
        driver.get(url)
        ele = driver.find_element_by_id('username')
        ele.clear()
        ele.send_keys(username)
        ele = driver.find_element_by_id('password')
        ele.clear()
        ele.send_keys(password)
        ele = driver.find_elements_by_css_selector("[class='btn btn-success']")
        print(ele)
        ele[0].click()


# t = login(url,username,password)
# t.login()
#
#






