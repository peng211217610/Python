#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''删除一门存在的课程成功'''


#引入所需的包
import sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
import API_1_kecheng as ke
from random import randint

'''
思路：
列出开始的课程
添加课程
删除该添加的课程
列出此时的课程，与开始时比对，需完全一致
'''
lesson_pre = ke.list_course('/api/mgr/sq_mgr/')
n = randint(0,999999)
re = ke.add_course('/api/mgr/sq_mgr/','PySchool_%06s' % n,'PySchool_%06s' % n,randint(0,9))
id = re['id']
assert re['retcode'] == 0
re = ke.delete_course('/api/mgr/sq_mgr/',id)
assert re['retcode'] == 0
lesson_af = ke.list_course('/api/mgr/sq_mgr/')

#检查
if lesson_pre == lesson_af:
    pass
else:
    print('delete course has issue!')
    sys.exit()

print('Success!')