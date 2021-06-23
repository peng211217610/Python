#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''课程已存在，添加失败'''

#引入包
import sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
import API_1_kecheng as ke
from random import randint
import sys

#添加课程
n = randint(0,999999)
ke.add_course('/api/mgr/sq_mgr/','PySchool_%06s' % n,'PySchool_%6s' % n,5)
lesson_count_pre = ke.list_course('/api/mgr/sq_mgr/')


re = ke.add_course('/api/mgr/sq_mgr/','PySchool_%06s' % n,'PySchool_%6s' % n,5)
lesson_count_af = ke.list_course('/api/mgr/sq_mgr/')

#print(re)
assert re['retcode'] == 2
assert re['reason'] == '同名课程存在'

if lesson_count_pre != lesson_count_af:
    print('API has issue!')
    sys.exit()

print('Success!')