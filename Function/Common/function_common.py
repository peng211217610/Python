#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''公共函数'''

#引入相关包
import time,datetime
import xlrd,xlwt,xlutils
import os,sys,time,shutil,json
import pymysql,cx_Oracle
from random import randint,choice,uniform
import pytest,pytest_html,pytest_parallel,pytest_rerunfailures

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



#鼠标与键盘相关操作


#执行shell文件
'''调用cmd窗口执行DOS命令'''
#引入相关包
import subprocess
from subprocess import PIPE
import paramiko

#执行cmd命令公共命令，获得输出(这是个字符串)
def exec_cmd(cmd):
    st=subprocess.Popen(cmd,stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True,encoding='gbk')
    output,err=st.communicate()
    # print(output)
    return output



'''paramiko库远程操作Linux'''
#操作Linux
def paramiko_operate_linux(remoteServer,cmd):
    ssh = paramiko.SSHClient()
    # 调用方法，表示没有存储远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname,port,username,password = remoteServer
    ssh.connect(hostname,port,username,password)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    print(stdout.read())
    ssh.close()




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

    def get_all_values_from_excel(self,filename,sheetname):
        xls = xlrd.open_workbook(filename, formatting_info=False)
        sheet = xls.sheet_by_name(sheetname)
        total_rows = sheet.nrows
        return [sheet.row_values(i) for i in range(1, total_rows)]

    # 读取excel中的内容
    def read_excel(self):
        wb = xlrd.open_workbook(r'D:\TDdownload\WEO_Data (4).xls')
        sheet = wb.sheet_by_name('WEO_Data (4)')
        cols0 = sheet.col_values(1)
        cols1 = sheet.col_values(8)
        conList = []

        with open(r'D:\TDdownload\Document\Python\SQLFile\execute.sql', 'w+', encoding='utf8') as f:
            for i in range(len(cols0)):
                # p = int(cols1[i])
                q = cols1[i]
                print(q)
                f.write("update gdp set population_rank_2017='%s' where itemno='%s'\n" % (q, cols0[i]))
                # conList.append('(%s,%s),' % (cols0[i],cols1[i]))
            f.flush()
            f.seek(0)
            sqlList = f.read().splitlines()



def find_out_all_value(eles,att=''):
    return [one.get_attribute(att) if att != '' else one.text for one in eles]


#获取Python所在路径
def get_python_dir():
    #Function.Common地址
    common_dir=os.path.dirname(os.path.abspath(__file__))
    function_dir=os.path.dirname(common_dir)
    #python地址
    return os.path.dirname(function_dir)



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
'''操作数据库'''
class operate_db:

    def operate_mysql(mysqlInfo, sqlList, sql):
        db = pymysql.connect(mysqlInfo)  # 连接数据库
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


'''Windows和Linux互相传文件和文件夹'''
class Transfer_File:

    def Window_to_Linux_File(remoteServer, window_path, linux_path):
        cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} {window_path} {username}@{linux_ip}:{linux_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Window_to_Linux_Dir(remoteServer, window_path, linux_path):
        cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} -r {window_path} {username}@{linux_ip}:{linux_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Linux_to_Window_File(remoteServer, linux_path, window_path):
        cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} {username}@{linux_ip}:{linux_path} {window_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Linux_to_Window_Dir(remoteServer, linux_path, window_path):
        cmd = 'D:/TDdownload/Document/Python/pscp.exe -pw {password} -r {username}@{linux_ip}:{linux_path} {window_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)



'''批量启动软件'''
def start_exe_in_batches(exeList):
    exe = exeList.splitlines()[1:]
    for one in exe:
        os.startfile(one)
        time.sleep(1)
#要打开的程序列表
exeList = r'''
C:\Myprograms\J-计算机\UltraEdit\uedit64.exe
'''
# start_exe_in_batches(exeList)



'''
移动到图片上，点击鼠标右键，输入键盘字母v，定位到窗口，修改文件名，点击保存
'''
def right_click_and_save_picture_to():
    pass


















if __name__=="__main__":
    # exec_cmd('dir')
    print(get_current_username_by_exec_cmd('net config workstation'))
    print(myTime().mymonth())
    print(myTime().mydate())
    print(myTime().mybeforedate())
    print(myTime().mytime())
    print(myTime().mytimestamp())
    # Transfer_File().Window_to_Linux_File(remoteServer, r'D:\TDdownload\Document\Python\test\memory.py', '/home')
    # Transfer_File().Window_to_Linux_Dir(remoteServer,r'D:\TDdownload\Software', '/home')
    # Transfer_File().Linux_to_Window_File(remoteServer,'/home/aaa.txt', r'D:\TDdownload\Software')
    # Transfer_File().Linux_to_Window_Dir(remoteServer,'/home/phm', r'D:\TDdownload\Software')
    pass