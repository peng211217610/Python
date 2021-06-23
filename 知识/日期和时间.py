#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg


import time

#返回时间戳，从1970年1月1日0时开始计时的毫秒数
time.time()

#等待时间
time.sleep(1)





import datetime

#常量  datetime.MINYEAR  和  datetime.MAXYEAR

#将时间格式化输出
dt = datetime.datetime.now()
dt.strftime('%Y-%m-%d %H:%M:%S')






import calendar

#判断是否为闰年
calendar.isleap(2019)





























