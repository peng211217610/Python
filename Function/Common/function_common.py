#!/usr/bin/python3
# -*- coding: utf-8 -*-
#备注
remark = '''公共函数'''

#引入相关包
from Function.Config.basic_variable import *
from types import SimpleNamespace
import time,datetime,calendar
import xlrd,xlwt,xlutils
from pathlib import Path
import string
import markdown
import socket,hashlib,base64,zipfile,glob
import win32con,win32com.client,win32gui,win32api,pyautogui,pywinauto
pyautogui.FAILSAFE = True#防止程序失控，鼠标移动到屏幕外
import pyperclip#跨平台剪贴板操作
#import pymouse#pykeyboard没安装，用其他代替吧
#============================================================键盘和鼠标
from pynput.keyboard import Controller as KeyboardController
keyboard = KeyboardController()
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController
mouse = MouseController()
#============================================================键盘和鼠标结束
from random import randint,choice,uniform,random
from decimal import Decimal
#bs4有问题了，引起exit code -1073741818 (0xC0000006)
from bs4 import BeautifulSoup
import pytest
import subprocess
from subprocess import PIPE
import paramiko
import pymysql,pymongo#cx_Oracle没安装
import urllib3
# from requests.packages import urllib3
urllib3.disable_warnings()
import urllib.parse
import requests
from requests_toolbelt import MultipartEncoder
#PIL库的名字是pillow，用于图片相关处理
from PIL import Image,ImageGrab
#有问题了，引起exit code -1073741818 (0xC0000006)更新库也不行
# from docx import Document
# from docx.shared import Cm,Inches,Pt
# from docx.oxml.ns import qn
# from docx.enum.section import WD_ORIENTATION
import csv
import tablib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import mplfinance as mpf
import collections
import base64
from functools import wraps
import execjs
import statistics
from threading import Thread
#忽略产生的警告
# import warnings
# warnings.simplefilter('ignore', category=UserWarning)
import sqlite3
import logging
#mitmproxy没安装
import zipfile #解压zip包
import ctypes
#生成虚拟姓名、手机号、身份证号
from faker import Faker




#pandas设置
# 加了这一行那表格的一行就不会分段出现了
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置列名对齐
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)


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

    #获取当前时间的时分秒，转换成str类型
    def myhms(self):
        return  self.mytime()[8:14]

    #将输入时间转换为时间戳，单位为1代表秒级，1000为毫秒级，1000000为微秒级
    def mytimestamp(self,unit=1):
        return int(round(time.time()*unit))

    #将输入的年月日时分秒转换成时间戳
    def get_timestamp_by_format_date(self,date='20240815000000',unit=1,date_format='%Y-%m-%d %H:%M:%S'):
        """
        :param date: 要转换的日期，如：20240815000000
        :param date_format: 上述date的格式，如：%Y%m%d%H%M%S
        :param unit:1为秒级，1000是毫秒
        :return:
        """
        return int(time.mktime(time.strptime(date,date_format))*unit)

    #输入时间串，转换成有格式的时间
    def convert_timestring_to_format_time(self,time_str='20240815000000'):
        year=time_str[:4]
        month=time_str[4:6]
        date=time_str[6:8]
        hour=time_str[8:10]
        minutes=time_str[10:12]
        seconds=time_str[12:14]
        return '%s-%s-%s %s:%s:%s' % (year,month,date,hour,minutes,seconds)

    #将时间戳转换成东八区时间串。传入的timestamp是以秒为单位的int类型
    def convert_timestamp_to_timestring(self,timestamp,unit=1,fmt='%Y-%m-%d %H:%M:%S'):
        #默认是秒级的时间戳
        timestamp=int(timestamp/unit)
        # 转换为UTC时间
        utc_time = datetime.datetime.fromtimestamp(timestamp, datetime.UTC)
        # 转换为东八区时间
        from zoneinfo import ZoneInfo
        beijing_time = utc_time.astimezone(ZoneInfo('Asia/Shanghai'))
        # 格式化为字符串
        return beijing_time.strftime(fmt)

    #获取今天是星期几
    @staticmethod
    def get_weekday():
        return datetime.datetime.now().weekday()

    #判断是否为闰年
    @staticmethod
    def is_runnian(year=None):
        return calendar.isleap(int(year))

    #判断两个时间是否相隔足够长的时间
    #日期格式是年-月-日 时：分：秒
    def compare_two_time_long_enough(self,before,after,how_long=60):
        fmt = "%Y-%m-%d %H:%M:%S"
        t1 = datetime.datetime.strptime(before, fmt)
        t2 = datetime.datetime.strptime(after, fmt)
        delta = t2 - t1
        return delta.total_seconds() >= how_long

    #补齐时间，例如‘0940’，补齐后是“09:40:00”
    def fullfill_the_time_string(self,input_time_str='0940'):
        if ':' in input_time_str:
            input_time_str=input_time_str
            if input_time_str.endswith(":"):
                input_time_str+='00'
        else:
            if len(input_time_str)==4:
                input_time_str+='00'
            input_time_str=input_time_str[:2]+':'+input_time_str[2:4]+':'+input_time_str[4:6]
        return input_time_str



'''键盘相关操作'''
class Keyboard:

    def __init__(self):
        self.f = File()
        json_config = os.path.join(file_dir,'JSON','配置_键盘键码.json')
        self.mydict=self.f.get_mydict_from_json_file(json_config)

    #基础函数，按下按钮
    def basic_down(self,keynumber):
        win32api.keybd_event(keynumber,0,0,0)

    #基础函数，松开按键
    def basic_up(self,keynumber):
        win32api.keybd_event(keynumber,0,win32con.KEYEVENTF_KEYUP,0)

    #按下单个字母
    '''常用键：Enter，Down Arrow，Left Arrow，Right Arrow，Up Arrow，Control，Backspace'''
    def press_single(self,keyboard):
        keynumber=self.mydict[keyboard]
        self.basic_down(keynumber)
        self.basic_up(keynumber)

    def enter(self):
        self.press_single('Enter')

    # #按键事件
    # def event(self,keynumber=None):
    #     win32api.keybd_event(keynumber,0,0,0)
    #     win32api.keybd_event(keynumber,0,win32con.KEYEVENTF_KEYUP,0)

    def press_double(self,keylist=None):
        #根据keylist获取键码
        if not keylist:
            print('press_double参数请输入列表')
        keynumber_list=[self.mydict[i] for i in keylist]
        #先按下多个键
        for i in keynumber_list:
            self.basic_down(i)
        #再依次松开
        for i in keynumber_list[::-1]:
            self.basic_up(i)

    #ctrl+Q截图(用pillow代替，该功能暂时不用)
    def ctrl_and_Q(self):
        self.press_double(['Control','Q'])

    #按向下键
    def down(self,times=1):
        for _ in range(times):
            self.press_single('Down Arrow')

    #打开桌面搜索框
    def open_search_box(self):
        self.press_double(keylist=['win','S'])

    #通过粘贴的方式往文本框输入内容
    def input_value_by_ctrl_v(self,input_str):
        pyperclip.copy(input_str)
        #然后按下Ctrl+v
        self.press_double(keylist=['Control','V'])




