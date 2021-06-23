#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg

import unittest
from selenium import webdriver

class googleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def testPageTitle(self):
        self.driver.get('http://www.google.com')
        self.assertIn('Google',self.driver.title)

if __name__=="__main__":
    unittest.main(verbosity=2)