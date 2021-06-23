#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''修改老师成功'''

#引入包
import requests,json,sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
from random import randint
import API_2_laoshi as ls


#新增一个老师
username = 'chenqingyan_%6s' % randint(0, 999999)
res = ls.add_teacher('/api/mgr/sq_mgr/',username)
assert res['retcode'] == 0

#获取新增老师id
id = res['id']

#列出老师，看这个老师的信息
re_te = ls.list_teacher('/api/mgr/sq_mgr/')
for i in re_te['retlist']:
    if i['id'] == id:
        pass
        #print(i)

#修改该id的老师
re_md = ls.modify_teacher('/api/mgr/sq_mgr/',id)
assert re_md['retcode'] == 0

#再次列出老师，看这个老师的信息
re_te_af = ls.list_teacher('/api/mgr/sq_mgr/')
for i in re_te_af['retlist']:
    if i['id'] == id:
        pass
        #print(i)

print('Success!')