'''鼠标相关操作'''
class Mouse:

    def __init__(self):
        pass

    #按下鼠标左键移动到特定位置放开
    def mouseDown_move_to_position_then_mouseUp(self,begin,after):
        pyautogui.mouseDown(x=begin[0], y=begin[1], button='left')
        pyautogui.mouseUp(x=after[0], y=after[1], button='left', duration=1)

    #鼠标指针移动到某个位置
    def move_to_a_position(self,coords=None,duration=1):
        x,y=coords
        pyautogui.moveTo(x, y,duration)

    #鼠标点击某个位置
    def click_at_a_position(self,coords=None):
        #默认点击左键，button参数默认为left，右键的用不上暂时不写
        pywinauto.mouse.click(coords=coords)

    #鼠标滚动滚轮
    def mouse_scroll(self,dwData):
        #dwData是向上或向下滚动的幅度。正值往上滚，负值往下滚
        win32api.mouse_event(0,0,dwData,win32con.MOUSEEVENTF_HWHEEL)






'''电脑屏幕相关'''
class Screen:

    def __init__(self):
        pass

    #获取当前电脑的屏幕分辨率，返回值是int类型
    def get_screen_definition(self):
        screen_width, screen_height = pyautogui.size()
        return screen_width,screen_height

    #获取屏幕中心点的坐标
    def get_center_coordinate(self):
        width,height=self.get_screen_definition()
        half_width=int(width/2)
        half_height=int(height/2)
        return half_width,half_height

    #将客户端居中并设置1/4大小
    def get_move_window_position(self):
        half_width,half_height=self.get_center_coordinate()
        half_half_width=int(half_width/2)
        half_half_height=int(half_height/2)
        return half_half_width,half_half_height,half_width,half_height



'''cmd窗口命令'''
class Cmd:

    def __init__(self):
        pass

    #使用subprocess命令执行cmd命令
    #执行这个命令不会打开cmd窗口，只会输出内容
    def exec_cmd_by_subprocess(self,cmd_list):
        #将命令列表转换成命令字符串
        cmd_command=' && '.join(cmd_list)
        st=subprocess.Popen(cmd_command,stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True,encoding='utf-8')
        output,err=st.communicate()
        return output

    #打开cmd窗口执行cmd命令，默认窗口不关闭
    def exec_cmd_in_cmd_window(self,cmd_list,close_window='N'):
        cmd_command=' && '.join(cmd_list)
        k.open_search_box()
        time.sleep(1)
        k.input_value_by_ctrl_v('命令提示符')
        time.sleep(1)
        k.enter()
        time.sleep(1)
        k.input_value_by_ctrl_v(cmd_command)
        k.enter()
        #如果不用关闭窗口，则手动操作，如果关闭窗口，则获取命令的输出内容
        if close_window=='N':
            return None
        else:
            #获取窗口句柄(不要用这个方法，获取edit窗口失败，想要获取输出用subprocess)
            hwnd=win32gui.FindWindow('ConsoleWindowClass','命令提示符')
            #pywinauto比win32更适合获取输出
            app=pywinauto.Application(backend='win32').connect(handle=hwnd)
            main_window=app.window()
            main_window.print_control_identifiers()
            #找到编辑框
            edit_window=main_window.child_window(class_name="Edit")
            output = edit_window.get_value()
            # 关闭窗口
            main_window.close()
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
    output=exec_cmd_by_subprocess(cmd).splitlines()
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

    #返回的reader是个迭代器，newline=''代表不会每行新增一个空行
    def get_csv_iterator(self,filename):
        with open(filename,'r',newline='',encoding='utf-8') as f:
            reader = csv.reader(f)
        return reader

    #将数据写入文件，data是个列表，列表中嵌套小列表
    def write_to_file(self,filename,data):
        with open(filename,'w',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)


'''Word相关操作'''
class Word:

    def __init__(self):
        pass


    def ctrl_event(self,keynumber=None):
        pass

    #添加附件
    def add_attachment(self,filename):
        # ctrl+End移动到word末尾
        k.press_double(keylist=['Control','End'])
        # 输入回车
        k.enter()
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
    def get_two_item_to_tuple(self,filename,sheetname,first_item_index,second_item_index,include_headline='N'):
        sheet = self.init_sheet(filename,sheetname)
        col1 = sheet.col_values(first_item_index)
        col2 = sheet.col_values(second_item_index)
        begin_index = 0 if include_headline == 'Y' else 1
        return [(col1[i],col2[i]) for i in range(begin_index,len(col1))]

    #根据筛选条件获取列的值组成列表：结果列的名称，筛选列的名称，条件（如果为空，代表除第一行之外的全部）
    def get_col_values_by_condition(self,filename,sheetname,condition=('','','')):
        headline_list = self.get_headline_from_excel(filename,sheetname)
        sheet_list = self.get_row_values_from_excel(filename,sheetname)
        tg_list = []
        for i in sheet_list:
            if (condition[2] != '' and i[headline_list.index(condition[1])] in condition[2]) or condition[2]=='':
                tg_list.append(i[headline_list.index(condition[0])])
        return tg_list

    #读取Excel，获得字典列表：key_index默认取1是因为我习惯把第一列作为序列列，第二列才是名称，第二列的索引为1
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


