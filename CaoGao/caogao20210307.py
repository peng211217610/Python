#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = ''''''

#引入相关包
import tushare as ts
import pandas as pd
import numpy
from Function.Common.function_common import myTime

#加了这一行那表格的一行就不会分段出现了
pd.set_option('display.width', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)


pro=ts.pro_api('7dc1ab69a90b2cd71b306c17490ab0d382bac9bdcb238d6328ac43f7')
# ts.set_token('7dc1ab69a90b2cd71b306c17490ab0d382bac9bdcb238d6328ac43f7')


#周线信息
# df = pro.weekly(ts_code='000001.SZ',start_date='20100930',end_date='20210222')

#指数信息
# df = pro.index_basic(market='SZSE')


#获取公募基金信息
# df = pro.fund_basic(market='E')#积分不够

#获取股票信息
# df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

#上证指数行情数据（用ts.set_token）
# df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20100101', end_date='20210312')

#这是基金
# df = ts.pro_bar(ts_code='159995.SZ', asset='FD', start_date='20210312', end_date=myTime().mydate())

#这是股票
# df = ts.pro_bar(ts_code='600094.SH', asset='E', start_date='20150101', end_date=myTime().mydate())


#这是版块
# df = pro.ths_daily(ts_code='885525.TI', start_date='20150101', end_date='20210315')

#货币供应量
df = pro.cn_m(start_m='197001', end_m='202003')


#获取资产类型
def get_asset(assettype):
    return 'E' if assettype=='股票' else 'FD' if assettype=='基金' else 'I' if assettype=='指数' else 'C'







print('df:\n',df)

# print(type(df))


df.to_csv(r'D:\TDdownload\货币供应量.csv')
# df.to_csv(r'D:\TDdownload\版块列表.csv')

# print(type(df.iat[0, 6]))




# sss=numpy.float(df.iat[0, 6])
# print(sss)
# print(type(sss))

if __name__=="__main__":
    pass