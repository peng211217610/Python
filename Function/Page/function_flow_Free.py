#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''流程类'''

# 引入包
from Function.Page.function_page_FreeSubmit import *


class Free:

    def __init__(self,driver):
        self.driver = driver
        # 如果需要在当前页面调用其他页面的方法，直接在这里实例化，下面的方法就能直接用self.submit_page.submit()执行
        self.submit_page = FreeSubmit(driver)
        self.audit_page = AuditPage(driver)


    def xxxxxxxxxxxxxxxxxx(self):
        #这里写我对每个页面做什么操作
        pass


































if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
