#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''老师已存在，添加老师失败'''

#引入包
import requests,json,sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
from random import randint
import API_2_laoshi as ls


#判断是否存在username为chenqingyan_000000的用户，存在就删除
res = ls.list_teacher('/api/mgr/sq_mgr/')
if res['retcode'] == 0:
    #获取usernameList
    usernameList = []
    for i in range(0,len(res['retlist'])):
        usernameList.append(res['retlist'][i]['username'])
    if 'chenqingyan_000000' in usernameList:
        for i in range(0,len(res['retlist'])):
            if res['retlist'][i]['username'] == 'chenqingyan_000000':
                id = res['retlist'][i]['id']
        ls.delete_teacher('/api/mgr/sq_mgr/',id)
else:
    print('调查询老师接口失败！')


#新增一个老师，username不填，使用默认值
res = ls.add_teacher('/api/mgr/sq_mgr/')

if res['retcode'] == 0:
    re_pre = ls.list_teacher('/api/mgr/sq_mgr/')
    #再添加一次相同名字的老师
    re_add = ls.add_teacher('/api/mgr/sq_mgr/')
    if re_add['retcode'] != 0:
        re_af = ls.list_teacher('/api/mgr/sq_mgr/')
    else:
        print('添加老师失败，请检查添加老师功能是否正常！')
        sys.exit()
else:
    print('添加老师失败，请检查添加老师功能是否正常！')
    sys.exit()


#检查结果
assert re_pre == re_af
assert re_add['retcode'] == 1


print('Success!')