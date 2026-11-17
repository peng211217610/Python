#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''免费软件提交页面'''

# 引入包
from Function.Page.function_page_BasePage import *

class FreeSubmit(BasePage):

    submit = (By.ID, "submit_btn")

    def __init__(self,driver):
        super().__init__(driver) #注意这里没有self



    def tijiao(self):
        print('用例里的调用')
        pass








































if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
