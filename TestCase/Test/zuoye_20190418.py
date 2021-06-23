#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

'''
登录 51job ，
http://www.51job.com

输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉）， 
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息

Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg

from selenium import webdriver

#不打开浏览器测试
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)


#driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.51job.com/')

#定位输入框，清理掉内容后输入关键词
ele = driver.find_element_by_id('kwdselectid')
ele.clear()
ele.send_keys('python')

#定位地址，会弹出一个弹窗
driver.find_element_by_id('work_position_click').click()

#注意，打开弹窗，通常需要设置一个等待时间，等待弹窗打开
time.sleep(3)
ele_area = driver.find_element_by_id('work_position_click_multiple_selected')
ele_cityList = ele_area.find_elements_by_class_name('ttag')

#判断ele_cityList是否为空列表
if ele_cityList != []:
    for one in ele_cityList:
        one.click()

#选择杭州并点击
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

#点击确定
driver.find_element_by_id('work_position_click_bottom_save').click()
time.sleep(3)

#关闭弹窗后定位到搜索按钮，并点击
driver.find_element_by_css_selector('.ush button').click()


#挑转到新页面，定位搜索结果元素，赋值给变量，方便后续操作,查询列表是ele_resultList里面的class为el，且没有title的元素
ele_resultList = driver.find_element_by_id('resultList').find_elements_by_css_selector('.el')[1:]

for one in ele_resultList:
    jobName = one.find_element_by_css_selector('.t1 a').text
    companyName = one.find_element_by_css_selector('.t2 a').text
    jobAddr = one.find_element_by_css_selector('.t3').text
    salary =  one.find_element_by_css_selector('.t4').text
    releaseTime = one.find_element_by_css_selector('.t5').text
    out_putList = [jobName,companyName,jobAddr,salary,releaseTime]
    print('|'.join(out_putList))


driver.quit()

















