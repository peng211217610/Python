#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''移动端自动化练习'''

#变量


#引入相关包
import time
from Function.Common.function_init_appiumdriver import *

# driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
# driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys()

driver.find_element_by_android_uiautomator('new UiSelector().text("武汉晴川学院")').click()
# els1 = driver.find_elements_by_android_uiautomator("new UiSelector().text(\"武汉晴川学院\")")
# els1[1].click()

# driver.find_element_by_id('my_home_page').click()

# els1 = driver.find_elements_by_android_uiautomator("new UiSelector().text(\"武汉晴川学院\")")
# els1[2].click()


els1=driver.find_elements_by_id('com.chaoxing.mobile:id/tv_title')
els1[1].click()

driver.find_element_by_android_uiautomator("new UiSelector().text(\"健康日报\")").click()

time.sleep(2)
def getSize():                               #获取当前的width和height的x、y的值
    x = driver.get_window_size()['width']   #width为x坐标
    y = driver.get_window_size()['height']  #height为y坐标
    return (x, y)

def swipeUp(t):  #当前向上滑动swipeup
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2,500)  #设置时间为500
swipeUp(9000)     #向上滑动9000


driver.find_element_by_android_uiautomator('new UiSelector().text("点击获取定位")').click()


# driver.quit()









if __name__=="__main__":
    pass