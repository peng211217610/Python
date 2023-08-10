#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''生成ini配置文件'''

#引入包
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'aaa':'1',
    'bbb':2
}














if __name__=="__main__":
    pass