#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''课程不存在，添加课程成功'''

#引入包
import os
import sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
import API_1_kecheng as ke
from random import randint

#添加课程
lesson_count_pre = ke.list_course('/api/mgr/sq_mgr/')['total']
n = randint(0,999999)
re = ke.add_course('/api/mgr/sq_mgr/','PySchool_%06s' % n,'PySchool_%06s' % n,5)
lesson_count_af = ke.list_course('/api/mgr/sq_mgr/')['total']


#检查
assert re['retcode'] == 0
if lesson_count_pre == lesson_count_af -1:
    pass
else:
    print('add course failed!')
    sys.exit()

if '{"id": %d, "name": "PySchool_%06s", "desc": "PySchool_%06s", "display_idx": 5}' % (re['id'],n,n):
    print('Success!')
else:
    print('Failed!')