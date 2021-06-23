#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''使用Beautifulsoup解析HTML'''

'''
打开百度新歌榜， http://music.baidu.com/top/new

在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者
 
注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉

最终结果显示的结果如下：
我不能忘记你       :  林忆莲
等                :  严艺丹
飞天              :  云朵
粉墨              :  霍尊
春风十里不如你     :  李健

'''
#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get('http://music.baidu.com/top/new')

try:
    ele = driver.find_element_by_id('songListWrapper')
    ele2 = ele.find_elements_by_tag_name('li')
    for one in ele2:
        ele_up = one.find_element_by_css_selector('.status > i').get_attribute('class')
        #print(ele_up)
        if ele_up == 'new':
            songTitle = one.find_element_by_css_selector('.song-title > a').text
            #把括号后面的标签去掉
            idx = songTitle.find('（')
            if idx != -1:
                songName = songTitle[:idx]
            else:
                songName = songTitle
            songSinger = one.find_element_by_css_selector('.singer a').text
            print('{0:{1}<30}:\t{2}'.format(songName,chr(12288),songSinger))
    #print(ele.text)
except:
    print('get element failed!')
finally:
    driver.quit()