'''MarkDown处理'''
class MarkDown:

    def __init__(self):
        pass

    #根据三级标题，获取对应的表格，转换成df格式
    #这个函数主要用来存放一些表格数据，做成dataframe继续处理
    def get_table_to_df_by_heading(self,filename, heading_name, table_index=0):
        """
        提取指定三级标题下（包含其子标题内）的表格。
        :param filename: Markdown 文件路径，记得加后缀.md
        :param heading_name: 三级标题内容（不用带 ###）
        :param table_index: 存在多个表格时，提取第几个（默认第一个）
        """
        # 1. 读取文件并转 HTML
        md_text = Path(filename).read_text(encoding="utf-8")
        html_text = markdown.markdown(md_text, extensions=['tables'])

        # 2. 解析 HTML
        soup = BeautifulSoup(html_text, "html.parser")

        # 3. 找到目标 H3 节点
        target_h3 = soup.find("h3", string=lambda text: text and text.strip() == heading_name.strip())
        if not target_h3:
            raise ValueError(f"未找到 3 级标题：### {heading_name}")

        # 4. 从 H3 往下找表格，遇到下一个 H1/H2/H3 停止
        tables = []
        for sibling in target_h3.next_siblings:
            # 只有遇到 1、2、3 级标题才停止（遇到 h4 及以下会继续收集）
            if sibling.name in ("h1", "h2", "h3"):
                break
            if sibling.name == "table":
                tables.append(sibling)

        # 5. 校验并返回
        if not tables:
            raise ValueError(f"标题 ### {heading_name} 下没有找到表格")
        if table_index >= len(tables):
            raise IndexError(f"标题 ### {heading_name} 下只有 {len(tables)} 个表格，无法获取第 {table_index} 个")

        # 6. 将 HTML 表格转换为 Pandas DataFrame
        # 要让它知道这是一段 HTML 文本，而不是文件路径，所以用io.StringIO
        df = pd.read_html(io.StringIO(str(tables[table_index])))[0]

        return df

    #把原始Markdown文本，转换成能输出HTML包含图片的文本
    def convert_raw_text_to_normal_text(self,md_text):
        """
        将各种不规则的 Markdown 图片链接统一替换为标准的 ![](Images/文件名) 格式
        """
        # 1. 处理 Obsidian 风格：![[20261023101026.png]] -> ![](Images/20261023101026.png)
        def replace_obsidian(match):
            # 提取 ![[ 和 ]] 之间的内容
            raw_path = match.group(1)
            # 统一斜杠，并提取最后一部分作为文件名，防御带路径的情况
            filename = raw_path.replace("\\", "/").split("/")[-1].strip()
            return f"![](Images/{filename})"

        # 匹配 ![[...png]]
        md_text = re.sub(r'!\[\[(.*?\.png)\]\]', replace_obsidian, md_text)

        # 2. 处理标准格式：![xxx](path/to/file.png) -> ![](Images/file.png)
        def replace_standard(match):
            # 提取括号内部的路径
            raw_path = match.group(1)
            # 统一斜杠，按 / 分割取最后一个部分（文件名），并去掉可能残留的右括号
            filename = raw_path.replace("\\", "/").split("/")[-1].replace(")", "").strip()
            return f"![](Images/{filename})"

        # 匹配 ![xxx](...png)
        md_text = re.sub(r'!\[.*?\]\((.*?\.png)\)', replace_standard, md_text)

        return md_text

    #把Markdown格式的文本，转换成HTML文本，图片以Base64格式嵌入
    def convert_md_content_to_html_content(self,md_text):
        #组装md_text的时候注意，遇到图片，一律转换成标准格式，因为插件不认wikilink，判断是图片就是感叹号开头，png加右括号结尾
        #base_path:md文件所在目录，用来解析相对图片路径
        mkd = markdown.Markdown(extensions=["pymdownx.b64"],extension_configs={"pymdownx.b64":{"base_path": f"{TestResult_dir}"}})
        html_content = mkd.convert(md_text)
        #后续可以把内容写入到一个HTML文件里
        #给所有表格加上边框和内联样式
        html_content = html_body.replace(
            '<table>',
            '<table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">'
            )
        #给表头和单元格加一点内边距，看起来更像网页
        html_content = html_content.replace('<th>', '<th style="padding: 8px; background-color: #f2f2f2; border: 1px solid #ccc;">')
        html_content = html_content.replace('<td>', '<td style="padding: 8px; border: 1px solid #ccc;">')
        return html_content


'''邮件相关'''
class Email:

    def __init__(self):
        pass

    #调用 Outlook发送邮件
    def send_email_by_outlook(self,html_content):
        # 启动 Outlook 程序
        outlook = win32com.client.Dispatch("Outlook.Application")
        # 创建一封新邮件
        mail = outlook.CreateItem(0)
        # 邮件主题
        mail.Subject = "自动化测试报告"
        mail.To = "zhangsan@example.com;lisi@example.com"  # 收件人
        mail.CC = "manager@example.com"                   # 抄送人
        mail.BCC = "secret@example.com"                   # 密送人
        mail.HTMLBody = html_content
        # 显示邮件窗口（让你确认或直接发送）
        mail.Display()
        # mail.Send()#发送














