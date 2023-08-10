#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''获取链家网的心房数据'''

# 引入包
from selenium import webdriver


driver=webdriver.Chrome(executable_path=r'C:\Myprograms\Y-qita\Python')
driver.maximize_window()
driver.implicitly_wait(10)



def get_xinfang_info(host,port):
    xinfang_info=[]
    for i in range(1,59):
        driver.get('https://sz.fang.lianjia.com/loupan/pg%s/' % str(i))
        if i==1:
            time.sleep(5)
        else:
            time.sleep(2+randint(1,3))
            time.sleep(randint(1,2))
        driver.execute_script(down)
        time.sleep(1+randint(1,2))
        for j in range(1,11):
            name=driver.find_element_by_xpath('//ul[@class="resblock-list-wrapper"]/li[%s]/div/div[1]/a' % str(j)).text
            region=driver.find_element_by_xpath('//ul[@class="resblock-list-wrapper"]/li[%s]/div/div[2]/span[1]' % str(j)).text
            address=driver.find_element_by_xpath('//ul[@class="resblock-list-wrapper"]/li[%s]/div/div[2]/a' % str(j)).text
            room_num='/'.join(one.text for one in driver.find_elements_by_xpath('//ul[@class="resblock-list-wrapper"]/li[%s]/div/a/span' % str(j)))
            square=driver.find_element_by_xpath('//ul[@class="resblock-list-wrapper"]/li[%s]/div/div[3]/span' % str(j)).text
            avg_price=driver.find_element_by_xpath('//ul[@class="resblock-list-wrapper"]/li[%s]/div/div[6]/div[1]/span[1]' % str(j)).text
            print(i,j)
            xinfang_info.append((name,region,address,room_num,square,avg_price))
    insertinfo=[{{'index_%03d' % str(i):xinfang_info[i]}} for i in range(len(xinfang_info))]
    collection = pymongo.MongoClient(host, int(port))['lianjia']['xinfang']
    collection.insert_many(insertinfo)


























if __name__ == "__main__":
    get_xinfang_info(host,port)
    pass
