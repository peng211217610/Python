#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''cmd修改环境变量'''

#引入相关包



'''
使用 wmic 命令修改环境变量是永久性的，而使用 set 命令修改环境变量是只针对当前命令行环境的临时修改。
'''



#临时修改环境变量（仅对当前窗口生效）
'''
所有环境变量
set

查看某个环境变量
set Java_Home

修改环境变量
set var_name=var_value

修改为空
set var_name=

添加环境变量的值
set PATH=%PATH%;d:\\xxx
'''




#永久修改当前用户环境变量
'''
获取 PATH 环境变量的 用户 和 变量值
wmic ENVIRONMENT where name="PATH" get UserName,VariableValue


修改 OS 环境变量值为 Windows_NT，这会覆盖掉原有的变量值
wmic ENVIRONMENT where name="os" set VariableValue="Windows_NT"

修改 PATH 环境变量值，新增路径 T:\myScripts
wmic ENVIRONMENT where "name='PATH' and username='<system>'" set VariableValue="%PATH%;T:\myScripts"

新增用户变量
wmic ENVIRONMENT create name="Testuser",username="%username%",VariableValue="D:\\test03"


新增系统环境变量 myTemp，值为 %OS%%SystemDrive% 
wmic ENVIRONMENT create name="myTemp",username="<system>",VariableValue="%OS%%SystemDrive%"

删除 myTemp 环境变量 
wmic ENVIRONMENT where "name='myTemp'" delete



【注意事项】
        1、 where 关键字后跟的参数必须是一个连续的字符串，如果参数字符串含有空格需要用英文双引号 " 将参数括起来；若字符串中有多个限定词，比如既有 name 又有 username，则需要使用 and 关键字来连接这些限定词。
        2、在读取环境变量值时不需要管理员权限，但在创建、写入环境变量值时必须具备管理员权限。






'''
















if __name__=="__main__":
    pass