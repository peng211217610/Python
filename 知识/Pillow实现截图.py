#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''截图功能汇总'''


'''
备注：Python可以调用windows API实现屏幕截图，特点是截图时间快。操作繁琐，需要的用的时候上网查。
'''


#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg

from PIL import ImageGrab

im = ImageGrab.grab((0,0,0+1000,0+1000))

#打开图片
im.show()


#保存图片
im.save('dir')




clip = ImageGrab.grabclipboard()








if __name__=="__main__":
    pass