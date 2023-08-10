#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''股票交易计算'''

# 引入相关包
from Function.Config.common_variable import *
import tushare as ts
import pandas as pd


# 加了这一行那表格的一行就不会分段出现了
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

ts.set_token('7dc1ab69a90b2cd71b306c17490ab0d382bac9bdcb238d6328ac43f7')

#读取Excel，获得股票&基金列表数据
my_stock_list = Excel().get_row_values_from_excel(stock_config,'Sheet1',include_headline='Y')

dict_my_stock = Convert().convert_excel_list_to_full_dict(my_stock_list,3,needed_column=['投资品种','股票名称','交易价格','预期低价','预期高价','卖出步长','买入步长','是否持仓','是否计算'])

print(Convert().convert_dict_to_format_json(dict_my_stock))







if __name__=="__main__":
    pass