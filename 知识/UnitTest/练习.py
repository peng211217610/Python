#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''练习unittest的使用'''

#变量
pythonPath = r'D:\TDdownload\Document\Python'


#引入相关包
import os,sys,time
sys.path.append(pythonPath)
from configure import *
from random import randint
import unittest



class unittest_test(unittest.TestCase):

    def setUp(self):
        self.url = 'http://acc.mof.gov.cn/'
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(self.url)
        driver.execute_script("arguments[0].click()",driver.find_element_by_xpath('//div[@id="XXCX"]/div/a[1]'))

    def test_condition1(self):
        driver.execute_script("arguments[0].click()",driver.find_element_by_id('cpaDivision'))
        driver.find_element_by_xpath('//select[@id="cpaDivision"]/option[@value="620000"]').click()
        self.assertEqual(1,1)

    def test_condition2(self):
        driver.find_element_by_xpath('//div[@id="index_main"]/following-sibling::div[1]/div[1]//input').send_keys('5566')
        self.assertEqual(1,1)

    def test_condition3(self):
        driver.find_element_by_xpath('//div[@id="index_main"]/following-sibling::div[1]/div[1]/div[1]/div[3]//input').send_keys('陈庆炎')
        self.assertEqual(1,1)

    def tearDownc(self):
        driver.execute_script("arguments[0].click()",driver.find_element_by_xpath('//div[@id="index_main"]/following-sibling::div[1]/div[1]/a'))
        record_number = driver.find_element_by_id('recordTotals').text
        print(record_number)
        driver.close()


# def suite():
#     tryTestCase = unittest.makeSuite(unittest_test,'test')
#     return tryTestCase








if __name__=="__main__":
    #suite()
    # 在main()中加verbosity参数，可以控制输出的错误报告的详细程度
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)