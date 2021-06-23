#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg
import time

target_dir = '/Users/swa/backup'

#之所以用列表是为了将多个文件打包
source = ['/Users/swa/notes']

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

if os.system(zip_command) == 0:
    print('Success!')
else:
    print('Failed!')


if __name__ == "__main__":
    pass