#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''读取数据，制作SQL语句写入SQL文件'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg



def get_data_and_write_sql(sourcefile):
    with codecs.open(sourcefile,'r',encoding='ISO-8859-1') as f:
        with open(cfg.sqlfile, 'w+', encoding='utf8') as e:
            lineList = f.read().splitlines()[1:]
            #print(lineList)
            for one in lineList:
                if one == '':
                    break
                oneList = one.split('\t')
                countryName = oneList[0]
                for idx in range(15,42):
                    yearName = idx + 1977
                    nian = 'y_' + str(yearName)
                    if oneList[idx] == 'n/a':
                        value = 0
                    else:
                        value = float(oneList[idx].replace(',','')) * 10
                    #e.write("insert into gdp_by_year (country_en_name,y_1980) values ('%s','%.3f')\n" % (countryName, value))
                    e.write("update gdp_by_year set %s='%.3f' where country_en_name='%s'\n" % (nian,value,countryName))
            e.flush()
            e.seek(0)
            global sqlList
            sqlList = e.read().splitlines()
    return sqlList



if __name__=="__main__":
    get_data_and_write_sql(r'D:\TDdownload\WEO_Data (5).xls')