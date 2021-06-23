#!/usr/bin/python3
# -*- coding:utf-8 -*-

TestCaseDesc = '''课程相关的函数'''

#引入包
import sys
import configure as cfg
import requests
import json
from random import randint
n = randint(0,999999)




#列出课程
def list_course(uri):
    params = {
        'action':'list_course',
        'pagenum':1,
        'pagesize':100
    }
    r = requests.get('%s%s' % (cfg.host,uri),params=params)
    return r.json()

#list_course('/api/mgr/sq_mgr/')



#添加课程
def add_course(uri,name,desc,display_idx):
    data = {
        'action':'add_course',
        'data':'''{
            "name":"%s",
            "desc":"%s",
            "display_idx":"%d"
        }''' % (name,desc,display_idx)
    }
    r = requests.post('%s%s' % (cfg.host,uri),data=data)
    return r.json()

#add_course('/api/mgr/sq_mgr/','PySchool_%06s' % n,'PySchool_%06s' % n,5)




#修改课程
def modify_course(uri,id,name,desc,display_idx):
    data = {
        'action':'modify_course',
        'id':id,
        'newdata':'''{
            "id":"%d",
            "name":"%s",
            "desc":"%s",
            "display_idx":"%d",
            "$$hashKey":"object:24",
            "editing":true
        }''' % (id,name,desc,display_idx)
    }
    r = requests.put('%s%s' % (cfg.host,uri),data=data)
    return r.json()

#print(modify_course('/api/mgr/sq_mgr/',1041,'PySchool_162322','PySchool_162322',5))





#删除课程
def delete_course(uri,id,):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "action":"delete_course",
        "id":id
    }
    r = requests.delete('%s%s' % (cfg.host,uri),headers = headers,data = data)
    return r.json()

#print(delete_course('/api/mgr/sq_mgr/',1041))




