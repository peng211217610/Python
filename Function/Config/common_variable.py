#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''基础配置&公共变量'''

#引入相关包
from Function.Common.function_common import *
from Function.Config.special_variable import *

#浏览器选择(Chrome、Firefox、Ie、Edge)
browser= 'Chrome'

#JS操作滚动条位置
up="document.documentElement.scrollTop=0"
middle="document.documentElement.scrollTop=1500"
down="document.documentElement.scrollTop=10000"
# up="window.scrollTo(0,0)"
# down="window.scrollTo(0,document.body.scrollHeight)"
left="var q=document.documentElement.scrollLeft=0"
right="var q=document.documentElement.scrollLeft=10000"


input_str='aaa'
huanhang='\n'
#Linux远程主机登陆地址
#remoteServer = ('192.168.145.128',22,'root','huawei')
#remoteServer = ('192.168.145.129',22,'root','Winovs12')
remoteServer = ('192.168.145.130',22,'root','Winovs12')

#Oracle连接地址
oracleInfo = 'phm/Winovs12@192.168.145.130:1521/orcl'

#MongoDB连接地址
# mongodb_url='mongodb://phm:Winovs12@192.168.145.130:27017(这是错的)'

#字符变量
greece="αβγδεζηθικλμνξοπρστυφχψω"
fangxiang="←↑→↓↖↙↗↘↕"

#划线
line1="="*50
line2="="*100
line3="="*150
line4="="*200
line5="="*250

#时间戳
now_time=t.mytimestamp()#int类型，默认精确到秒
mytimestamp=str(now_time)#转换成str型
mydate=str(t.mydate())#年月日
mytime=str(t.mytime())#年月日时分秒
myformattime=str(t.mytime(output_format='%Y-%m-%d %H:%M:%S'))#格式化年-月-日 时:分:秒
myhour=mytime[8:10]#字符串
myhms=mytime[8:14]#字符串，时分秒
myweek=t.get_weekday()#今天星期几


#--------------------------------------------------------接口自动化
userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# contentType='application/x-www-form-urlencoded'
origin='https://sz.lianjia.com/'
referer='https://sz.lianjia.com/'



#--------------------------------------------------------程序路径
yingxiongsha=r''










#--------------------------------------------------------获取配置
#匹配账号密码
up_list_group=Excel().get_row_values_from_excel(os.path.join(excel_dir,'000_我的配置.xls'),'账号密码')


















if __name__=="__main__":
    print(mytime)
    pass