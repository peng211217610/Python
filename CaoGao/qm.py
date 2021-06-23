#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''编程可能会考的题目'''


#1
'''
给定a，b的值，a=3，b=5，然后交换两个数字的值并输出。
'''
a=3
b=5
c=[a,b]
a=c[1]
b=c[0]
print(a,b)


#2
'''
一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，如何通过编程来求解？请编程计算并输出结果。
'''
def cal_interger():
    for a in range(0,1000000):
        x = (a + 100) ** 0.5
        y = (a + 268) ** 0.5
        if str(x).split('.')[1] == '0' == str(y).split('.')[1]:
            print(a)


#3
'''
判断101到200之间有多少个素数，并输出所有素数
'''
def cal_prime():
    alist = []
    blist = []
    for a in range(101,201):
        for b in range(2,int(a/2)+1):
            if a%b == 0:
                if a not in alist:
                    alist.append(a)
        if a not in alist:
            blist.append(a)
    print(blist)


#4
'''
编程求1!+2!+3!+4!+......+50!的值，并输出结果
'''
def cal_sum_factorial(n):
    alist = []
    b=1
    for a in range(1,n+1):
        b = b*a
        alist.append(b)
    print(sum(alist))



if __name__=="__main__":
    cal_interger()
    cal_prime()
    cal_sum_factorial(50)
    pass