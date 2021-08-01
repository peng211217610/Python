#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = ''''''

#引入相关包
from Function.Common.function_common import  *
from Function.Common.function_common import *


all_values_list=CSV().get_all_values_from_csv('pro_bar')





#收盘点数
close_dian=[one.split(',')[3] for one in all_values_list]



for i in range(len(close_dian)):
    close_dian[i]=float(close_dian[i])
# print(close_dian)


# print(max(close_dian))#5166.35
# print(min(close_dian))#1950.013


#最近一年平均点位
time_and_dianwei=[(int(one.split(',')[2]),float(one.split(',')[3])) for one in all_values_list]


need_dian=[i[1] for i in time_and_dianwei if i[0] >20200312]

# for i in time_and_dianwei:
#     print(type(i[0]))
#     if i[0]<20200312:
#         time_and_dianwei.remove(i)
#         # del time_and_dianwei[i]
print(need_dian)





print(len(need_dian))
print(round(sum(need_dian)/len(need_dian)))



if __name__=="__main__":
    pass