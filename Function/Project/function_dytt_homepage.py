#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''首页的一些操作'''

#引入相关包
from Function.Common.function_init_webdriver import *


def open_homepage_click_newest_movie():
    driver(r'https://www.dytt8.net/')
    driver.implicitly_wait(10)
    #这网站有广告，先点一下，再关闭这个窗口
    handle = driver.current_window_handle
    # try:
    #     # driver.find_element_by_id('cs_kd_div').click()
    #     ActionChains(driver).move_by_offset(200,100).click().perform()
    # finally:
    #     handles = driver.window_handles
    #     for one in handles:
    #         if one != handle:
    #             driver.switch_to.window(one)
    #             driver.close()
    #     driver.switch_to.window(handle)
    eles = driver.find_elements_by_xpath('//div[contains(@class,"co_content2")]/ul/a')
    # print(eles)
    FilmNameList_withduplicate = find_out_all_value(eles)
    # print(FilmNameList_withduplicate)
    #删除列表中重复元素
    FilmNameList=list(set(FilmNameList_withduplicate))

    for one in FilmNameList:
        driver.find_element_by_xpath('//a[(text()="%s")]' % one).click()
        handles = driver.window_handles
        for i in handles:
            if i != handle:
                driver.switch_to.window(i)
                fileName = driver.find_element_by_xpath('//div[@class="bd3"]/div[1]/div[2]/div[1]/h1/font').text
                #等待图片显示
                img_xpath = '//div[@class="bd3"]/div[1]/div[2]/div[2]/ul/div[1]/span/p/img'
                # WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,'img_xpath')))
                # action = ActionChains(driver).move_to_element(driver.find_element_by_xpath(img_xpath))
                # action.send_keys(Keys.ARROW_DOWN)
                # action.send_keys('v')
                # action.perform(r'D:\TDdownload')
                time.sleep(1)
                ActionChains(driver).context_click(driver.find_element_by_xpath(img_xpath)).perform()
                # ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
                pyautogui.write(['down','down','enter'])
                time.sleep(2)
                win32com.client.Dispatch('WScript.shell').Sendkeys('\n')
                time.sleep(2)
                ActionChains(driver).send_keys(Keys.ENTER)
                driver.close()
                driver.switch_to.window(handle)









    driver.quit()









if __name__=="__main__":
    open_homepage_click_newest_movie()
    pass