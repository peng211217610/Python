#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''计算数字货币挂单'''

# 引入包



'''
思路：
1、多循环结构，大循环控制大周期，小循环控制小周期
2、分别设置5%，10%，15%三个循环，卖出价在此基础上加5%
3、买入与卖出总是成对出现，要设置买入，就要同时设置卖出，否则既不买入也不卖出
4、价格保留2位小数
5、买入与卖出，分别设置五档
'''

#小循环
# for i in range(6):
#     # print(round(1.86*(1-0.15)**i,2))
#     print(round(1.86 * (1+0.10)**i,2))

#大循环
# for i in range(6):
#     print(round(1.39*(1-0.05)**i,2))
    # print(round(1.39 * (1+0.10)**i,2))


mdx_deal_price=1.7
knc_deal_price=2.00

# mdx_stock_in_hold=100
# knc_stock_in_hold=125
#
#
# #高点，梯度要大，低点梯度要小，最小梯度为
#
# default_step=0.1
# transaction_index=0.5
# buy_in_index=1-transaction_index
# sale_out_index=transaction_index
#
# buy_in_price=2.24*(1-default_step)*buy_in_index
#
# print(buy_in_price)

#买入梯度15%
#卖出梯度20%


def buy_and_sale_price(input_price):
    print(round(input_price*0.85,2))
    print(round(input_price*1.2,2))





if __name__ == "__main__":
    buy_and_sale_price(mdx_deal_price)
    buy_and_sale_price(knc_deal_price)
    pass
