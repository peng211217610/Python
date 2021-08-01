#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''公共函数'''

#引入相关包
import time,datetime
import os,sys,shutil,json
import xlrd,xlwt,xlutils
import win32con,win32gui,win32com.client,pyautogui
from random import randint,choice,uniform
from bs4 import BeautifulSoup
import pytest,pytest_html,pytest_parallel,pytest_rerunfailures
import subprocess
from subprocess import PIPE
import paramiko
import pymysql,cx_Oracle
import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
import hashlib
from docx import Document


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



'''鼠标与键盘相关操作'''



'''调用cmd窗口执行DOS命令'''
#执行cmd命令公共命令，获得输出(这是个字符串)
def exec_cmd(cmd):
    st=subprocess.Popen(cmd,stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True,encoding='gbk')
    output,err=st.communicate()
    # print(output)
    return output



'''paramiko库远程操作Linux'''
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


'''CSV文件操作'''
class CSV:

    def __init__(self):
        pass

    def get_all_values_from_csv(self,filename):
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

    def get_row_values_from_excel(self,filename,sheetname):
        xls = xlrd.open_workbook(filename, formatting_info=True)
        sheet = xls.sheet_by_name(sheetname)
        return [sheet.row_values(i) for i in range(1,sheet.nrows)]

    def get_all_values_from_excel(self,filename,sheetname):
        xls = xlrd.open_workbook(filename, formatting_info=False)
        sheet = xls.sheet_by_name(sheetname)
        total_rows = sheet.nrows
        return [sheet.row_values(i) for i in range(1, total_rows)]

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


'''操作数据库'''
class operate_db:
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
    def __init__(self):
        pass

    def operate_mysql(self,sql,mysql,fetchone_fetchall='fetchall'):
        db = pymysql.connect(host=mysql['host'], port=mysql['port'], user=mysql['user'],passwd=mysql['passwd'], database=mysql['database'],charset=mysql['charset'])  # 连接数据库
        cur = db.cursor()  # 获取游标
        # sql = '''show databases;'''
        # 执行sql语句
        global results
        results = []
        try:
            if type(sql)==str:
                sqllist=[sql]
            else:
                sqllist=sql
            for x in sqllist:
                cur.execute(x)
                if fetchone_fetchall == 'fetchone':
                    result = cur.fetchone()
                    results.append(result)
                elif fetchone_fetchall == 'fetchall':
                    result = cur.fetchall()
                    results.append(result)
                elif fetchone_fetchall == 'fetchmany':
                    result = cur.fetchmany()
                    results.append(result)
                else:
                    db.commit()
        except:
            db.rollback()
        finally:
            db.close()
        return results

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


'''上传'''
class WinUpLoadFile:

    def winUpLoadFile(self,file_path,title):
        time.sleep(3)
        #一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
        dialog = win32gui.FindWindow("#32770",title)
        #二级窗口
        comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        #三级窗口
        combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
        #四级窗口
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)
        #执行操作
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        #点击打开上传文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


'''读写文件'''
class File:

    def __init__(self):
        pass

    #把输出内容写入到文件
    def write_to_file(self,filename,mode,content):
        with open(filename,mode,encoding='utf-8') as f:
            f.write(content)

    #清空文件内容
    def clear_file_content(self,filename):
        self.write_to_file(r'%s' % filename,'w','')


'''转换'''
class Convert:

    def convert_str_to_list(self,str,sepreate_by):
        if sepreate_by != '':
            get_list=[one for one in str.splite(sepreate_by) if one != '']
        else:
            get_list = [one for one in str.splitlines() if one != '']
        return get_list


'''带颜色的字符串'''
class Color:
    '''
    #"\033[显示方式;前景色;背景色m要输出的内容\033[m"
    显示方式：
    0 默认
    1 高亮显示
    4 下划线
    5 闪烁
    7 反白显示
    8 不可见
    前景色             背景色           颜色
    ---------------------------------------
    30                40              黑色
    31                41              红色
    32                42              绿色
    33                43              黃色
    34                44              蓝色
    35                45              洋红
    36                46              青色
    37                47              白色
    '''
    def output_string_with_color(self,content,color=31):
        return "\033[%dm%s\033[m" % (color,content)



def find_out_all_value(eles,attribute=''):
    return [one.text.strip() if attribute == '' else one.get_attribute(attribute) for one in eles]


#获取Python所在路径
def get_python_dir():
    #Function.Common地址
    common_dir=os.path.dirname(os.path.abspath(__file__))
    function_dir=os.path.dirname(common_dir)
    #python地址
    return os.path.dirname(function_dir)
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
    # WinUpLoadFile().winUpLoadFile(r'D:\TDdownload\新建文件夹\53453453453.zip','打开')
    pass