#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''公共函数'''

#引入相关包
import time,datetime
import os,sys,shutil,json
import xlrd,xlwt,xlutils
import socket,hashlib,base64,zipfile,glob
import win32con,win32com.client,win32gui,win32api,pyautogui
import pymouse,pykeyboard
from random import randint,choice,uniform
from bs4 import BeautifulSoup
import pytest,pytest_html,pytest_parallel,pytest_rerunfailures
import subprocess
from subprocess import PIPE
import paramiko
import pymysql,cx_Oracle,pymongo
import urllib3
# from requests.packages import urllib3
urllib3.disable_warnings()
import urllib.parse
import requests
from requests_toolbelt import MultipartEncoder
from PIL import ImageGrab
from docx import Document
from docx.shared import Cm,Inches,Pt
from docx.oxml.ns import qn
from docx.enum.section import WD_ORIENTATION
import pandas as pd
import collections
import base64


'''定义时间类'''
class myTime:

    def __init__(self):
        pass

    #将输入时间转换成年月
    def mymonth(self,output_format='%Y%m',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

    #将输入时间转换成年月日，返回string类型
    def mydate(self,output_format='%Y%m%d',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

    #获取当前时间前（后）X天
    def mybeforedate(self,output_format='%Y%m%d',before_or_after_days=-1):
        input_date=datetime.date.today()+datetime.timedelta(days=before_or_after_days)
        return str(input_date).replace('-','')

    #将输入时间转换成年月日时分秒，返回string类型
    def mytime(self,output_format='%Y%m%d%H%M%S',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

    #将输入时间转换为时间戳，单位为1代表秒级，1000为毫秒级，1000000为微秒级
    def mytimestamp(self,unit=1):
        return int(round(time.time()*unit))


'''键盘相关操作'''
class keyboard:

    def __init__(self):
        pass

    #ctrl+Q截图(用pillow代替，该功能暂时不用)
    def ctrl_and_Q(self):
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(81, 0, 0, 0)
        win32api.keybd_event(81, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    #按向下键
    def down(self,times):
        for _ in range(times):
            win32api.keybd_event(40,0,0,0)
            win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)


'''鼠标相关操作'''
class mouse:

    def __init__(self):
        pass

    #按下鼠标左键移动到特定位置放开
    def mouseDown_move_to_position_then_mouseUp(self,begin,after):
        pyautogui.mouseDown(x=begin[0], y=begin[1], button='left')
        pyautogui.mouseUp(x=2745, y=778, button='left', duration=1)


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


'''Word相关操作'''
class Word:

    def __init__(self):
        pass

    #添加附件
    def add_attachment(self,filename):
        # ctrl+End移动到word末尾
        win32api.keybd_event(17,0,0,0)
        win32api.keybd_event(35,0,0,0)
        win32api.keybd_event(35,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        # 输入回车
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        # crtl+N打开拆入对象窗口
        win32api.keybd_event(18,0,0,0)
        win32api.keybd_event(78,0,0,0)
        win32api.keybd_event(78,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(74,0,0,0)
        win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(74,0,0,0)
        win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(18,0,0,0)
        win32api.keybd_event(70,0,0,0)
        win32api.keybd_event(70,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(18,0,0,0)
        win32api.keybd_event(66,0,0,0)
        win32api.keybd_event(66,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
        # 上传附件
        WinUpLoadFile().winUpLoadFile(filename,'浏览')
        win32api.keybd_event(18,0,0,0)
        win32api.keybd_event(65,0,0,0)
        win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)


'''Excel相关操作'''
class Excel:

    def __init__(self):
        pass

    #对sheet进行初始化
    def init_sheet(self,filename,sheetname):
        xls=xlrd.open_workbook(filename,formatting_info=True)
        sheet=xls.sheet_by_name(sheetname)
        return sheet

    #获取行值
    def get_row_values_from_excel(self,filename,sheetname,include_headline='N'):
        sheet=self.init_sheet(filename,sheetname)
        begin_index = 0 if include_headline == 'Y' else 1
        return [sheet.row_values(i) for i in range(begin_index,sheet.nrows) if sheet.row_values(i) != []]

    #获取列值
    def get_col_values_from_excel(self,filename,sheetname):
        sheet = self.init_sheet(filename,sheetname)
        return [sheet.col_values(i) for i in range(sheet.ncols)]

    #获取第一行（标题），返回一个列表
    def get_headline_from_excel(self,filename,sheetname):
        sheet = self.init_sheet(filename,sheetname)
        return sheet.row_values(0)

    #获取两列组成元组，根据后者的值，匹配出前者（通常用来做列表key值）
    def get_two_item_to_tuple(self,filename,sheetname,first_item_index,second_item_index):
        sheet = self.init_sheet(filename,sheetname)
        col1 = sheet.col_values(first_item_index)
        col2 = sheet.col_values(second_item_index)
        return [(col1[i],col2[i]) for i in range(len(first_item_index))]

    #根据筛选条件获取列的值组成列表：结果列的名称，筛选列的名称，条件（如果为空，代表除第一行之外的全部）
    def get_col_values_by_condition(self,filename,sheetname,condition=('','','')):
        headline_list = self.get_headline_from_excel(filename,sheetname)
        sheet_list = self.get_row_values_from_excel(filename,sheetname)
        tg_list = []
        for i in sheet_list:
            if (condition[2] != '' and i[headline_list.index(condition[1])] in condition[2]) or condition[2]=='':
                tg_list.append(i[headline_list.index(condition[0])])
        return tg_list

    #读取Excel，获得字典列表
    def get_excel_dict_list(self,filename,sheetname,key_index='1',needed_line='all'):
        sheet_list = self.get_row_values_from_excel(filename,sheetname,include_headline='Y')
        headline_list = sheet_list[0]
        tg_item = headline_list if needed_line == 'all' else needed_line
        if needed_line == 'all':
            tg_list = sheet_list
        else:
            x_list = []
            for x in range(len(tg_item)):
                x_list.append(headline_list.index(tg_item[x]))
            tg_list = []
            for i in sheet_list:
                j_list = []
                for j in range(len(tg_item)):
                    j_list.append(i[x_list[j]])
                tg_list.append(j_list)
        tg_dict = collections.OrderedDict()
        for i in tg_list[1:]:
            tg_dict[i[int(key_index)]] = Convert().convert_two_list_to_dict(tg_item,i)
        return tg_dict

    #组合成以关键字为key的字典
    def get_dict(self,filename,sheetname,index_name,value_name='all',include_headline='N',fetch_zone='all'):
        sheet = self.init_sheet(filename,sheetname)
        tg_dict = {}
        index_index = sheet.row_values(0).index(index_name)
        sheet_values_list = [sheet.row_values(i) for i in range(sheet.nrows) if sheet.row_values(i)[index_index] != '']
        if include_headline == 'N':
            sheet_values_list.pop(0)
        for i in range(len(sheet_values_list)):
            if value_name == 'all':
                tg_value = sheet_values_list[i]
            else:
                tg_value = sheet_values_list[i][sheet.row_values(0).index(value_name)]
            tg_dict[sheet_values_list[i][index_index]] = tg_value
        return tg_dict


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

    def operate_mysql(self,sql,mysql,print_sql='Y',fetchone_fetchall='fetchall',default_cursor='tuple'):
        db = pymysql.connect(host=mysql['host'],port=mysql['port'],user=mysql['user'],passwd=mysql['passwd'],database=mysql['database'],charset=mysql['charset'])  # 连接数据库
        if default_cursor=='tuple':
            cur = db.cursor()  # 获取游标，select结果以元组方式返回
        else:
            cur = db.cursor(pymysql.cursors.DictCursor) #获取游标，select结果以字典方式返回
        # sql = '''show databases;'''
        # 执行sql语句
        # global results
        results = []
        try:
            if type(sql)==str:
                sqllist=[sql]
            else:
                sqllist=sql
            for x in sqllist:
                if print_sql=='Y':
                    print(x)
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
        except KeyError:
            db.rollback()
        finally:
            db.close()
        return results

    def operate_oracle(self,oracleInfo,sqlList):
        conn = cx_Oracle.connect(oracleInfo)
        cur = conn.cursor()
        # print(sqlList)
        for one in sqlList:
            print(one)
            cur.execute(one)
        conn.commit()
        cur.close()
        conn.close()

    def operate_mongodb(self,host,port,database_name,collection_name,insert_content):
        collection=pymongo.MongoClient(host,int(port))[database_name][collection_name]
        collection.insert_many(insert_content)


'''Windows和Linux互相传文件和文件夹'''
class Transfer_File:

    def __init__(self):
        pass

    def Window_to_Linux_File(self,remoteServer, window_path, linux_path):
        cmd = 'D:/TDdownload/Document/Python/tools/pscp.exe -pw {password} {window_path} {username}@{linux_ip}:{linux_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Window_to_Linux_Dir(self,remoteServer, window_path, linux_path):
        cmd = 'D:/TDdownload/Document/Python/tools/pscp.exe -pw {password} -r {window_path} {username}@{linux_ip}:{linux_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Linux_to_Window_File(self,remoteServer, linux_path, window_path):
        cmd = 'D:/TDdownload/Document/Python/tools/pscp.exe -pw {password} {username}@{linux_ip}:{linux_path} {window_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Linux_to_Window_Dir(self,remoteServer, linux_path, window_path):
        cmd = 'D:/TDdownload/Document/Python/tools/pscp.exe -pw {password} -r {username}@{linux_ip}:{linux_path} {window_path}'.format(password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)


'''上传'''
class WinUpLoadFile:

    def winUpLoadFile(self,file_path,title):
        time.sleep(4)
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

    #把输出内容写入到文件，默认换行
    def write_to_file(self,filename,mode,content,next_line='Y'):
        with open(filename,mode,encoding='utf-8') as f:
            if next_line=='Y':
                f.write(content+'\n')
            else:
                f.write(content)

    #写日志
    def write_to_log(self,filename,mode,content):
        with open(filename,mode,encoding='utf-8') as f:
            f.write('='*80+myTime().mytime()+'\n')
            f.write(content+'\n')

    #清空文件内容
    def clear_file_content(self,filename):
        self.write_to_file(r'%s' % filename,'w','')

    #读取文件的内容
    def read_file_return_content(self,filename,mode='r',print_content='N'):
        with open(filename,mode,encoding='utf-8') as f:
            content=f.read()
            if print_content=='Y':
                print(content)
        return content

    #创建文件夹
    def create_dir(self,dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    #移动文件
    def move_file(self,filename,target_file_path):
        self.create_dir(target_file_path)
        for data in glob.glob(filename):
            shutil.move(data,target_file_path)

    #获取文件地址
    def file_full_path(self,file_path,filename):
        return os.path.join(file_path,filename)


'''获取文件属性'''
class File_Attribute:

    def __init__(self):
        pass

    #sha256
    def CalcFileSha256(self,filename):
        with open(filename,'rb') as f:
            sha256obj = hashlib.sha256()
            sha256obj.update(f.read())
            hash_value = sha256obj.hexdigest()
            return hash_value

    #文件大小
    def CalcFileSize(self,filename):
        return os.stat(filename).st_size

    #md5
    def CalcFileMd5(self,filename):
        with open(filename,'rb') as f:
            myhash = hashlib.md5()
            while True:
                b = f.read(8096)
                if b:
                    myhash.update(b)
                else:
                    break
            return myhash.hexdigest()


'''转换'''
class Convert:

    #字符串转换成列表，保留空值
    def convert_str_to_list_with_blank(self,str,sepreate_by):
        if sepreate_by != '':
            get_list = [one.strip() for one in str.split(sepreate_by)]
        else:
            get_list = [one.strip() for one in str.splitlines()]
        return get_list

    #字符串转换成列表
    def convert_str_to_list(self,str,sepreate_by):
        if sepreate_by != '':
            get_list=[one.strip() for one in str.split(sepreate_by) if one != '']
        else:
            get_list = [one.strip() for one in str.splitlines() if one != '']
        return get_list

    #字符串转换成列表，去重并排序
    def convert_str_to_list_with_distinct_value_and_order(self,str,sepreate_by):
        return sorted(list(set(self.convert_str_to_list(str,sepreate_by))))

    #将列表转换成字符串，连接符作为入参，默认不要连接符
    def convert_list_to_string(self,input_list,combain_character=''):
        string=''
        for one in input_list:
            string+=(str(one)+combain_character)
        if combain_character=='':
            new_string=string
        else:
            new_string=string[:-len(combain_character)]
        return new_string

    #将读取的Excel列表值转换成字典，每行非空记录为字典值
    def convert_excel_list_to_dict(self,excel_list,key_item_index):
        mydict={}
        for one in excel_list:
            if one[key_item_index]!='':
                mydict[one[key_item_index]]=one
        return mydict

    #将读取的Excel列表值转换成完全的字典
    def convert_excel_list_to_full_dict(self,excel_list,key_item_index,drop_headline='Y',needed_column=''):
        mydict = {}
        headline = excel_list[0]
        tg_excel_list = excel_list if drop_headline == 'N' else excel_list[1:]
        for i in tg_excel_list:
            if i[key_item_index] != '':
                inner_dict = {}
                for j in range(len(headline)):
                    #把不需要的列去掉
                    if headline[j] in needed_column or needed_column=='':
                        inner_dict[headline[j]] = i[j]
                mydict[i[key_item_index]] = inner_dict
        return mydict

    #将多个换行字符串，转换成元组对的形式，要求两个列表个数相同
    def convert_multiple_str_to_tuple(self,str1,str2):
        str1list = self.convert_str_to_list(str1,'')
        str2list = self.convert_str_to_list(str2,'')
        mylist = []
        for i in range(len(str1list)):
            mylist.append((str1list[i],str2list[i]))
        return mylist

    #将加密的URL转换成字典
    def convert_encoded_url_to_dict(self,str):
        if r'%20' in str:
            stringlist = str.replace(r'%20',' ').split('&')
        else:
            stringlist = str.split('&')
        dict_string = {}
        for one in stringlist:
            dict_string[one.split('=')[0]] = one.split('=')[1]
        return dict_string

    #将字典转换成urlencoded url
    def convert_dict_to_encoded_url(self,dict):
        return urllib.parse.urlencode(dict)

    #将文件列表拼接成带双引号的字符串，上传文件可同时选择多个文件
    #例如：D:\TDdownload\下载\安全扫描\20210731\"osmanageService.war""OSTMSService.war"
    def convert_filelist_to_string_with_quota(self,filenamelist):
        string=''
        for one in filenamelist:
            new_one='"%s"' % one
            string+=new_one
        return string

    #将doc文档转换为docx
    def convert_file_format_doc_to_docx(self,filename):
        word=win32com.client.Dispatch('Word.Application')
        doc = word.Documents.Open(filename)
        doc.SaveAs(filename[:-4] + '.docx',12,False,"",True,"",False,False,False,False)
        doc.Close()
        word.Quit()
        return filename[:-4] + '.docx'

    #gav地址转换成链接地址
    def convert_gav_to_link(self,gav):
        gavlist = gav.split(':')
        tg_link = []
        for one in gavlist:
            if one != gavlist[-1] and '.' in one:
                tg_link.append(one.replace('.','/'))
            else:
                tg_link.append(one)
        return '/'.join(tg_link)

    #gav地址转换成g、a、v列表
    def convert_gav_to_gavlist(self,gav):
        pass

    #将数据库结果，元组类型转列表，results是元组类型的数据库结果，返回的是列表类型
    def convert_db_results_tuple_to_list(self,results):
        return [one[0] for one in results[0]]

    #去掉列表内的重复值
    def convert_list_to_distinct_value(self,mylist):
        return [one for one in mylist if one not in mylist]

    #将列表内的值全部转换成某种格式
    def convert_list_value_to_other_format(self,mylist,tgtype='str'):
        if tgtype=='int':
            return [int(one) for one in mylist]
        elif tgtype=='lower':
            return [one.lower() for one in mylist]
        elif tgtype=='upper':
            return [one.upper() for one in mylist]
        elif tgtype=='strip':
            return [one.strip() for one in mylist]
        else:
            return [str(one) for one in mylist]

    #将列表的名字转换成索引
    def convert_list_column_name_to_index(self,list,column_name):
        return list.index(column_name)

    #将字典转换成json格式化输出
    def convert_dict_to_format_json(self,mydict):
        return json.dumps(mydict,sort_keys=True,indent=2,ensure_ascii=False)

    #将两个列表转换成键值对，要保证两者的长度一致
    def convert_two_list_to_dict(self,key_list,value_list):
        tg_dict = {}
        for i in range(len(key_list)):
            tg_dict[key_list[i]] = value_list[i]
        return tg_dict


'''计算'''
class Calculate:

    def __init__(self):
        pass

    #字符串转换为md5值
    def get_md5_by_str(self,str):
        m = hashlib.md5()
        m.update(str.encode("utf8"))
        return m.hexdigest()


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

def find_out_difference_between_two_list(list1,list2,print_len='Y'):
    if print_len=='Y':
        print('两个列表的长度分别为：',end='')
        print(str(len(list1))+','+str(len(list2))+'\n',end='')
    print('list1存在，list2不存在的：')
    [print(i) for i in list1 if i not in list2]
    print('list2存在，list1不存在的：')
    [print(i) for i in list2 if i not in list1]


'''Get'''
class Get:

    def __init__(self):
        pass

    #根据输入的值，从元组对中匹配出另一个值
    def get_another_item_from_tuple_by_item(self,tuple_list,input_value):
        tg_item=None
        for i in tuple_list:
            if i[1]==input_value:
                tg_item=i[0]
                break
        return tg_item


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


'''截图'''
class snapshot:

    def __init__(self):
        pass

    def save_snapshot_by_pillow(self,area,filename):
        # 第一个参数 开始截图的x坐标
        # 第二个参数 开始截图的y坐标
        # 第三个参数 结束截图的x坐标
        # 第四个参数 结束截图的y坐标
        if area=='full':
            ImageGrab.grab().save(filename)
        else:
            ImageGrab.grab(area).save(filename)


'''压缩'''
class Compress:

    def __init__(self):
        pass

    def zip(self,packagename,filelist):
        z = zipfile.ZipFile(packagename,'w')
        [z.write(one) for one in filelist]
        z.close()


'''判断'''
class Judge:

    def __init__(self):
        pass

    #判断输入的字符串是否为json
    def is_json(self,input_str):
        try:
            json.loads(input_str)
        except ValueError:
            return False
        return True

    #查看是否存在重复项
    def is_contains_repeat(self,alist):
        blist = []
        for i in alist:
            if i in blist:
                print(i)
            else:
                blist.append(i)
        print(blist)


'''设置环境变量，Windows通过cmd命令修改系统环境变量，Linux修改profile文件修改'''
class set_env_variable:

    def __init__(self):
        pass

    #通过环境变量名，获取环境变量值
    def get_env_variable_value(self,variable_name):
        output=exec_cmd('wmic ENVIRONMENT where name="%s" get UserName,VariableValue' % variable_name)
        path_list=[i for i in output.splitlines() if '<SYSTEM>' in i or '%s' % get_current_username_by_exec_cmd('net config workstation') in i]
        return path_list


'''常用Linux命令'''
class Linux_Command:

    def __init__(self):
        pass

    #开启远程Oracle数据库
    def start_oracle(self):
        return '\n'.join(['#!/usr/bin/bash','su - oracle -c "lsnrctl start;sqlplus / as sysdba" << EOF','startup','EOF'])

    #关闭远程Oracle数据库
    def shutdown_oracle(self):
        return '\n'.join(['#!/usr/bin/bash','su - oracle -c "sqlplus / as sysdba" << EOF','shutdown immediate;','exit;','EOF','su - oracle -c "lsnrctl stop"'])


'''UI自动化'''
class UI:

    def __init__(self):
        pass

    #清除元素内容后重新输入
    def clear_and_send_keys(self,ele,content):
        ele.clear()
        ele.send_keys(content)























































if __name__=="__main__":
    # exec_cmd('dir')
    # print(get_current_username_by_exec_cmd('net config workstation'))
    # print(myTime().mymonth())
    # print(myTime().mydate())
    # print(myTime().mybeforedate())
    print(myTime().mytime())
    # print(myTime().mytimestamp())
    # Transfer_File().Window_to_Linux_File(remoteServer, r'D:\TDdownload\Document\Python\test\memory.py', '/home')
    # Transfer_File().Window_to_Linux_Dir(remoteServer,r'D:\TDdownload\Software', '/home')
    # Transfer_File().Linux_to_Window_File(remoteServer,'/home/aaa.txt', r'D:\TDdownload\Software')
    # Transfer_File().Linux_to_Window_Dir(remoteServer,'/home/phm', r'D:\TDdownload\Software')
    pass