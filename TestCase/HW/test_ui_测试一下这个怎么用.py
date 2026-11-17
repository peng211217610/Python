#!/usr/bin/python3
# -*- coding:utf-8 -*-
from Function.Page.function_page_HomePage import HomePage

remark = ''''''

# 引入包
from Function.Page.function_page_FreeSubmit import *

@pytest.fixture(scope='class')#scope放在class 级别，可以
def submit_page(home_page):
    # 回到首页，点击链接进入
    home_page.click_lianjie()#跳转到对应的目录
    return FreeSubmit(home_page.driver)








class Test1:

    def test_01_zhewanyi(self,submit_page):#不用填driver，因为login_page会自动网上找到driver
        submit_page.tijiao()








































if __name__ == "__main__":
    # whether_need_add_or_minus(2000)
    pass
