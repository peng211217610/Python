#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''截图功能汇总'''


'''
备注：Python可以调用windows API实现屏幕截图，特点是截图时间快。操作繁琐，需要的用的时候上网查。
'''


#引入相关包
# pythonPath = r'D:\TDdownload\Document\Python'
# import os,sys,time
# sys.path.append(pythonPath)
# import configure as cfg
#
# from PIL import ImageGrab
#
# im = ImageGrab.grab((0,0,0+1000,0+1000))
#
# #打开图片
# im.show()
#
#
# #保存图片
# im.save('dir')
#
#
#
#
# clip = ImageGrab.grabclipboard()

from PIL import ImageGrab

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (760, 0, 1160, 1080)
im = ImageGrab.grab(bbox)

# 参数 保存截图文件的路径
im.save('777as.png')






if __name__=="__main__":
    pass