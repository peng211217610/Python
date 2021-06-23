#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''测试'''

#引入相关包
from Config.common_variable import *
from Function.Common.function_common import *
# from Function.Common.function_init_webdriver import *
from selenium import webdriver

driver=webdriver.Firefox()


def west_test():
    driver.get('https://aq.yy.com/p/reg/mobile.do')
    time.sleep(10)
    # driver.find_element_by_css_selector('#select_result').click()
    driver.find_element_by_xpath('//span[@id="select_result"]/em').click()
    eles=driver.find_elements_by_css_selector('#selectOption li')
    codelist=find_out_all_value(eles,'data-node-value')
    valuelist=find_out_all_value(eles)
    print(codelist,valuelist)
    driver.quit()









if __name__=="__main__":
    west_test()
    pass