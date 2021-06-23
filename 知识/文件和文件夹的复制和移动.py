#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''文件和文件夹的复制和移动'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg


#使用的模块是shutil
import shutil

#复制文件到文件，如果dst是文件夹，表示文件不改名
shutil.copyfile(src,dst) #复制源文件src到目的文件dst，注意，src和dst都是带文件


#复制文件到文件夹
shutil.copy(src,dst_dir) #dst_dir表示目的目录


#复制文件夹到文件夹*****注意：dst_dir目录必须是不存在的目录（即最后一级目录不存在）
shutil.copytree(src_dir, dst_dir)


#移动文件
shutil.move("C:\\a\\1.txt","C:\\b")
#移动文件夹
shutil.move("C:\\a\\c","C:\\b")


#重命名文件
shutil.move("C:\\a\\2.txt","C:\\a\\new2.txt")
#重命名文件夹
shutil.move("C:\\a\\d","C:\\a\\new_d")

#删除文件，用os库
os.remove(os.path.join(root, name))
os.unlink("C:\\b\\1.txt")

#删除文件夹
shutil.rmtree(os.path.join(root, dir_name))
#如果文件夹是空的，可以用下面的方法，不为空则会报错
os.rmdir("C:\\b\\new_a")

#新建文件
os.mkdir('dir')


# if __name__ == "__main__":
#     pass