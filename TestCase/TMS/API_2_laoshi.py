#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''1.添加老师.2.列出老师.3.修改老师.4.删除老师.'''

#引入包
import requests,json,sys
import configure as cfg
from random import randint
from API_1_kecheng import list_course


#先获取课程列表
def get_kechengList():
    res = list_course('/api/mgr/sq_mgr/')
    if res['retcode'] == 0:
        courseList = res['retlist']
        #print(courseList)
        if len(courseList) == 0:
            print('一门课程都没有')
            kechengList = []
        else:
            kechengList = []
            for one in courseList:
                #print(type(one))
                id = one['id']
                name = one['name']
                kecheng = {}
                kecheng["id"] = id
                kecheng["name"] = name
                #kecheng_json = json.dumps(kecheng)
                kecheng_json = kecheng
                if randint(1,10) == 1:
                    kechengList.append(kecheng_json)
    else:
        print('接口返回失败')
        sys.exit()
    return kechengList



#新增老师
def add_teacher(uri,username='chenqingyan_000000'):
    #username = 'chenqingyan_%6s' % randint(0,999999)
    course = get_kechengList()
    #print(course)
    display_idx = randint(1,9)
    data = {
        'action':'add_teacher',
        'data':'''{
            "username":"%s",
            "courses":%s,
            "realname":"chenqingyan",
            "desc":"chenqingyan",
            "display_idx":"%d",
            "password":"sq888"
        }''' % (username,json.dumps(course),display_idx)
    }
    r = requests.post('%s%s' % (cfg.host,uri),headers = cfg.headers,data = data)
    #列出老师接口，返回的retlist中courses参数跟传参data中的courses完全不一样。所以需要处理。
    if r.json()['retcode'] == 0:
        courseIdList = []
        for i in course:
            courseDict = {}
            courseDict['course_id']=i['id']
            courseIdList.append(courseDict)
        global teacherInfo
        teacherInfo = {
            "id":r.json()['id'],
            "realname":"chenqingyan",
            "desc":"chenqingyan",
            "display_idx":display_idx,
            "username":username,
            "courses":courseIdList,
        }
    return r.json()



#列出老师
def list_teacher(uri):
    params = {
        'action':'list_teacher',
        'pagenum':'1','pagesize':'200'
    }
    r = requests.get('%s%s' % (cfg.host,uri),params=params)
    return r.json()



#修改老师
def modify_teacher(uri,id):
    username = 'chenqingyan_%6s' % randint(0, 999999)
    course = get_kechengList()
    data = {
        'action':'modify_teacher',
        'id':id,
        'newdata':'''{
            "username":"%s",
            "courses":%s,
            "realname":"chenqingyan",
            "desc":"chenqingyan",
            "display_idx":"%d",
            "password":"sq888"
        }''' % (username,json.dumps(course),randint(1,9))
    }
    r = requests.put('%s%s' % (cfg.host, uri), headers=cfg.headers, data=data)
    return r.json()



#删除老师
def delete_teacher(uri,id):
    data = {
        'action':'delete_teacher',
        'id':id
    }
    r = requests.delete('%s%s' % (cfg.host,uri),data=data)
    return r.json()




if __name__ == '__main__':
    #username = 'chenqingyan_%6s' % randint(0, 999999)
    #add_teacher('/api/mgr/sq_mgr/',username)
    #list_teacher('/api/mgr/sq_mgr/')
    #modify_teacher('/api/mgr/sq_mgr/',241)
    #delete_teacher('/api/mgr/sq_mgr/',241)
    pass






































