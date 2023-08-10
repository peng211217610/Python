#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''tushare获取MACD'''

#引入包
from Function.Oppty.function_oppty_common import *
import pandas as pd
import numpy as np
import talib
import tushare as ts
ts.set_token('7dc1ab69a90b2cd71b306c17490ab0d382bac9bdcb238d6328ac43f7')





# 加了这一行那表格的一行就不会分段出现了
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)






#
# df = pro.stk_factor(ts_code='399006.SH', start_date=myTime().mybeforedate(before_or_after_days=-3), end_date=myTime().mydate(), fields='ts_code,trade_date,macd,kdj_k,kdj_d,kdj_j')
#
#
# print(df)



# my_stock_list = Excel().get_all_values_from_excel('\\'.join([python_dir,'File','Excel','My Stock.xls']),'Sheet1')
#
# def get_asset(assettype):
#     return 'E' if assettype == '股票' else 'FD' if assettype == '基金' else 'I' if assettype == '指数' else 'C'
#
#
# # 基金和股票，收盘价不是同一列
# def get_column_index(assettype):
#     return 6 if assettype == '基金' else 5 if assettype == '股票' else 3
#
#
# def get_my_stock_list_with_latest_price():
#     # 下面这段代码用来，当提示index 0 is out of bounds for axis 0 with size 0时，用来查找哪个股票停牌了
#     xxdict={}
#     for x in my_stock_list:
#         if x[3]!='':
#             print(x[2])
#             xxdict[x[3]]=float(pro.stk_factor(ts_code=x[3], asset=get_asset(x[1]), start_date=myTime().mybeforedate(before_or_after_days=-10), end_date=myTime().mydate()).iat[0, get_column_index(x[1])])
#     return xxdict
#
#
# print(get_my_stock_list_with_latest_price())



df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20211201', end_date=myTime().mydate())

# print(df)

close = np.asarray(df["close"].values)

print(close)


diff, dea, my_macd = talib.MACD(close,
                                             fastperiod=12,
                                             slowperiod=26,
                                             signalperiod=9)
macd = np.nan_to_num(my_macd)
print(macd)


# df['EMA12'] = talib.EMA(np.array(close), timeperiod=6)
# df['EMA26'] = talib.EMA(np.array(close), timeperiod=12)
#  # 调用talib计算MACD指标
# df['MACD'],df['MACDsignal'],df['MACDhist'] = talib.MACD(np.array(close),
#                             fastperiod=6, slowperiod=12, signalperiod=9)
#
# print(df.tail())


if __name__=="__main__":
    pass