#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''打开电影天堂首页'''
import pytest
from Function.Project.function_dytt_login import *


#变量

# class Test_open_homepage:
#
#     def setup_model(self):
#         print('setup_model')
#
#     @classmethod
#     def setup_class(cls):
#         print('setup_class')
#
#     def setup_funciton(self):
#         print('setup_funciton')
#
#     def setup(self):
#         print('setup')
#
#
#     def test_funciton_1(self,open_browser):
#
#         a = 1
#
#         assert a==1
#
#     def test_function_2(self):
#         b=2
#         assert b==2
#
#     def teardown(self):
#         print('teardown')
#
#     def teardown_funciton(self):
#         print('teardown_function')
#
#     @classmethod
#     def teardwon_class(cls):
#         print('teardown_class')
#
#     def teardown_model(self):
#         print('teardown_model')


def test_open_url():
    open_url('http://www.baidu.com')
    open_url('https://www.csdn.net/')


def test_open_urt():
    handles=driver.window_handles
    print(handles)



def test_function_sss():
    title=driver.title
    print(title)



#引入相关包













if __name__=="__main__":
    pytest.main(['-s','test_open_homepage'])
    pass