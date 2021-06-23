#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''计算亏损金额'''

'''
思路：
当前价格乘以1-步长，得到一个末期值，
该值与最终价格进行比较，若小于，则本次操作不会发生，若大于，则本次操作会发生
若操作发生，则需要知道，本次是第几次发生

本次成交，获取持股数，增持或减持数，成交价，出价和入价，
以日期为key，以当天最高最低为元组，构成一个字典。
重点是需要获取到下一次，是出点还是入点，首先以日期递增进行对比
该日期下的元组区间是否包含预期的出点和入点
如果包含，那么判断是出点或者入点。
接着求出，增持或减持数
如果本次的出入类型与上次相同，则如果为入型，金额递增1000，如果为出型，则本次出的股数与上上次买入数相同（意味着每次成交股数要作为一个列表）
如果出入类型相反，先入后出，出的股数与入的股数相同。如果先出后入，需要找到最近一次入的金额加上1000


持股数sum_stock(整数类型)

盈利20%卖出是指初始投入的20%，即3000*20%=600


'''


'''
股票数据
'''
# stock_weekly={
#     "20200717":(11.39,9.25),
#     "20200718":(10.45,9.35),
#     "20200719":(9.74,9.26),
#     "20200720":(10.18,9.35),
#     "20200721":(9.64,8.96),
#     "20200722":(9.41,9.08),
#     "20200723":(9.46,9.10),
#     "20200724":(9.41,8.72),
#     "20200725":(9.13,8.45),
#     "20200726":(9.73,8.54),
#     "20200727":(8.82,8.14),
#     "20200728":(8.22,8.02),
#     "20200729":(8.25,8.10),
#     "20200730":(8.39,8.15),
#     "20200731":(8.29,8.05),
#     "20200732":(8.18,7.91),
#     "20200733":(8.00,7.74),
#     "20200734":(8.10,7.93),
#     "20200735":(8.17,7.93),
#     "20200736":(8.16,7.97),
#     "20200737":(8.25,8.04),
#     "20200738":(8.16,7.60),
#     "20200739":(7.95,7.56),
#     "20200740":(7.79,7.32),
#     "20200741":(7.40,7.22),
#     "20200742":(7.40,6.78),
#     "20200743":(6.95,6.59),
#     "20200744":(7.16,6.73),
#     "20200745":(7.03,6.65),
#     "20200746":(6.89,6.40),
#     "20200747":(6.58,6.39),
#     "20200748":(6.98,6.64),
#     "20200749":(7.12,6.87),
#     "20200750":(7.33,6.92),
#     "20200751":(7.44,6.82),
#     "20200752":(6.83,6.50),
# "20200753":(7.00,6.50),
# "20200754":(7.44,7.29)
# }

# for one in range(35):
#     total=20200717+one
#     print('"%d"' % total +':'+'()'+',')




'''
假定初始成交价11.39，投入金额3000元
本次成交数据
成交数量=金额除以100再除以价格，取整，再乘以100
'''






'''
所有入的股，都要写在一个列表中，直到其中的所有股全清掉
'''



# stockList = []
# stockList.append(exchange[3])


with open(r'D:\TDdownload\600094.csv','r',encoding='utf-8') as f:
    content=f.read()
    # print(content)
    mycontentlist=content.splitlines()
    del mycontentlist[0]
    stock_weekly={}
    mycontentlist.reverse()
    for one in mycontentlist:
        #这是概念板块
        # high=float(one.split(',')[5])
        # low=float(one.split(',')[6])
        #这是股票
        high = float(one.split(',')[4])
        low = float(one.split(',')[5])
        up_down_tuple=(high,low)
        tr_date=one.split(',')[2]
        stock_weekly[tr_date]=up_down_tuple


# print(stock_weekly)















