#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''操作数据库'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from random import randint
import pymysql,cx_Oracle



class operate_db:
    className = 'operate_database'


    def operate_mysql(mysqlInfo, sqlList, sql):
        db = pymysql.connect(cfg.mysqlInfo)  # 连接数据库
        cur = db.cursor()  # 获取游标
        # sql = '''show databases;'''
        # 执行sql语句
        try:
            cur.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()


    def operate_oracle(oracleInfo,sqlList):
        conn = cx_Oracle.connect(oracleInfo)
        cur = conn.cursor()
        # print(sqlList)
        for one in sqlList:
            print(one)
            cur.execute(one)
        conn.commit()
        cur.close()
        conn.close()


if __name__=="__main__":
    #先获取sqlList的值
    operate_db().operate_oracle(cfg.oracleInfo,sqlList)



#详细说明
'''
备注：对于查询语句，可以使用
cur.fetchone()
cur.fetchmany()
cur.fetchall()
sql = """
    SELECT * FROM TABLE(NOLOCK) WHERE PARAMETER1 = %s AND PARAMETER2 = %s AND PARAMETER3 = %d
"""
#execute可以直接传参
cur.execute(sql, PARAMETER1, PARAMETER2, PARAMETER3)
'''