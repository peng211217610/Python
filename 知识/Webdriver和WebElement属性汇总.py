#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''Python+Selenium WebDriver API：浏览器及元素的常用函数及变量整理总结'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from selenium import webdriver

#浏览器属性dir(driver)
'''
调用说明：
driver.属性值


变量说明：
1.driver.current_url：用于获得当前页面的URL
2.driver.title：用于获取当前页面的标题
3.driver.page_source:用于获取页面html源代码
4.driver.current_window_handle:用于获取当前窗口句柄
5.driver.window_handles:用于获取所有窗口句柄


函数说明：
1.driver.find_element*():定位元素，详看另外一篇博文：Selenuim+Python之元素定位总结及实例说明
2.driver.get(url):浏览器加载url。实例：driver.get("http//:www.baidu.com")
3.driver.forward()：浏览器向前（点击向前按钮）。
4.driver.back()：浏览器向后（点击向后按钮）。
5.driver.refresh()：浏览器刷新（点击刷新按钮）。
6.driver.close()：关闭当前窗口，或最后打开的窗口。
7.driver.quit():关闭所有关联窗口，并且安全关闭session。
8.driver.maximize_window():最大化浏览器窗口。
9.driver.set_window_size(宽，高)：设置浏览器窗口大小。
10.driver.get_window_size()：获取当前窗口的长和宽。
11.driver.get_window_position()：获取当前窗口坐标。
12.driver.get_screenshot_as_file(filename):截取当前窗口。
实例：driver.get_screenshot_as_file('D:/selenium/image/baidu.jpg')
13.driver.implicitly_wait(秒)：隐式等待，通过一定的时长等待页面上某一元素加载完成。
若提前定位到元素，则继续执行。若超过时间未加载出，则抛出NoSuchElementException异常。
14.driver.switch_to.frame(id或name属性值)：切换到新表单(同一窗口)。若无id或属性值，可先通过xpath定位到iframe，再将值传给switch_to.frame()
15.driver.switch_to.parent_content():跳出当前一级表单。该方法默认对应于离它最近的switch_to.frame()方法。
16.driver.switch_to.default_content():跳回最外层的页面。
17.driver.switch_to_window(窗口句柄)：切换到新窗口。
18.driver.switch_to.window(窗口句柄):切换到新窗口。
19.driver.switch_to_alert():警告框处理。处理JavaScript所生成的alert,confirm,prompt.
20.driver.switch_to.alert():警告框处理。
21.driver.execute_script(js):调用js。
22.driver.get_cookies():获取当前会话所有cookie信息。
23.driver.get_cookie(cookie_name)：返回字典的key为“cookie_name”的cookie信息。
实例：driver.get_cookie("NET_SessionId")
24.driver.add_cookie(cookie_dict):添加cookie。“cookie_dict”指字典对象，必须有name和value值。
25.driver.delete_cookie(name,optionsString):删除cookie信息。
26.driver.delete_all_cookies():删除所有cookie信息。

'''

#页面元素属性
'''
调用说明：
driver.find_element*.属性值
或
element=driver.find_element*
element.属性值
 
变量说明：
1.element.size:获取元素的尺寸。
2.element.text：获取元素的文本。
3.element.tag_name:获取标签名称。
 
函数说明：
1.element.clear():清除文本。
2.element.send_keys(value):输入文字或键盘按键（需导入Keys模块）。
3.element.click()：单击元素。
4.element.get_attribute(name):获得属性值
5.element.is_displayed():返回元素结果是否可见（True 或 False）
6.element.is_selected():返回元素结果是否被选中（True 或 False）
7.element.find_element*():定位元素，用于二次定位。
'''





