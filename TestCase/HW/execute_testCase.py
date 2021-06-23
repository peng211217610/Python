#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''执行测试用例'''

#变量


#引入相关包
import pytest



pytest.main(['-s','./testCase','--html=./report/report.html'])
# pytest.main(['-q','./testCase','--tb=line'])







if __name__=="__main__":
    pass