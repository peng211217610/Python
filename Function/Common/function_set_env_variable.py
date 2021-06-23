#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''设置环境变量'''

#引入相关包
from Function.Common.function_common import  *


'''
Windows通过cmd命令修改系统环境变量，Linux修改profile文件修改
'''


class set_env_variable:

    def __init__(self):
        pass

    #通过环境变量名，获取环境变量值
    def get_env_variable_value(self,variable_name):
        output=exec_cmd('wmic ENVIRONMENT where name="%s" get UserName,VariableValue' % variable_name)
        path_list=[i for i in output.splitlines() if '<SYSTEM>' in i or '%s' % get_current_username_by_exec_cmd('net config workstation') in i]
        return path_list



for i in set_env_variable().get_env_variable_value('PATH'):
    output=i.strip().split(';')
    [print(i) for i in output]










if __name__=="__main__":
    # print(set_env_variable().get_env_variable_value('PATH'))
    pass