#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''访问天气查询网站（网址如下），查询江苏省天气'''

'''
Selenium 作业 1

请到如下网址下载最新Chrome浏览器 的 webdriver 驱动
https://chromedriver.storage.googleapis.com/index.html

pip 安装Selenium Web driver Python 客户端库
1. 访问天气查询网站（网址如下），查询江苏省天气 
http://www.weather.com.cn/html/province/jiangsu.shtml

2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如 
温度最低为12℃, 城市有连云港 盐城 
'''

from selenium import webdriver

driver = webdriver.Chrome(r'D:\TDdownload\Document\Python\chromedriver.exe')

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

driver.implicitly_wait(10)

ele = driver.find_element_by_id('forecastID')

itemList = ele.text.split('℃\n')

#print(itemList)
cityTem = {}
for one in itemList:
    idx = one.find('/')#找到字符串中/的索引位置，获取/前面部分，写入到新列表
    newValue = one[:idx].replace('℃','')
    cityName = newValue.split('\n')[0]
    lowTem = int(newValue.split('\n')[1])
    cityTem[cityName] = lowTem
#print(cityTem)
temp = sorted(cityTem.values())
cityList = []
lowestTemp = temp[0]                #第一个元素一定是气温最低的
#遍历所有城市，如果键值等于最低气温值，将键名写入到城市列表
for item in cityTem.keys():
    if cityTem[item] == lowestTemp:
        cityList.append(item)

print(cityList)

driver.quit()

