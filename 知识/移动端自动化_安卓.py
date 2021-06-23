#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''安卓自动化的一些说明'''

#变量


#引入相关包
from appium import webdriver

desire_caps={
    "deviceName":"aaa"
}

driver=webdriver.Remote("http://localhost:4327/wd/hub",desire_caps)
'''
滚动查找元素
'''

'''




'''
#按回车键
driver.press_keycode(66)


#允许输入中文
desire_caps['unicodeKeyboard']=True
desire_caps['resetKeyboard']=True




#Android的resource-id对应ID定位方式
driver.find_element_by_id('com.tencent.mobileqq:id/btn_login')


#Android的content-desc属性对应AccessibilityId定位方式
driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')


#Android的Xpath定位与PC的Xpath定位大同小异，可以通过相对路径的定位方式定位。区别在于，这里相对路径定位的//后只可以接Android的class属性或*。
driver.find_element_by_xpath('//android.widget.EditText[@text="QQ号/手机号/邮箱"]')


#UIAutomator

#匹配全部text文字
driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")')

#包含text文字
driver.find_element_by_android_uiautomator('new UiSelector().textContains("机")')

#以text什么开始
driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("手")')

#正则匹配text
driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^手.*")')

#className
driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')

#classNameMatches
driver.find_elements_by_android_uiautomator('new UiSelector().classNameMatches("^android.widget.*")')

#resource-id
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.syqy.wecash:id/et_content")')

#description
driver.find_element_by_android_uiautomator('new UiSelector().description("S 日历")')

#descriptionStartsWith
driver.find_element_by_android_uiautomator('new UiSelector().descriptionStartsWith("日历")')

#descriptionMatches
driver.find_element_by_android_uiautomator('new UiSelector().descriptionMatches(".*历$")')


'''
iOS
iOS的label和name属性都对应AccessibilityId定位方式，如果有则推荐使用。

iOS10 以上使用XCUITest框架后，原生框架不支持XPATH，Appium进行了转换，速度很慢不建议使用。



'''









if __name__=="__main__":
    pass