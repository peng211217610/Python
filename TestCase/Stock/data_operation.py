#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''对数据处理，判断买入和卖出数量'''

#引入相关包
from Function.Common.function_common import *


sheet_values_list=get_all_values_from_excel()

output_list=[]
for one in sheet_values_list:

    if one[1]=='基金':
        default_rate=0.05
    else:
        default_rate=0.10
    if one[9]=='':
        actual_rate=default_rate
    else:
        actual_rate=float(one[9])
    item_index=int(one[0])
    name=one[2]
    current_price=one[4]
    if one[5]=='':
        low_price=round(current_price*(1-actual_rate),3)
    else:
        low_price=one[5]
    if one[6]=='':
        high_price=round(current_price*(1+actual_rate),3)
    else:
        high_price=one[6]
    today_price=one[10]
    output_list.append([item_index,name,current_price,low_price,high_price,today_price])
# print(output_list)

# [print(one) for one in output_list]


# for one in output_list:

buy_list=[one for one in output_list if one[5]<=one[3]]
sale_list=[one for one in output_list if one[5]>=one[4]]

print('买入')
print(buy_list)


print('卖出')
print(sale_list)












if __name__=="__main__":
    pass