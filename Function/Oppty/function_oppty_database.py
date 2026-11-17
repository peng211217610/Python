#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''操作数据库'''

# 引入包
from Function.Config.common_variable import *

#env和dbtype组合确认代号(键值)
def get_mysql(env,dbtype):
    """
    :param dbtype: ostms、srcmanage、govdsit、govduat
    :param dbname: ostms、srcmanage_sit、govdsit、govduat
    """
    #下面这两行的函数没了，需要重新写
    # dict_mysql=get_dict().dict_mysql()
    # mysql_value=dict_mysql[get_dict().get_mysql_key_by_env_and_dbtype(env,dbtype)]
    mysql={
        "host":mysql_value[2],
        "port":int(mysql_value[3]),
        "user":mysql_value[4],
        "passwd":mysql_value[5],
        "database":mysql_value[6],
        "charset":mysql_value[7]
    }
    return mysql


#公共查询
def db_common_query(mysql,sql,print_sql='Y',print_result='Y',fetchone_fetchall='fetchall',default_cursor='tuple'):
    op_result=operate_db().operate_mysql(mysql,sql,print_sql,fetchone_fetchall,default_cursor)
    # print(sql)
    if print_result=='Y':
        print(op_result)
    return op_result


#注意：dbname是数据库名，不是登录用户名
def db_common_update(mysql,sql,print_sql='Y'):
    # print(mysql)
    # print(sql)
    operate_db().operate_mysql(mysql,sql,print_sql,'')


#公共操作
def db_common_operate(op_type,mysql,sql,print_sql='Y',print_result='Y',fetchone_fetchall='fetchall',default_cursor='tuple'):
    if op_type=='select':
        # print(sql)
        return db_common_query(mysql,sql,print_sql,print_result,fetchone_fetchall,default_cursor)
    else:
        # print(sql)
        operate_db().operate_mysql(mysql,sql,print_sql,'')
        return None


if __name__ == "__main__":
    pass
