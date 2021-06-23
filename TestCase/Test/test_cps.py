#!/usr/bin/python3
# -*- coding:utf-8 -*-
#定义变量

#--------------------------------------------------打一个断点
# print('hello world')
# m=1
# while m < 10:
#       print('OK')
#       m+=1
#       if m==10:
#          print("hello")
#       else:
#          print('wocao')
#--------------------------------------------------while类型，满足10到12岁的女性录取，其他不录取，并统计最终符合条件的人数
# n=1
# sum=0
# while n <= 2:
#       a=input('Please enter gender,M or F:')
#       b=int(input('age:'))
#       n+=1
#       if a=='F' and 10<=b<=12:
#          print('Welcome to the team')
#          sum+=1
#       else:
#          print('sorry')
# print(sum)
#--------------------------------------------------日期和时间格式化输出的方法小结
import datetime
now=datetime.datetime.now()
print(now.strftime('%a'))         #%a 输出当前是星期几的英文简写
print(now.strftime('%A'))         #%A 输出完整的星期几名称英文
print(now.strftime('%b'))         #%b 输出月份的英文简写
print(now.strftime('%B'))         #%B 输出月份的英文完整名称
print(now.strftime('%c'))         #%c 以本地时间显示日期和时间
print(now.strftime('%d'))         #%d 显示1-31之间的数，每月的第几天，也就是年月日中的日
print(now.strftime('%H'))         #%H 以24小时制显示小时，比如，02,14
print(now.strftime('%I'))         #%I 以12小时制的方式显示当前小时
print(now.strftime('%j'))         #%j 显示当前日期为一年中的第几天
print(now.strftime('%m'))         #%m 显示1-12之间的月份
print(now.strftime('%M'))         #%M 显示00-59之间的分钟数
print(now.strftime('%p'))         #%p 以 A.M./P.M.方式显示是上午还是下午
print(now.strftime('%S'))         #%S 显示0-59之间的秒数
print(now.strftime('%U'))         #%U 显示一年中的第几周，星期天为一周的第一天
print(now.strftime('%w'))         #%w  显示一周中的第几天，其中星期天为0，星期一为1
print(now.strftime('%W'))         #%W 显示一年中的第几周，和U%把不同的是星期一为一周的第一天
print(now.strftime('%x'))         #%x 显示当地的日期
print(now.strftime('%X'))         #%X 显示当地的时间
print(now.strftime('%y'))         #%y 显示(00 - 99) 之间的年份,2013年则显示结果为13
print(now.strftime('%Y'))         #%Y 显示完整年份，如2013
print(now.strftime('%%'))         #用于显示%符号
print(now.strftime('%z'))         #%z, %Z 输出时区，如果不能显示，则显示为空字符
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  #显示当前日期时间：格式为：年-月-日 时:分:秒
#--------------------------------------------------打一个断点




















































