#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''操作数据库'''

# 引入包
from Config.common_variable import *
from Function.Common.function_common import *

def get_mysql(env,dbtype,dbname):
    '''
    :param dbtype: ostms、srcmanage、govdsit、govduat
    :param dbname: ostms、srcmanage_sit、govdsit、govduat
    '''
    dict_mysql=get_dict().dict_mysql()
    mysql_value=dict_mysql[get_dict().get_mysql_key_by_env_and_dbtype(env,dbtype)]
    mysql={
        "host":mysql_value[2],
        "port":int(mysql_value[3]),
        "user":mysql_value[4],
        "passwd":mysql_value[5],
        "database":dbname,
        "charset":mysql_value[6]
    }
    return mysql

#通用查询
def db_common_query(env,dbtype,dbname,sql):
    mysql=get_mysql(env,dbtype,dbname)
    op_result=operate_db().operate_mysql(sql,mysql)
    print(op_result)
    return op_result

#注意：dbname是数据库名，不是登录用户名
def db_common_update(env,dbtype,dbname,sql):
    mysql = get_mysql(env,dbtype,dbname)
    operate_db().operate_mysql(sql,mysql,'')


if __name__ == "__main__":
    pass
