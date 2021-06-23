#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''testing'''


#引入相关包
from selenium import webdriver
import json


def testing():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')
    ele_input = driver.find_element_by_css_selector('#kw')
    ele_input.clear()
    ele_input.send_keys('python')
    try:
        ele_enter = driver.find_element_by_css_selector("*[class='bg s_btn_wr'] #su").click()
    except:
        print('find element failed')
    time.sleep(3)
    driver.quit()


def transfer_url_string_to_params(str):
    output={}
    paramsList = str.split('&')
    for one in paramsList:
        left_right=one.split('=')
        output[left_right[0]]=left_right[1]
    json_str=json.dumps(output)
    new_json_str=json_str[1:-1]
    si=new_json_str.replace(': ',':').replace(',',', \n')
    # print(si)
    return si



# data = {"ret":0,"version":"10.1.28.676"}






if __name__=="__main__":
    transfer_url_string_to_params('thunderPid=11111&sign=f1bd42598d63f741eb48dbcaa8704e5a')
    # testing()