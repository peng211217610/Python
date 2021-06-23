#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''

阅读下面的两个知识点

1. ffmpeg可以用下面的参数来录制Windows 桌面操作的视频。

ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop 
-c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "fffffffffffffffff"

其中 fffffffffffffffff 部分 是需要填入 产生的视频文件名。

录制过程中，用户按键盘 q 键，可以退出录制。


2. ffmpeg还可以用来合并视频文件，windows下面的格式如下

ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4

其中concat.txt 是要合并视频的文件列表。格式如下，每行以file 开头 后面是要合并的视频文件名：

file 20170330_110818.mp4
file 20170330_110833.mp4



------------------------------
下载ffmpeg程序 (进入 http://ffmpeg.zeranoe.com/builds/ 点击 Download FFmpeg按钮即可)

要求大家写一个python程序，运行后提示用户是要做什么操作，如下
 '请选择您要做的操作：1：录制视频，2：合并视频：'
 
 如果用户输入1并回车， 则调用ffmpeg录制视频文件，产生在当前目录下面。
 要求录制的视频文件名 是当前时间（年月日_时分秒.mp4格式），
 比如 '20170330_093612.mp4' （怎么产生这种时间格式的字符串，不知道的请自行网上搜索方法）
 
 如果用户输入2并回车，则按字母顺序列出当前目录下所有的 mp4为扩展名
 的视频文件(怎么列出，请自行网上搜索方法)，并在前面编上序号。如下所示
 
 ---------------------------------
    目录中有这些视频文件：
    1 - 20170329_202814.mp4
    2 - 20170330_093251.mp4
    3 - 20170330_093612.mp4

    请选择要合并视频的视频文件序号(格式 1,2,3,4) : 
 ---------------------------------    

 用户输入视频序号（序号以逗号隔开）后， 程序合并视频文件， 输出的合并后视频文件名 固定为 out.mp4

'''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys,time
sys.path.append(pythonPath)
import configure as cfg

#定义时间类
class myTime:
    className = 'myTime'

    def mytime(self,output_format='%Y%m%d%H%M%S',input_time=time.localtime()):
        return time.strftime(output_format,input_time)

nowTime = myTime().mytime('%Y%m%d_%H%M%S')


Obj = input('请选择您要做的操作：1：录制视频，2：合并视频：')


i = 1

if Obj == '1':
    os.system('C:\\Myprograms\\V-工具\\ffmpeg\\bin\\ffmpeg.exe -y -rtbufsize 100M -f gdigrab \
        -framerate 10 -draw_mouse 1 -i desktop \
        -c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "D:\\TDdownload\\%s.mp4"' % nowTime)
elif Obj == '2':
    AllFile = sorted(os.listdir('D:\\TDdownload'))
    #print(AllFile)
    #将mp4文件名按行写入mp4List.txt文件中
    with open('D:\\TDdownload\\mp4List.txt','w+',encoding='utf8') as ct:
        for one in AllFile:
            if os.path.isfile('D:\\TDdownload\\%s' % one):
                if one[-4:] == '.mp4':
                    ct.write(str(i) +' - ' + one+'\n')
                    i += 1
        #print(i)
        #列出MP4文件供使用者选择
        ct.seek(0)
        if ct.read() == '':
            print(ct.read())
            print('这是一个空文件')
            sys.exit(3)
        else:
            ct.seek(0)
            print(ct.read())
            ct.seek(0)
            ct_content = ct.read().splitlines()
            #print(ct_content)

    item = input('请选择要合并视频的视频文件序号(格式 1,2,3,4) :')
    # try:
    #     #对输入内容整理格式
    #     itemList = []
    #     if item.find(',') == -1:
    #         print('只选了一个文件，无需合并！')
    #         itemList.append(item)
    #         sys.exit(1)
    #     else:
    #         for i in item.split(','):
    #             value = i.strip()
    #             itemList.append(value)
    #     goalList = []
    #     for j in itemList:
    #         if j in map(str,range(len(ct_content)+1)):
    #             goalList.append(j)
    #         else:
    #             print('该输入值有误，请检查！')
    #     if len(goalList) == 0:
    #         print('输入内容没有合法值，请重新选择')
    #         sys.exit(3)
    #     elif len(goalList) == 1:
    #         print('需要合并的文件数只有1个，无需合并')
    #         sys.exit(2)
    #     else:
    #         print(goalList)
    #         print(ct_content)
    #             with open('D:\\TDdownload\\concat.txt','w+',encoding='utf8') as concat:
    #             for x in goalList:
    #                 for y in ct_content:
    #                     if x == y[:len(x)]:
    #                         concat.write('file'+' '+"'%s'" % y[len(x)+3:]+'\n')
    #                 else:
    #                     continue
    #             concat.seek(0)
    #             print(concat.read())
    #             concat.seek(0)
    #     os.chdir(r'D:\\TDdownload')
    #     os.system('C:\\Myprograms\\V-工具\\ffmpeg\\bin\\ffmpeg.exe -f concat -i "D:\\TDdownload\\concat.txt" -codec copy "D:\\TDdownload\\out.mp4"')
    # except Exception as e:
    #     print(e)
else:
    print('Wrong Input,Please input 1 or 2!')

if __name__ == "__main__":
    pass