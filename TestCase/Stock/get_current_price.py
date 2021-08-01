#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''获取当前价格'''

# 引入相关包
from Config.common_variable import *
import tushare as ts
import pandas as pd


# 加了这一行那表格的一行就不会分段出现了
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

ts.set_token('7dc1ab69a90b2cd71b306c17490ab0d382bac9bdcb238d6328ac43f7')

my_stock_list = Excel().get_all_values_from_excel('\\'.join([python_dir,'File','Excel','My Stock.xls']),'Sheet1')


# 获取资产类型
def get_asset(assettype):
    return 'E' if assettype == '股票' else 'FD' if assettype == '基金' else 'I' if assettype == '指数' else 'C'


# 获取持有的基金列表和股票列表
def get_fund_and_stock_list():
    return [[i[1], i[3]] for i in my_stock_list if i[12] == "是"]



# df = ts.pro_bar(ts_code='515790.SH,512480.SH,159806.SZ,513050.SH,159949.SZ,159995.SZ,512760.SH,515250.SH,515030.SH,512710.SH,159906.SZ,512970.SH', asset='FD', start_date='20210312', end_date=myTime().mydate())


# 基金和股票，收盘价不是同一列
def get_column_index(assettype):
    return 6 if assettype == '基金' else 5 if assettype == '股票' else 3


# 首先读列表，通过类型和ts_code，调接口获取当前价格，写到最后一个
def get_my_stock_list_with_latest_price():
    # for one in my_stock_list:
    #     if one[3]!='':
    #         df=ts.pro_bar(ts_code=one[3], asset=get_asset(one[1]), start_date=myTime().mybeforedate(before_or_after_days=-3), end_date=myTime().mydate())
    #         print(float(df.iat[0, 6]))
    # my_stock_list_with_latest_price=[[one[0],one[3],numpy.float(ts.pro_bar(ts_code=one[3], asset=get_asset(one[1]), start_date='20210312', end_date=myTime().mydate()).iat[0,get_column_index(one[1])])] for one in my_stock_list if one[3]!='']
    return {x[3]: float(ts.pro_bar(ts_code=x[3], asset=get_asset(x[1]), start_date=myTime().mybeforedate(before_or_after_days=-3), end_date=myTime().mydate()).iat[0, get_column_index(x[1])]) for x in my_stock_list if x[3] != ''}


#报IndexError: index 0 is out of bounds for axis 0 with size 0，是因为get_my_stock_list_with_latest_price()函数start_date是昨天，end_date是今天，而今天是周日，所以获取到的结果为空，因为恰好周六和周日不开盘，所以把mybeforedate函数的before_or_after_days改成-2，即获取从前天到今天的记录。
#情形2：股票代码错误，导致找不到数据
#情形3：当前时间为周一收盘前，由于周一的数据还没出，周六周日周一一共三天，之前配置获取两天前的数据，导致没有数据，改成-3
ts_code_with_price = get_my_stock_list_with_latest_price()

output_list = []
for one in my_stock_list:
    #正常情况下，基金以下跌4%，股票以下跌6%补仓，下跌比例加sold_out_plus作为卖出的幅度。
    #当持仓较重且当前大盘已在高位时，需要减仓，所以调高补仓的门槛，调低卖出的门槛
    #当持仓金额不足,1500，可以设置虚拟成交，实际不卖出，但excel上标记卖出价
    # default_rate = 0.04 if one[1] == '基金' else 0.06
    # sold_out_plus = 0.05
    default_rate = 0.07 if one[1] == '基金' else 0.09
    sold_out_plus = 0.05

    actual_rate = default_rate if one[9] == '' else float(one[9])+0.03

    #交易的数量，对应excel第9列
    transaction_amount = 1 if one[8] == '' or abs(int(one[8]))<=1 else int(one[8])

    item_index = int(one[0])
    name = one[2]
    current_price = one[4] if one[4] != '' else 10000.0
    #获取低价（买入价）
    if one[5] == '':
        low_price = round(current_price * (1 - actual_rate), 3)
    else:
        low_price = one[5]
    #获取高价（卖出价）
    if one[6] == '':
        # print(type(current_price))
        # print(current_price)
        # print(one)
        # high_price_rate=0.15 if one[9] == 0.11 else actual_rate
        high_price = round(current_price * (1 + actual_rate + sold_out_plus), 3)
    else:
        high_price = one[6]
    today_price = current_price if one[3] == '' else ts_code_with_price[one[3]]
    output_list.append([item_index, name, one[3], transaction_amount, current_price, low_price, high_price, today_price])
