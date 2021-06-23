#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''公共函数'''

#引入相关包
import time,datetime
import xlrd,xlwt,xlutils

'''定义时间类'''
class myTime:

    def __init__(self):
        pass

    #将输入时间转换成年月
    def mymonth(self,output_format='%Y%m',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

    #将输入时间转换成年月日
    def mydate(self,output_format='%Y%m%d',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

    #获取当前时间前（后）X天
    def mybeforedate(self,output_format='%Y%m%d',before_or_after_days=-1):
        input_date=datetime.date.today()+datetime.timedelta(days=before_or_after_days)
        return str(input_date).replace('-','')

    #将输入时间转换成年月日时分秒
    def mytime(self,output_format='%Y%m%d%H%M%S',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

    #将输入时间转换为时间戳，单位为1代表秒级，1000为毫秒级，1000000为微秒级
    def mytimestamp(self,unit=1):
        return int(round(time.time()*unit))

def find_out_all_value(eles,att=''):
    return [one.get_attribute(att) if att != '' else one.text for one in eles]


#鼠标与键盘相关操作


#执行shell文件

'''调用cmd窗口执行DOS命令'''
#引入相关包
import subprocess
from subprocess import PIPE


#执行cmd命令公共命令，获得输出(这是个字符串)
def exec_cmd(cmd):
    st=subprocess.Popen(cmd,stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True,encoding='gbk')
    output,err=st.communicate()
    # print(output)
    return output



#获取当前计算机的登陆用户，用于修改环境变量
def get_current_username_by_exec_cmd(cmd):
    output=exec_cmd(cmd).splitlines()
    computer_name=output[1].replace(' ','|').split('|')[-1]
    user_full_name=output[2].replace(' ','|').split('|')[-1]
    #用户名只会取前5位
    return computer_name+'\\'+user_full_name[:5]


'''读取CSV文件'''
def get_all_values_from_csv(filename):
    with open(r'D:\TDdownload\%s.csv' % filename,'r',encoding='utf-8') as f:
        content = f.read()
        mycontentlist = content.splitlines()
        del mycontentlist[0]
        mycontentlist.reverse()
        return mycontentlist



'''Excel相关操作'''
class Excel():

    def __init__(self):
        pass

    def get_column_index_from_excel(self):
        pass

    def get_column_values_from_excel(self):
        pass

    def get_row_values_from_excel(self):
        pass
        # row_list=[sheet.row_values(i) for i in range(sheet.nrows)]
        # return row_list

    def get_all_values_from_excel(self,filename):
        xls = xlrd.open_workbook(r'D:\TDdownload\%s.xls' % filename, formatting_info=False)
        sheet = xls.sheet_by_name('Sheet1')
        total_rows = sheet.nrows
        return [sheet.row_values(i) for i in range(1, total_rows)]























if __name__=="__main__":
    # exec_cmd('dir')
    print(get_current_username_by_exec_cmd('net config workstation'))
    print(myTime().mymonth())
    print(myTime().mydate())
    print(myTime().mybeforedate())
    print(myTime().mytime())
    print(myTime().mytimestamp())
    pass