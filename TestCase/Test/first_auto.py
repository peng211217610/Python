# from selenium import webdriver
# import sys
# driver = webdriver.Firefox(r'D:\TDdownload\geckodriver-v0.24.0-win64\geckodriver.exe')
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("松勤")



from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')




