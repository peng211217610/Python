#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''删除老师成功'''

#引入包
import requests,json,sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
from random import randint
import API_2_laoshi as ls


#列出老师列表
te_pre = ls.list_teacher('/api/mgr/sq_mgr/')
#获取当前老师数量
te_account_pre = te_pre['total']

#新增一个老师
username = 'chenqingyan_%6s' % randint(0, 999999)
res = ls.add_teacher('/api/mgr/sq_mgr/',username)
assert res['retcode'] == 0  #确保添加老师成功，不成功就退出
te_id = res['id']
#列出当前老师列表
te_mid = ls.list_teacher('/api/mgr/sq_mgr/')
#获取此时老师数量
te_account_mid = te_mid['total']

if te_account_mid - te_account_pre != 1:
    print('add teacher failed!')

#删除刚才添加的老师
ls.delete_teacher('/api/mgr/sq_mgr/',te_id)
#列出此时的老师列表
te_af = ls.list_teacher('/api/mgr/sq_mgr/')

if te_af == te_pre:
    pass
else:
    print('delete teacher failed！')
    sys.exit(3)

print('Success!')














