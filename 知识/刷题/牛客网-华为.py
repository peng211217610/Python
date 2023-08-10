#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark=''''''

# 引入包



#HJ4 字符串分隔


# a=int(input())
mlist=[]
for i in range(1):
    x,y='0 3'.strip().split()
    mlist.append((x,int(y)))
mdict1={}
for i in mlist:
    if i[0] not in mdict1.keys():
        mdict1[i[0]]=i[1]
    else:
        mdict1[i[0]]+=i[1]
mdict2={}
for i in sorted(mdict1.keys()):
    mdict2[i]=mdict1[i]
for i in mdict2.keys():
    print(i,'',mdict2[i])





















































if __name__=="__main__":
    pass