'''操作数据库'''
class operate_db:
    """
    备注：对于查询语句，可以使用
    cur.fetchone()
    cur.fetchmany()
    cur.fetchall()
    sql = '''
        SELECT * FROM TABLE(NOLOCK) WHERE PARAMETER1 = %s AND PARAMETER2 = %s AND PARAMETER3 = %d
    '''
    #execute可以直接传参
    cur.execute(sql, PARAMETER1, PARAMETER2, PARAMETER3)
    """
    def __init__(self):
        pass

    @staticmethod
    def operate_mysql(mysql,sql,print_sql='Y',fetchone_fetchall='fetchall',default_cursor='tuple'):
        db = pymysql.connect(host=mysql['host'],port=mysql['port'],user=mysql['user'],passwd=mysql['passwd'],database=mysql['database'],charset=mysql['charset'])  # 连接数据库
        if default_cursor=='tuple':
            cur = db.cursor()  # 获取游标，select结果以元组方式返回
        else:
            cur = db.cursor(pymysql.cursors.DictCursor) #获取游标，select结果以字典方式返回
        # sql = '''show databases;'''
        # 执行sql语句
        results = []
        try:
            if isinstance(sql,str):
                sqllist=[sql]
            else:
                sqllist=sql
            for x in sqllist:
                if print_sql=='Y':
                    print(x)
                cur.execute(x)
                if cur.description:#如果是查询语句，增删改就是None
                    result = None
                    if fetchone_fetchall == 'fetchall':
                        result = cur.fetchall()
                    elif fetchone_fetchall == 'fetchone':
                        result = cur.fetchone()
                    elif fetchone_fetchall == 'fetchmany':
                        result = cur.fetchmany()
                    else:
                        raise ValueError("不支持的 fetch 模式")
                    results.append(result)
            db.commit()#不管是select还是update，最终都提交一下
        except Exception as e:
            db.rollback()
            print(f"数据库操作异常: {e}")
            raise
        finally:
            cur.close()
            db.close()
        return results

    #操作sqlite3
    @staticmethod
    def operate_sqlite3(sqlite_db, sql, sql_data=None, print_sql=True):
        """
        :param sqlite_db: db文件路径
        :param sql: sql命令（字符串，或字符串列表）
        :param sql_data: 条件或插入的数据（元组、列表、或列表套元组/列表）
        :param print_sql: 是否打印完整的 SQL
        """
        conn = sqlite3.connect(sqlite_db)
        cur = conn.cursor()
        try:
            # ================= 1. 单条 SQL 处理 =================
            if isinstance(sql, str):
                if sql_data is None:
                    cur.execute(sql)
                    if print_sql:
                        print(sql)
                # 如果是单条数据，如: (1, 2) 或 [1, 2]
                elif isinstance(sql_data, (tuple, list)) and len(sql_data) > 0 and not isinstance(sql_data[0], (tuple, list)):
                    cur.execute(sql, sql_data)
                    if print_sql:
                        formatted_sql = sql
                        for param in sql_data:
                            # 强转 str，防止数字/元组导致 replace 报错
                            formatted_sql = formatted_sql.replace('?', str(param), 1)
                        print(formatted_sql)
                # 如果数据是列表套列表/元组（如批量插入），但 sql 传了字符串，走 executemany
                elif isinstance(sql_data, list):
                    cur.executemany(sql, sql_data)
                    if print_sql:
                        for row in sql_data:
                            formatted_sql = sql
                            for param in row:
                                formatted_sql = formatted_sql.replace('?', str(param), 1)
                            print(formatted_sql)
            # ================= 2. 多条 SQL 语句处理 =================
            elif isinstance(sql, list):
                # 2.1 如果是带参数的批量执行（例如 sql_data 是批量插入的数据）
                if sql_data is not None:
                    # 默认 sql[0] 是带 ? 的模板
                    cur.executemany(sql[0], sql_data)
                    if print_sql:
                        for row in sql_data:
                            formatted_sql = sql[0]
                            for param in row:
                                formatted_sql = formatted_sql.replace('?', str(param), 1)
                            print(formatted_sql)
                # 2.2 如果只是单纯的多个独立 SQL 脚本拼接（不需要参数）
                else:
                    sql_script = ''.join(sql)
                    cur.executescript(sql_script)
                    if print_sql:
                        print(sql_script)
            else:
                raise ValueError("sql 参数必须是字符串或字符串列表")
            # ================= 3. 统一提交与异常处理 =================
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"SQLite执行异常: {e}")
            raise  # 不吞错，直接抛出给上层
        finally:
            cur.close()
            conn.close()


    @staticmethod
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

    @staticmethod
    def operate_mongodb(host,port,database_name,collection_name,insert_content):
        collection=pymongo.MongoClient(host,int(port))[database_name][collection_name]
        collection.insert_many(insert_content)