# print(output_list)

# [print(one) for one in output_list]


buy_list = [one for one in output_list if one[7] <= one[5]]
sale_list = [one for one in output_list if one[7] >= one[6]]

# 下面这个模块用来分析，当one[7]是str类型时，是excel中哪条记录有问题
# buy_list=[]
# sale_list=[]
# for one in output_list:
#     print(type(one[7]))
#     print(type(one[5]))
#     print(one)
#     if one[7]<=one[5]:
#         buy_list.append(one)
#     elif one[7]>=one[6]:
#         sale_list.append(one)
#     else:
#         pass


if len(buy_list) > 0:
    for one in buy_list:
        buy_amount = int(int(one[3] * 10 / one[-1]) * 100)
        print(['买入', one[0], one[1], one[2], one[-1], buy_amount])


#未持仓的股票code
# not_hold_stock_list = [one[2] for one in my_stock_list if one[12] == "否"]

'''
卖出的规则：
1、净买入数为1，则在价格相对买入价格涨10%时卖出
'''
if len(sale_list) > 0:
    for one in sale_list:
        sale_amount = 1*1000 if abs(int(one[3]))<=1 else abs(int(one[3]))*1000
        print(['卖出', one[0], one[1], one[2], one[-1],int(sale_amount/(one[-1]*100))*100])

#---------------------------------------------------------------------------------------------------------仓位控制计算公式
'''
1、2500点作为最低点，5000点作为最高点，低于2500可满仓，高于5000点，可最多留20%
2、2500-5000，相差2500点，划分十档，每档250点
3、上证指数每上升250点，减少10%的仓位（权重的10%）
4、权重的划分，上证2500-5000的区间，是第一个权重，占50%，最近的最高点和最低点，作为第二个权重，占50%
5、软件上的仓位和上面计算的仓位不同。需要换算。（因为部分资金不放在APP，放在其他地方）




'''

# 不放在同花顺的资金金额
amount_outside = 44000

# 放在同花顺的资金金额
amount_inside = 300000

# 虚拟资金(资金不属于我，但要用的时候能用)
amount_virtual = 100000

# 当前点位
current_zhishu = 3581

# 最近的最高点
last_max = 3731

# 最近的最低点
last_min = 3328

# 但是这个weight并不是APP上的仓位
weight = (1 - (current_zhishu - 2500) / (5000 - 2500)) * 0.7 + (
            1 - (current_zhishu - last_min) / (last_max - last_min)) * 0.3


# 打印当前应该控制的仓位（APP上显示的）
weight_in_app = weight + weight * (amount_outside + amount_virtual) / amount_inside
# print(weight_in_app)

#盈利分析
'''
假定下跌4%补一次，上涨9%卖一次，补仓10次（总买入11次）每次1元，则最终获利为15.197，赢利大约4元，利润率38%
'''
# print((0.96**10)*(1.09**11)+(0.96**9)*(1.09**10)+(0.96**8)*(1.09**9)+(0.96**7)*(1.09**8)+(0.96**6)*(1.09**7)+(0.96**5)*(1.09**6)+(0.96**4)*(1.09**5)+(0.96**3)*(1.09**4)+(0.96**2)*(1.09**3)+(0.96**1)*(1.09**2)+(0.96**0)*(1.09**1))



if __name__ == "__main__":
    pass
