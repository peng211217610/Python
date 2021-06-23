#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''




import pymysql
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='t1', charset='utf8')
cur = db.cursor()
sql = "select * from t1.userinfo where username='username' and pwd='pwd'"
cur.execute(sql)
result=cur.execute(sql) #执行sql语句，返回sql查询成功的记录数目
cur.close()
db.close()
















if __name__ == "__main__":
    pass