'''Windows和Linux互相传文件和文件夹'''
class Transfer_File:

    def __init__(self):
        self.pscp_path=os.path.join(tool_dir,'pscp.exe')

    def Window_to_Linux_File(self,remoteServer, window_path, linux_path):
        cmd = '{pscp_path} -pw {password} {window_path} {username}@{linux_ip}:{linux_path}'.format(pscp_path=self.pscp_path,password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Window_to_Linux_Dir(self,remoteServer, window_path, linux_path):
        cmd = '{pscp_path} -pw {password} -r {window_path} {username}@{linux_ip}:{linux_path}'.format(pscp_path=self.pscp_path,password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Linux_to_Window_File(self,remoteServer, linux_path, window_path):
        cmd = '{pscp_path} -pw {password} {username}@{linux_ip}:{linux_path} {window_path}'.format(pscp_path=self.pscp_path,password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)

    def Linux_to_Window_Dir(self,remoteServer, linux_path, window_path):
        cmd = '{pscp_path} -pw {password} -r {username}@{linux_ip}:{linux_path} {window_path}'.format(pscp_path=self.pscp_path,password=remoteServer[3], window_path=window_path, username=remoteServer[2], linux_ip=remoteServer[0],linux_path=linux_path)
        os.system(cmd)


'''上传'''
class WinUpLoadFile:

    @staticmethod
    def winUpLoadFile(file_path,title):
        time.sleep(4)
        #一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
        # #32770是许多系统对话框的默认类名
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

    #把输出内容写入到文件，默认换行，换行是指在末尾多加一空行
    def write_to_file(self,filename,mode,content,next_line='N'):
        with open(filename,mode,encoding='utf-8') as f:
            if next_line=='Y':
                f.write(content+'\n')
            else:
                f.write(content)

    #将字典转换成json写入文件
    def write_dict_to_file(self,filename,mydict,mode='w'):
        content=c.convert_dict_to_format_json(mydict)
        self.write_to_file(filename,mode,content,next_line='N')


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

    #读取json文件，返回字典
    def get_mydict_from_json_file(self,filename):
        if not os.path.exists(filename):
            self.write_to_file(filename,'w','',next_line='N')
            mydict= {}
        else:
            content=f.read_file_return_content(filename)
            if Judge().is_json(content):
                mydict=c.convert_json_to_dict(content)
            else:
                mydict={}
        return mydict

    #读取txt文件，返回列表
    def get_mylist_from_txt_file(self,filename):
        content=self.read_file_return_content(filename)
        return c.convert_str_to_list(content,'')

    #读取csv文件，返回DataFrame，暂无必要，直接用pd的方法即可

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

    #删除目录下所有文件
    def delete_files(self,file_path,filename=''):
        #如果filename为空，代表删除目录下所有文件，如果是逗号分隔的多个文件，删除多个
        if filename=='':
            #删除整个目录
            shutil.rmtree(file_path)
            #重建目录
            # os.makedirs(file_path,exist_ok=True)#为True表示已存在不报错
        elif ',' in filename:
            for i in filename.split(','):
                #如果是文件，直接删除，如果是文件夹，递归删除
                try:
                    if os.path.isfile(i):
                        os.remove(i)
                    elif os.path.isdir(i):
                        self.delete_files(i)
                        #删除空文件夹
                        os.rmdir(i)
                except Exception as e:
                    print('删除%s出错，出错原因%s' % (i,e))
        #删除单个文件
        else:
            os.remove(filename)

    #解压文件
    def jieya_rar_zip_file(self,file_path,filename):
        #zipfile库只能解压ZipCrypto加密的包，AES加密的不支持：7-Zip、WinRAR、好压等默认使用AES加密
        zip_path = os.path.join(file_path,filename)
        with zipfile.ZipFile(zip_path) as zf:
            for info in zf.infolist():
                #如果 compress_type 是 99，就说明是 AES 加密
                print(info.filename, "压缩方式:", info.compress_type, "加密标志:", info.flag_bits)

    #读取压缩包
    def read_rar_zip_file(self,file_path,filename):
        with open(os.path.join(file_path,filename),'rb') as f:
            head = f.read(8)
        print(head)


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
    def convert_str_to_list(self,str,sepreate_by=''):
        if sepreate_by != '':
            get_list=[one.strip() for one in str.split(sepreate_by) if one != '']
        else:
            get_list = [one.strip() for one in str.splitlines() if one != '']
        return get_list

    #字符串转换成列表，去重并排序
    def convert_str_to_list_with_distinct_value_and_order(self,str,sepreate_by):
        return sorted(list(set(self.convert_str_to_list(str,sepreate_by))))

    #字符串转换成字符串，去掉字符串内部的空格和换行
    def convert_str_to_str_without_huanhang(self,string):
        new_string=''
        for i in string.splitlines():
            j=i.split()
            new_string+=''.join(j)
        return new_string


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

    #将列表转换为DataFrame
    def convert_list_to_DataFrame(self,mylist,title_name_list=None,begin_index=1):
        #列表是个大列表中长度相同的小列表，长度与传入的title_name_list一致
        #如果不传title_name_list表示不需要标题，此时标题会自动使用0,1,2索引
        if title_name_list:
            df=pd.DataFrame(mylist,index=range(begin_index,begin_index+len(mylist)),columns=title_name_list)
        else:
            df=pd.DataFrame(mylist,index=range(begin_index,begin_index+len(mylist)))
            df.to_string(header=False)
        return df

    # #将DataFrame格式化输出，没啥用
    # def convert_DataFrame_to_format_DataFrame(self,df, padding=2):
    #     #计算每列所需最小宽度
    #     custom_col_space=[max(len(str(item)) for item in df[col]) + padding for col in df.columns]
    #     df.to_string(index=False,col_space=custom_col_space,justify='left')
    #     return df


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
        return list(dict.fromkeys(mylist))

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
        return json.dumps(mydict,sort_keys=True,indent=2,ensure_ascii=False,default=default_dump)

    #读取JSON字符串，转换成字典
    def convert_json_to_dict(self,json_content):
        return json.loads(json_content)

    #将字典转换成DataFrame，以便写入csv文件(暂未实现，因为第一列不好处理)
    def convert_dict_to_df(self,mydict):
        df=pd.DataFrame()

    #将字典写成csv文件（特殊的字典，键的值是列表）
    def convert_dict_to_csv_format(self,mydict):
        tg_str=''
        for k,v in mydict.items():
            tg_list=[k]+v
            tg_str+=Convert().convert_list_to_string(tg_list,',')
            tg_str+='\n'
        tg_str=tg_str[:-1]
        tg_str.replace(',0.0,',',0,')
        return tg_str

    #将两个列表转换成键值对，要保证两者的长度一致
    def convert_two_list_to_dict(self,key_list,value_list):
        tg_dict = {}
        for i in range(len(key_list)):
            tg_dict[key_list[i]] = value_list[i]
        return tg_dict

    #将浮点数转换成精确的四舍五入值，默认保留小数点后2位
    def convert_float_to_decimal(self,number,weishu=2):
        return Decimal(str(number)).quantize(Decimal('0.%s' % '0'*weishu),rounding='ROUND_HALF_UP')

    #将浮点数转换成字符串，并保留固定长度（自动添加空格）。默认左对齐，无负数
    def convert_float_to_fixed_legth(self,number,length=7,duiqi='l',include_minus=False):
        str_number=str(number)
        #如果该列的值含负数，该值为正，则加上空格与负号对应
        if include_minus==True and '-' not in str_number:
            str_number=' '+str_number
        return str_number.ljust(length) if duiqi=='l' else str_number.rjust(length)

    #将字符串设置为固定长度
    def convert_str_to_fixed_length(self,string,length=7,duiqi='l'):
        #首先计算字符串长度
        length_of_string=len(string)
        #需要添加的空格
        need_blank=int(length-length_of_string) if length>=length_of_string else 0
        if duiqi=='l':
            return string+' '*need_blank
        else:
            return ' '*need_blank+string

    #将字段转换成数据库sql语句中的字段（也就是带引号）
    def convert_column_to_sql_formart(self,*column):
        tg_list=[]
        for i in column:
            #如果是字符串，就要加引号
            if isinstance(i,str):
                i="'%s'" % i
            elif i is None:
                i='%s' % 'null'
            else:
                i=i
            tg_list.append(i)
        return tg_list

    #将json文件，转换成parametrize参数
    #pytest使用的parametrize格式是列表里面放元组元素，例如[{"key1": "value1"}, {"key2": "value2"}]
    def convert_json_file_to_parametrize(self,filename):
        #检查文件是否存在
        file = os.path.join(json_dir,filename)
        if not os.path.exists(file):
            raise FileNotFoundError(f"找不到 JSON 文件: {filename}")
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        #校验顶层是否为列表
        if not isinstance(data, list):
            raise TypeError
        return data





#给Convert().convert_dict_to_format_json用，解决：Object of type int64 is not JSON serializable的问题
def default_dump(obj):
    """Convert numpy classes to JSON serializable objects."""
    if isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj


'''计算'''
class Calculate:

    def __init__(self):
        pass

    #字符串转换为md5值
    def get_md5_by_str(self,string):
        m = hashlib.md5()
        m.update(string.encode("utf8"))
        return m.hexdigest()




'''带颜色的字符串'''
class Color:
    """
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
    """
    def output_string_with_color(self,content,color=31):
        """
        :param content:
        :param color: 可以输入数字也可以输入英文
        :return:
        """
        match color:
            case 'black':
                color = 30
            case 'red':
                color = 31
            case 'green':
                color = 32
            case 'yellow':
                color = 33
            case 'blue':
                color = 34
            case 'magenta':
                color = 35
            case 'cyan':
                color = 36
            case 'white':
                color = 37
            case _:
                color = color
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





#matplotlib字体设置
font={"family":"Microsoft YaHei","size":12}
plt.rc('font', **font)#设置字体的更多属性
# plt.rc('axes', unicode_minus=False)#解决坐标轴负数的负号显示问题


'''截图'''
class Snapshot:

    def __init__(self):
        pass

    #通过pillow截图
    def save_snapshot_by_pillow(self,area,filename):
        # 第一个参数 开始截图的x坐标
        # 第二个参数 开始截图的y坐标
        # 第三个参数 结束截图的x坐标
        # 第四个参数 结束截图的y坐标
        if area=='full':
            ImageGrab.grab().save(filename)
        else:
            ImageGrab.grab(area).save(filename)

    #通过pyautogui截图
    def save_snapshot_by_pyautogui(self,area,filename):
        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(filename)


'''压缩'''
class Compress:

    def __init__(self):
        pass

    #用zipfile库对文件列表打包
    def make_zip_by_filelist(self,packagename,filelist):
        z = zipfile.ZipFile(packagename,'w')
        [z.write(one) for one in filelist]
        z.close()

    #对文件夹打包
    def make_zip_by_dirpath(self,packagename,dirpath:str):
        with zipfile.ZipFile(packagename, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(dirpath):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, dirpath)
                    zf.write(file_path, arcname)




'''判断'''
class Judge:

    def __init__(self):
        pass

    #判断输入的字符串是否为字典类型的json
    def is_json(self,input_str):
        if not isinstance(input_str, str):
            return False
        try:
            data = json.loads(input_str)
            return isinstance(data, dict)
        except ValueError:
            return False

    #查看字符串或列表中是否存在重复项
    def is_contains_repeat(self,alist):
        blist = []
        for i in alist:
            if i in blist:
                print(i)
            else:
                blist.append(i)
        print(blist)

    #判断两个文件的内容是否一致
    def is_two_files_same_content(self,file1,file2):
        file1_content=File().read_file_return_content(file1)
        file2_content=File().read_file_return_content(file2)
        if file1_content==file2_content:
            return True
        else:
            return False






'''设置环境变量，Windows通过cmd命令修改系统环境变量，Linux修改profile文件修改'''
class set_env_variable:

    def __init__(self):
        pass

    #通过环境变量名，获取环境变量值
    def get_env_variable_value(self,variable_name):
        output=subprocess.run('wmic ENVIRONMENT where name="%s" get UserName,VariableValue' % variable_name)
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


'''客户端相关操作'''
class Application:

    def __init__(self):
        pass

    #输入信息
    def send_message(self,hwnd,message):
        """
        :param hwnd: 窗口的句柄
        :param message: 要发送的消息内容
        :return:
        """
        #让窗口活跃
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.5)
        #模拟键盘输入
        for char in message:
            #WM_CHAR比WM_SETTEXT更可靠，代表逐字输入
            #WM_SETTEXT是会修改窗口的标题，WM_CHAR才是往输入框输入内容
            win32gui.SendMessage(hwnd,win32con.WM_CHAR,ord(char),0)
            time.sleep(randint(1,3)/100)

    #获取客户端坐标，分别代表左上，右下两个点
    #dlg是pywinauto获取到的窗口类，如dlg=app.window(title='aaa')
    def get_position_by_pywinauto(self,dlg):
        window_rect = dlg.rectangle()
        left = window_rect.left
        top = window_rect.top
        right = window_rect.right
        bottom = window_rect.bottom
        return left,top,right,bottom

    #将客户端居中，并占1/4大小
    def set_app_position_by_pywinauto(self,dlg,pos='center'):
        #如果pos为center，代表占1/4且居中
        #如果pos为full，代表全屏
        if pos=='center':
            left,top,right,bottom=Screen().get_move_window_position()
            dlg.move_window(left,top,right,bottom)
        elif pos=='full':
            dlg.maximize()
        else:
            dlg.minimize()

    #遍历，获取所有的窗口
    def get_all_windows_by_pywin32(self):
        hwnd_list=[]
        win32gui.EnumWindows(lambda hwnd,param:param.append(hwnd),hwnd_list)
        #通过句柄查找名称
        hwnd_name_list=[]
        for i in hwnd_list:
            hwnd_name=win32gui.GetWindowText(i)
            #Default IME是系统默认的输入法
            #HintWnd 是某些应用程序（如 IDE、编辑器或自定义工具）中常见的提示窗口
            #MSCTFIME UI是微软拼音输入法
            if hwnd_name not in ['','Default IME','HintWnd','MSCTFIME UI','Sogou_TSF_UI']:
                hwnd_name_list.append(hwnd_name)
        # hwnd_name_list=[win32gui.GetWindowText(i) for i in hwnd_list if win32gui.GetWindowText(i) not in ['','Default IME']]
        return hwnd_name_list

    #遍历，获取主窗口下的所有副窗口(这个函数有问题)
    def get_all_second_windows_by_pywin32(self,hwnd):
        hwnd_child_list=[]
        win32gui.EnumChildWindows(hwnd,lambda hwnd,param:param.append(hwnd),hwnd_child_list)
        return hwnd_child_list

    #移动鼠标点击程序内的某个位置：使用pywinauto
    def click_by_pywinauto_mouse(self,dlg,relative_x,relative_y):
        """
        :param dlg:
        :param relative_x: 元素相对程序窗口左上角的横坐标偏移
        :param relative_y: 元素相对程序窗口左上角纵坐标的偏移
        :return:
        """
        left,top,right,bottom=self.get_position_by_pywinauto(dlg)
        x_screen=left+relative_x
        y_screen=top+relative_y
        #移动鼠标指针，duration是指在1秒内完成该操作
        # pyautogui.moveTo(x_screen,y_screen,duration=1)
        #移动鼠标指针也可以用下面的方法
        # pywinauto.mouse.move((x_screen,y_screen))
        time.sleep(random()/10)
        pywinauto.mouse.click(coords=(x_screen,y_screen))

    #移动鼠标点击程序内的某个位置：使用pyautogui
    def click_by_pyautogui_mouse(self,x,y,wait_time=0):
        #wait_time是点击鼠标后的等待时间
        #x，y是相对左上角的坐标
        pyautogui.click(x,y)

    def wheather_exist_by_pyautogui(self,imageName):
        image_file = os.path.join(lightshot_dir, imageName)
        try:
            location = pyautogui.locateOnScreen(image_file,confidence=0.9)
            # a,b,c,d=location
            # print('找到了元素，是',imageName)
            # print(a,b,c,d)
            return location
        except:
            # print('未找到元素',imageName)
            return None

    #根据截图查找元素，使用pyautogui点击该元素
    def click_by_pyautogui_image(self,imageName,wait_time=0):
        location = self.wheather_exist_by_pyautogui(imageName)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
        else:
            print('未找到元素')




'''电脑端相关操作'''
class Windows:

    def __init__(self):
        pass

    #检查是否有管理员权限
    def check_is_admin(self):
        TOKEN_QUERY = 0x0008
        TokenElevation = 20
        class TOKEN_ELEVATION(ctypes.Structure): _fields_ = [("TokenIsElevated", ctypes.wintypes.DWORD)]
        h_token = ctypes.wintypes.HANDLE()
        if not ctypes.windll.advapi32.OpenProcessToken(ctypes.windll.kernel32.GetCurrentProcess(), TOKEN_QUERY, ctypes.byref(h_token)): return False
        elevation, returned_size = TOKEN_ELEVATION(), ctypes.wintypes.DWORD()
        success = ctypes.windll.advapi32.GetTokenInformation(h_token, TokenElevation, ctypes.byref(elevation), ctypes.sizeof(elevation), ctypes.byref(returned_size))
        ctypes.windll.kernel32.CloseHandle(h_token)
        print("========================================")
        return success and elevation.TokenIsElevated != 0

    #以管理员身份运行（这串代码有问题，升级到管理员权限，不会往下执行其他脚本）
    def execute_by_admin(self):
        """以管理员身份运行。如果不是管理员，则提权重启当前脚本并退出。"""
        if self.check_is_admin():
            return
        params = " ".join(f'"{a}"' for a in sys.argv)
        ret = ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
        if ret > 32:
            print(f"提权成功，新进程已启动。旧进程退出。")
        else:
            print(f"提权失败，错误码：{ret}")
        sys.exit()


    #使用pywin32将字符串复制到剪切板，方便直接粘贴
    def copy_text_to_clipboard(self,text='aaa'):
        import win32clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()

    #查找当前打开的所有窗口
    def list_all_windows(self):
        """分别用 uia 和 win32 后端枚举所有可见窗口"""
        all_windows = {}  # 用句柄去重

        for backend in ["uia", "win32"]:
            try:
                for window in pywinauto.Desktop(backend=backend).windows():
                    if window.is_visible() and window.window_text():
                        handle = window.handle
                        # 如果该句柄还没记录过，就加进去
                        if handle not in all_windows:
                            all_windows[handle] = {
                                "title": window.window_text(),
                                "class_name": window.class_name(),
                                "backend": backend
                            }
            except Exception as e:
                print(f"枚举 {backend} 后端时出错: {e}")

        # 打印结果
        for handle, info in all_windows.items():
            print(f"标题: {info['title']}")
            print(f"类名: {info['class_name']}")
            print(f"后端: {info['backend']}")
            print("-" * 30)

    #定位到设置窗口
    def locate_to_setting_window(self):
        #启动设置
        #用系统命令打开设置窗口
        os.startfile("ms-settings:")
        #说明：启动URI用os.startfile，启动exe用start
        app = pywinauto.Application(backend="uia").connect(title="设置", class_name="ApplicationFrameWindow")
        time.sleep(2)  # 等待设置窗口打开
        setting_window = app.window(title="设置", class_name="ApplicationFrameWindow")
        return setting_window

    #定位到创建并格式化磁盘分区
    def locate_to_diskpart_window(self):
        try:
            app = pywinauto.Application(backend='uia').connect(title='磁盘管理',class_name='MMCMainFrame',timeout=2)
        except:
            os.startfile("diskmgmt.msc")
            time.sleep(2)
            app = pywinauto.Application(backend='win32').connect(title='磁盘管理',class_name='MMCMainFrame')
        main = app.window(title='磁盘管理',class_name='MMCMainFrame')
        return main






'''ffmpeg的使用'''
class Ffmpeg:

    def __init__(self):
        pass

    def ddd(self):
        pass



'''一些混合的工具'''
class Tools:

    def __init__(self):
        pass

    #读取从世行下载的Excel文件，将数据写入sqlite
    def get_data_and_write_sql(self, sourcefile):
        sqlList = []
        with open(sourcefile, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.read().splitlines()
        for one in lines[1:]:
            one = one.strip()
            if not one:
                continue
            oneList = one.split('\t')
            if len(oneList) <= 41:
                continue
            countryName = oneList[0].strip().replace("'", "''")
            for idx in range(15, 42):
                yearName = idx + 1977
                nian = f'y_{yearName}'
                raw_val = oneList[idx].strip()
                if raw_val in ('n/a', '..', '', '-'):
                    value = 0.0
                else:
                    try:
                        value = float(raw_val.replace(',', '')) * 10
                    except ValueError:
                        value = 0.0
                sql = f"update gdp_by_year set {nian}='{value:.3f}' where country_en_name='{countryName}'"
                sqlList.append(sql)
        return sqlList

    #给Linux系统安装Python3
    def install_python3_to_linux(self):
        window_path = 'D:\\TDdownload'
        linux_path = '/usr/local'
        #通过Windows向Linux传Python安装包，传到/usr/local
        if os.path.isfile(window_path):
            pscp.Window_to_Linux_File(cfg.remoteServer,window_path,linux_path)
        else:
            print('这个目录下没有Python安装包！')
            sys.exit()
        #如果没有Python安装包，通过selenium获取
        #通过weget命令获取安装包，传到/usr/local
        # cmd = '''cd /usr/local
        # wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
        # '''
        #
        # po.paramiko_operate_linux(cmd)
        #安装到/usr/bin/python3下
        #1.上传shell脚本并赋权限、执行
        pscp.Window_to_Linux_File(cfg.remoteServer,r'D:\TDdownload\Document\Shell\backup_common\install_python3_to_linux.sh','/home')

        cmd = '''cd /home
        chmod +x /home/install_python3_to_linux.sh
        ./install_python3_to_linux.sh %s;
        ''' % cfg.Python_version
        po.paramiko_operate_linux(cfg.remoteServer,cmd)

    #使用you-get工具下载视频
    def download_video_by_you_get(self,url):
        r"""
        抖音视频，下载不成功。提示cookie已过期，刚获取的cookie，手动在浏览器上用插件下载。YouTube下载，要提供cookie，也要使用代理。
        you-get --no-caption -o "E:\\TDdownload" -c "cookie.txt" "https://www.bilibili.com/video/BV17zEEz5Ei8"
        :return:
        """
        #下载之前先更新cookie.txt，更新url链接
        cookie_file=os.path.join(ultra_dir,'cookie.txt')
        cmd.exec_cmd_by_subprocess(['you-get --no-caption -o "E:\\TDdownload" -c "%s" "%s"' % (cookie_file,url)])

    #用BBDown.exe下载B站视频
    def download_video_by_BBDown(self,download_dir=r'E:\TDdownload',video_uri='BV1TVhf6tEYb'):
        #从cookie-editer获取Header String类型的cookie，写到BBDown.data文件中
        cmd = ['BBDown.exe','--work-dir',download_dir,video_uri]
        #capture_output=True,        # 捕获输出
        #text=True,                  # 以文本形式返回
        #encoding='utf-8',           # 如果乱码可改成 'gbk'
        #check=True                  # 命令失败时抛异常
        process = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='gbk',errors='replace',bufsize=1)
        assert process.stdout is not None
        for line in process.stdout:
            print(line, end='')
        # process.wait()
        # if process.returncode != 0:
        #     raise RuntimeError(f'BBDown 执行失败，返回码：{process.returncode}')

    #制作rht文件，origin_picture要用PNG或BMP格式(不成功，打不开)
    def make_rht_file(self,origin_picture,inside_file):
        with open(origin_picture, 'rb') as img:
            img_data = img.read()
        with open(inside_file, 'rb') as f:
            hidden_data = f.read()
        combined = img_data + hidden_data
        target_name=os.path.join(r'E:\TDdownload','rht_%s.png' % myTime().mytime())
        print(target_name)
        with open(target_name, 'wb') as out:
            out.write(combined)

    #获取图片，然后将图片放大或缩小
    def fangda_or_suoxiao_picture(self,picture_file,scale):
        """
        :param picture_file:
        :param scale: 放大或缩小的比例，浮点数
        :return:
        """
        img = Image.open(picture_file)
        width, height = img.size
        new_width = int(width * scale)
        new_height = int(height * scale)
        # 等比例缩放（使用LANCZOS滤镜保证质量）
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_img.save(picture_file)











"""第三方API"""
class ThirdpartApi:

    def __init__(self):
        pass

    #百度API，文字识别，主要用于识别验证码
    def get_ocr_result_by_baidu_aip(self):
        #引入库
        from aip import AipOcr
        aip_config={
            'appId': 'xxxx',
            'apiKey': 'xxxxxx',
            'secretKey': 'xxxxxxxxx'
        }
        client = AipOcr(**aip_config)
        #读取验证码图片信息,screenImg是图片地址
        with open(screenImg,'rb') as fp:
            img_content=fp.read()
        #获取验证码
        result=client.basicGeneral(img_content)
        YanzhengMa = result['words_result'][0]['words'].replace(' ', '')
        if ':' in YanzhengMa:
            YanzhengMa_result = YanzhengMa.replace(':','')
        else:
            YanzhengMa_result = YanzhengMa
        return YanzhengMa_result








#实例化上面的方法
a=Application()
f=File()
c=Convert()
t=myTime()
k=Keyboard()
w=Windows()
cmd=Cmd()
ff=Ffmpeg()
db=operate_db()
tool=Tools()
fake = Faker('zh_CN')
md=MarkDown()



if __name__=="__main__":
    # exec_cmd_by_subprocess('dir')
    # print(get_current_username_by_exec_cmd('net config workstation'))
    # print(myTime().mymonth())
    # print(myTime().mydate())
    # print(myTime().mybeforedate(before_or_after_days=-120))
    # print(myTime().mytime())
    # print(myTime().mytimestamp())
    # Transfer_File().Window_to_Linux_File(remoteServer, r'D:\TDdownload\Document\Python\test\memory111.py', '/home')
    # Transfer_File().Window_to_Linux_Dir(remoteServer,r'D:\TDdownload\Software', '/home')
    # Transfer_File().Linux_to_Window_File(remoteServer,'/home/aaa.txt', r'D:\TDdownload\Software')
    # Transfer_File().Linux_to_Window_Dir(remoteServer,'/home/phm', r'D:\TDdownload\Software')
    #通过you-get下载视频
    # Tools().download_video_by_you_get("https://www.bilibili.com/video/BV17zEEz5Ei8")
    # print(t.get_timestamp_by_format_date(date='2025-10-26 14:03:00',unit=1,date_format='%Y-%m-%d %H:%M:%S'))
    #读取Markdown中的表格
    md_text = os.path.join(python_dir,'TestCase','TestResult','测试参数.md')
    print(md.get_table_to_df_by_heading(md_text, 'B1'))
