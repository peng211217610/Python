#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''公共变量'''

#引入相关包
from Config.general_variable import *
from Function.Common.function_common import *


#浏览器选择(Chrome、Firefox、Ie)
browser_choice='Chrome'

#谷歌浏览器可执行文件所在路径
chrome_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'

input_str='aaa'

#--------------------------------------------------------获取配置
#获取用户全名


#匹配出账号密码
up_list_group=Excel()
#从excel获取配置
# username_passwd_list_group=get_all_values_from_excel(r'xxx')

class get_dict:

    def dict_mysql(self):
        pass

    def get_mysql_key_by_env_and_dbtype(self,env,dbtype):
        pass

#--------------------------------------------------------字典变量
class Dict_variable:

    def __init__(self):
        pass
    #(adb按键)
    def dict_adb_keycode(self):
        dict_adb_keycode = {
            #Home键
            "home":"3",
            #返回键
            "back": "4",
            #电话拨号键
            "dail": "5",
            #音量加键
            "vol_puls": "24",
            #音量减键
            "vol_minus": "25",
            #电源键
            "power": "26",
            #照相机启动键
            "camera_on": "27",
            #多媒体下一曲键
            "media_next": "87",
            #多媒体上一曲键
            "media_previous": "3",
            #音量静音键
            "vol_off": "91",
        }
        return dict_adb_keycode





















if __name__=="__main__":
    pass