#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''首页'''

# 引入包
from Function.Page.function_page_LoginPage import *


class HomePage(BasePage):

    ele = (By.ID,"xxx")

    def __init__(self,driver):
        super().__init__(driver)

    def click_lianjie(self):
        print('homepage的点击链接')

    def back_to_homepage(self):
        print('回到首页')
















if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
