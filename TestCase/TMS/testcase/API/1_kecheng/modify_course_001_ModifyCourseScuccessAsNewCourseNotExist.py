#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''新课程名不存在，修改课程成功'''

#引入包
import os
import sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
import API_1_kecheng as ke
from random import randint


#添加课程并修改课程
n = randint(0,999999)
re = ke.add_course('/api/mgr/sq_mgr/','PySchool_%06s' % n,'PySchool_%06s' % n,5)
id = re['id']
m = randint(0,999999)
lesson_count_pre = ke.list_course('/api/mgr/sq_mgr/')['total']
rm = ke.modify_course('/api/mgr/sq_mgr/',id,'PySchool_%06s' % m,'PySchool_%06s' % m,randint(1,9))
lesson_count_af = ke.list_course('/api/mgr/sq_mgr/')['total']



#检查结果
assert rm['retcode'] == 0

if lesson_count_pre == lesson_count_af:
    pass
else:
    print('modify course function has issue!')
    sys.exit()

print('Success!')