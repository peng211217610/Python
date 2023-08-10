#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark=''''''

# 引入包
'''
找出两个字符串中最大公共子字符串，如"abjeccarde"，"sjdgcargde"的最大子串为"car"
'''

str1='''abjeccarde'''
str2='''sjdgcargde'''

# def Solution(str1,str2):
#     for i in range(len(str1)):
#         for j in range(len(str1)-1,1,-1):
#             # print(str1[i:j])
#             if str1[i:j] in str2:
#                 print(str1[i:j])
#                 break
# xxx=True
# for i in range(len(str1),0,-1):
#     for j in range(0,len(str1)-i):
#         if str1[j:j+i] in str2:
#             print(str1[j:j+i])
#             xxx=False
#             continue
#     if xxx==False:
#         break



# while True:
#     try:
#         slist=input().split()
#         stra=slist[0]
#         strb=slist[1]
#         a,b=float(stra),float(strb)
#         if a==b:
#             print('YES')
#         else:
#             print('NO')
#     except:
#         break

strs='''abcdefg'''
print(strs[::-1])




























if __name__=="__main__":
    # Solution(str1 , str2)
    pass