#引入相关包
def kuisun(ori_amount,step_amount,ori_price,step_price,begin_date,end_date):
    '''
    :param ori_amount: 初始金额
    :param step_amount: 每次比上次多多少金额
    :param ori_price: 第一次成交价格
    :param begin_date: 区间开始日期
    :param end_date: 区间结束日期
    :param step_price: 每次比上次下降多少百分比
    :param min_huiben_price: 要想回本，至少要达到的价格
    :return: 返回最终亏损了多少金额
    '''
    exchange = ("入",ori_price,begin_date,int(round(ori_amount / 100 / ori_price,2)) * 100,ori_amount)
    exchangeList = []
    exchangeList.append(exchange)
    # 持股数
    sum_stock = exchange[3]
    # 最近成交日期
    max_deal_date = exchange[2]

    # 下次出入价格
    next_up = round(exchange[1] * (1 + step_price),2)
    next_down = round(exchange[1] * (1 - step_price),2)
    final_price = stock_weekly[str(end_date)][-1]
    for one in stock_weekly.keys():
        #只取在开始日期和结束日期之间的数据
        if begin_date<=int(one)<=end_date:
            stockinList = []
            amountinList = []
            net_in = 0
            if int(one) > max_deal_date:
                # print(max_deal_date)
                for two in exchangeList:
                    if two[0] == "入":
                        stockinList.append(two[3])
                        # amountinList.remove(two[4])
                        net_in += 1
                    else:
                        # stockinList.remove(two[3])
                        del stockinList[-1]
                        # amountinList.append(two[4])
                        net_in -= 1
                # print(stockinList)
                del stockinList[0]
                # print(stockinList)
                #不考虑跳空高开，低开的情况。就是说当天的最低点比预期的最高点还高，或者最高点比预期的最低点还低。
                #为了简化计算，如果预期的高点，不落在区间内，即区间最小值大于预期，按预期值计算（这么处理是错误的，但是仅仅为方便计算）
                if stock_weekly[one][1] <= next_up <= stock_weekly[one][0] or next_up<= stock_weekly[one][1]:
                    #如果该股没有跌过，即exchangeList只有1条记录，则不卖出
                    if len(stockinList) > 0:
                        # print(type(stockinList))
                        # 如果是出，则一定是将股数最大的出掉(这是对于不对买入金额做限制的情况)
                        #由于如果本次买入金额为6000，本本次实际不买入，所以，出的话，先要将买入股数为0的先出掉
                        #上面注释作废，改为出是将stockinList最后一个记录出掉
                        # stockinList.reverse()
                        # for i in stockinList:
                        #     if i==0 or i == max(stockinList):
                        exchange = ("出",next_up,int(one),stockinList[-1],0)
                        stockinList.pop()
                        exchangeList.append(exchange)
                        max_deal_date = int(one)
                                # break
                        # stockinList.reverse()
                    #如果该股涨加仓和减仓次数相等，即净买入为1次（net_in=0），希望的效果是上涨20%全部卖出再以最高点下跌10%时再次建仓。但是这个太难写，
                    #简化为净买入net_in=0时，在这个卖出点的位置，以相同价格买入1000元
                    else:
                        exchange = ("入",next_up,int(one),int(round(step_amount / 100 / next_up,2)) * 100,step_amount)
                        exchangeList.append(exchange)
                #这里使用if代表当天挂一次卖出，挂一次买入。不考虑多次买入卖出的情况。如果是esif代表要么挂买要么挂卖。
                if stock_weekly[one][1] <= next_down <= stock_weekly[one][0] or next_down>=stock_weekly[one][0]:
                    # 如果是入，要计算出第一次入和本次入之间有几个出几个入
                    ready_amount = (net_in - 1) * step_amount + step_amount if net_in<=5 else 1*step_amount
                    exchange = ("入",next_down,int(one),int(round(ready_amount / 100 / next_down,2)) * 100,ready_amount)
                    max_deal_date = int(one)
                    exchangeList.append(exchange)
                next_up = round(exchange[1] * (1 + step_price),2)
                next_down = round(exchange[1] * (1 - step_price),2)
                # print(stockinList)

    [print(one) for one in exchangeList]
    # print(stock_weekly.keys())
    # total_kui = 0
    total_in_amount = 0
    total_out_amount = 0
    amount_in_list=[]

    # 计算亏损金额，计算方法：假定没有任何卖出，那么最终价格减去买入价格，乘以数量，就是本次操作最终亏损金额
    # 但实际上，卖出是存在的，这比卖出已经不产生亏损，所以实际上买入的计算重复计算了卖出后到最终价格之间的亏损，所以要把这部分扣除
    # 第一次买入的单独计算盈亏
    total_kui = round((final_price - exchangeList[0][1]) * exchangeList[0][3],2)
    # print(total_kui)
    del exchangeList[0]

    sum_other_kui=0
    # print(exchangeList)
    net_in=0
    for one in exchangeList:
        if one[0] == "入":
            # kui_amount = round((final_price - one[1]) * one[3],2)
            in_amount = -int(one[1] * one[3])
            in_stock = one[3]
            # amount_in_list.append(in_amount)
            # print(in_amount)
            net_in+=1
        else:
            #卖出的盈利计算跟最终价格无关，跟买入时的价格相关
            # kui_amount = round((one[1] - final_price) * one[3],2)
            in_amount = int((one[1] * one[3]))
            in_stock = -one[3]
            # total_out_amount += out_amount
            # amount_in_list.append(out_amount)
            net_in -= 1
        # print(in_amount)
        sum_other_kui += in_amount
        total_kui += in_amount
        sum_stock += in_stock

    if net_in !=0:
        print("出入数不相等")
    # print(stockinList)
    # 累计盈亏
    print(total_kui)

    # 除初始投入之外的盈亏
    print(sum_other_kui)

    # print(amount_in_list)

    # print(sum(amount_in_list))

    # 最终总投入资金
    # final_amount = total_in_amount
    # print(int(final_amount))

    # 总取出资金
    # print(int(total_out_amount))

    # 最终账上可见余额
    # print(int(sum_stock*final_price))


'''
待解决事项
1、每次都计算当前总投入金额，本次投入+前期投入（累计盈亏的相反值）大于20000，跳过买入步骤（换个思路：买入金额最大不超过5000）
1、每次在卖出点，在卖出前，判断盈利是否已大于20%，即累计盈亏>（初始买入价*数量*20%），满足条件，只保留初始买入量，其他持有量按当前价格全部卖出
'''












if __name__=="__main__":
    # kuisun(3000,1000,16.75,0.06,20100930,20210219)
    # kuisun(3000000,1000000,1254.202,0.05,20150105,20210315)
    kuisun(3000,1000,7.99,0.10,20150105,20210315)
    pass