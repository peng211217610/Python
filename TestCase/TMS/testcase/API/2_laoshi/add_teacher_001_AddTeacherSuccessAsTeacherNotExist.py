#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''添加老师成功'''

#引入包
import requests,json,sys
sys.path.append(r'D:\TDdownload\Document\Python\TMS')
import configure as cfg
from random import randint
import API_2_laoshi as ls


#列出老师数量
res = ls.list_teacher('/api/mgr/sq_mgr/')
teacher_number_pre = res['total']

#添加老师
username = 'chenqingyan_%6s' % randint(0,999999)
res = ls.add_teacher('/api/mgr/sq_mgr/',username)

assert res['retcode'] == 0
id = res['id']

#再次列出老师数量,断言只新增了一条记录
res = ls.list_teacher('/api/mgr/sq_mgr/')
teacher_number_af = res['total']

assert teacher_number_af == teacher_number_pre + 1

#判断新增记录在课程列表里
if ls.teacherInfo in res['retlist']:
    print('Success!')
else:
    print(ls.teacherInfo)
    print('记录添加内容与传入不符')

#检查数据库中新增了一条记录
import pymysql

db = pymysql.connect(host='localhost',port=3306,user='songqin',password='songqin',database='plesson',charset='UTF8')

#print(db)

cur = db.cursor()

sql = '''select * from plesson.sq_teacher order by user_id desc;'''

try:
    cur.execute(sql)
    db.commit()
    rec = cur.fetchone()
    print(rec)
except:
    db.rollback()


cur.close()
db.close()






