#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''登陆页面'''

# 引入包
from Function.Page.function_page_BasePage import *

class LoginPage(BasePage):

    ele = (By.ID,"xxx")

    def __init__(self,driver):
        super().__init__(driver)


    def login(self,username,password):
        print('登陆')



























if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
