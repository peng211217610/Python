#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''Linux上运行获取内容'''


import time


while True:
    nowTime = time.localtime()
    with open('/proc/meminfo',encoding='utf8') as f:
        content = f.read()
        List = content.splitlines()
        print(List)
        memDict = {}
        for one in List:
            itemName = one.split(':')[0]
            itemsize = int(one.split(':')[1].replace('kB','').strip())
            memDict[itemName] = itemsize
        MemTotal = memDict['MemTotal']
        MemFree = memDict['MemFree']
        Buffers = memDict['Buffers']
        Cached = memDict['Cached']
    MemAvailable = MemFree + Buffers + Cached
    avaMem = round((MemAvailable / MemTotal),2)*100
    with open('/home/ret.txt','a',encoding='utf8') as f:
        f.write('%s\t%d%%\n' % (time.strftime('%Y%m%d_%H:%M:%S',nowTime),avaMem))
    time.sleep(5)
















