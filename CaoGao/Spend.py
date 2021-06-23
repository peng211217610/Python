#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = ''''''

'''
# 北京地铁规定, 
# 消费满100元,下次开始打8折 
# 消费满150元,下次开始打5折 
# 累计消费400元之后,不在打折 
# 每个月消费额度自然清零 
# 问题:我每天坐地铁,往返要花12块,一个月上22天班.问我一个月要花多少钱? 
'''
#引入相关包

def spend():
    sum = 0
    initial_average_spend = round((12 / 2),2)
    for i in range(1,45):
        # print(i)
        if sum<=100:
            sum+=initial_average_spend
        elif 150>=sum>100:
            second_average_spend=round((12/2)*0.8,2)
            sum += second_average_spend
        elif 400>=sum>150:
            third_average_spend=round((12/2)*0.5,2)
            sum += third_average_spend
        else:
            sum += initial_average_spend
    return sum

#方法二
def spend_2():
    sum = 0
    initial_average_spend = round(12 / 2)
    i=1
    while i <=44:
        # print(i)
        if sum<=100:
            sum+=initial_average_spend
        elif 150>=sum>100:
            second_average_spend=round((12/2)*0.8,2)
            sum += second_average_spend
        elif 400>=sum>150:
            third_average_spend=round((12/2)*0.5,2)
            sum += third_average_spend
        else:
            sum += initial_average_spend
        i += 1
    return sum









if __name__=="__main__":
    print(spend())
    print(spend_2())
    pass