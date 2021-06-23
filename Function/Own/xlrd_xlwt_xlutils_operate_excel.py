#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = ''''''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from random import randint
import xlrd,xlwt,xlutils


#读取excel中的内容
def read_excel():
    wb = xlrd.open_workbook(r'D:\TDdownload\WEO_Data (4).xls')
    sheet = wb.sheet_by_name('WEO_Data (4)')
    cols0 = sheet.col_values(1)
    cols1 = sheet.col_values(8)
    conList = []

    with open(r'D:\TDdownload\Document\Python\SQLFile\execute.sql','w+',encoding='utf8') as f:
        for i in range(len(cols0)):
            #p = int(cols1[i])
            q = cols1[i]
            print(q)
            f.write("update gdp set population_rank_2017='%s' where itemno='%s'\n" % (q,cols0[i]))
            #conList.append('(%s,%s),' % (cols0[i],cols1[i]))
        f.flush()
        f.seek(0)
        sqlList = f.read().splitlines()



if __name__=="__main__":
    pass