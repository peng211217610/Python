

#
#
# print('hello')

# print(3+'tom')
# # print('tom'+3)

# print('name is' + 'tom')
# print('name is','tom')
#
# str1 = 'name is tom'
# print(len(str1))
# print(str1[0])
#
# print(str1[len(str1)-1])
#
# print(str1[5:7])
#
# print(str1.index('i'))
#
# print(str1[-18:-15])
# print(str1[::-1])

# alist = []
# print(type(alist))
#
# alist=[100,3.14,'abc']
# print(alist[1])
# alist[1]=200
# print(alist)
# alist[8]=200
# print(alist)

#
# a = ['this', 'test', 4.56, ['inner', 'list']]
# print(a[1][2])
#
# print(type(True))
#
#
# score = input('please input')
# print(type(int(score)))
#
#
#

# def func():
#     print('step1')
#     print('step2')
#
#
# print(max(11,12,13))
# print(max([11,12,13]))
# print(max((11,12,13)))
#
# print(type(func()))
#
#
# def t2(para):
#     para=3
# b=[1]
# t2(b)
# print(b)
#
#



#
# def getName(srcStr):
#     #获取指定字符串后半部分
#     delBefore = srcStr[srcStr.find('the name is'):]
#     #获取指定字符串+姓名
#     delAfter = delBefore.split(',')[0]
#     #以空格为分隔符获取列表并获取列表第4个元素（姓名）
#     Name = delAfter.split(' ')[3]
#     return Name
#
# srcStr = 'A girl come in, the name is Jack, level 955;'
# getName(srcStr)   #调用函数
#
# print(getName(srcStr))   #打印出函数值
#

#
# name = 'tom'
# age = 18
# print('name is %s' % (name,))
# print('name is %s,age is %s' % (name,age))
#
# print('%6d' % 56)
#
# print('%0.6f' % 3.14145)
#
# start = 0
# sumData = 0
# while start <=100:
#     sumData += start
#     start += 1
# print(sumData)
#


# filename = r'D:\TDdownload\Document\Python\test\file_object\test.txt'
# fo = open(filename,'r')
# # file_object.close()
# fo.read().splitlines()
# print(fo.tell())



#乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}'.format(j,i,i*j),end='\t')#制表用\t可以解决字符宽度不一致的问题
#     print()

#[3,5,7,2,0],作业，将其升序或降序排列

# import sys
# print(sys.path)

import time
now = time.strftime('%Y-%m-%d %H:%M:%S')
print(now)


try:
    500/0
except ZeroDivisionError:
    print('input can not be 0!'
except ValueError:
    print('输入值不是int')

import traceback








































