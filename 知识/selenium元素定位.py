#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''selenium使用笔记'''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg
from selenium import webdriver

driver = webdriver.Chrome('exedir')
driver.get('url')

#获取浏览器中已经保存的所有cookie
driver.get_cookies()
#获取特定cookie
driver.get_cookie('cookiename')

#隐式等待
driver.implicitly_wait(10)

#显式等待,需要的时候百度搜索吧，太长了


ele = driver.find_element_by_id('kw')

#对元素操作
ele.click()
ele.clear()
ele.send_keys('hello')
ele.find_element_by_id('su')



print(ele.text)#元素的文本内容
ele.get_attribute('href')#属性值
ele.get_attribute('innerHTML')#html内容
ele.get_attribute('outerHTML')#html内容

#获取输入框中的内容
ele.get_attribute('value')#注意不是用ele.text



#选择元素的方式
driver.find_element_by_id('kw')#找到返回，找不到报错

driver.find_element_by_name('kw')#如果有多个，返回第一个。找不到报错。
driver.find_elements_by_name('kw')#找所有kw的元素，返回一个列表，如果找不到，就是空列表

driver.find_element_by_class_name('kw')

driver.find_element_by_tag_name('kw')

driver.find_element_by_link_text('kw')

driver.find_element_by_partial_link_text('kw')


#iframe和frameset:iframe就是新开一个页面，frameset是里面可以放多个HTML页面
driver.switch_to.frame('frame_reference')
#frame_reference可以是1.frame元素的id或者name。2.frame元素的索引值。3.frame元素对应的webelement,driver.find_element_by_tag_name('iframe')

#切换回到主框架
driver.switch_to.default_content()

#如果是嵌套类型的，框架里面的框架里面还有框架，不能直接switch_to最里面一层，需要一步步切换。但是返回主框架可以一步完成
#如果是返回上一层
driver.switch_to.parent_frame()



#css选择器     h1 {color:red;font-size:14px;}属性之间用分号隔开。每个属性用键值对表示
#css选择元素的方式

#根据id       #food {color:red;}
driver.find_element_by_css_selector('#food')

#根据class   .vegetable {color:red;}
driver.find_element_by_css_selector('.vegetable')

#根据tag      p {color:red;}
driver.find_element_by_css_selector('p')

#根据tag和class组合     span.vegetable {color:red;}   注意这是并的关系
driver.find_element_by_css_selector('span.vegetable.good')#同时具有span这个tag属性，又有vegetable和good这两个class属性

#class中如果有空格，代表有多个属性，而不是带空格的属性
#仅限class属性，其他的例如spec属性，中间有空格也还是一个属性，是带中间空格的一个属性
'''
<span class="vegetable good">黄瓜</span>
'''



#后代选择器，即选择元素里面的子元素，可以跨代
driver.find_element_by_css_selector('#choose_car option')#与后代之间用空格隔开。

#子元素选择器，即必须是直接子元素，不可跨代
driver.find_element_by_css_selector('#choose_car > option')#用大于号如果是多层可以使用ul>ol>li>em，多次使用>,选中的是最后的元素

#选择所有子元素
driver.find_element_by_css_selector('#choose_car > *')#用星号表示所有子元素



#兄弟节点选择器，拥有相同的父节点：注意必须是相同的父节点
# 1.两个元素连接在一起的，不被其他元素隔开，用+号
driver.find_element_by_css_selector('#food + div')
# 2.必须是连接在一起的，不能被其他元素隔开，用~号
driver.find_element_by_css_selector('#food ~ div')


#某节点子元素有多个相同属性，但是只需要取其中一个
driver.find_element_by_css_selector('#food > p:nth-child(3)')#数字3是第几个子节点，跟p属性无关。是所有属性都算。







#组选择。要选择多个元素，是或的关系，可以用逗号隔开
driver.find_element_by_css_selector('p,button')#逗号隔开，就表示p属性和button属性的都选中

#因为或的优先级比较低，所以如下#food > span是一个整体
driver.find_element_by_css_selector('#food > span,button')#这是food下面的span属性（前面是一个整体），button属性。


'''
#CSS多种属性组合
*[style]#所有属性，并且，style属性
p[spec=len2]#p属性，并且，spec属性值为len2
p[spec='len2 len3']#p属性，并且，spec属性值为‘len2 len3’
p[spec*='len2']#p属性，并且，spec属性值包含len2
p[spec^='len2']#p属性，并且，spec属性是以len2开头的
p[spec$='len2']#p属性，并且，spec属性是以len2结尾的
p[class=special][name=p1]#p属性，并且，class属性的值等于special，并且，name属性的值是p1

'''


#单选框
ele.click()

#勾选框
ele.click()
ele.is_selected()#返回的是True或者False


#复选框，需要用到select方法
from seleniium.webdriver.support.ui import Select
select = Select(driver.find_element_by_id('multi'))
select.deselect_all()#去掉所有勾选
select.select_by_visible_text('雅阁')
select.select_by_visible_text('宝马')

















if __name__=="__main__":
    pass