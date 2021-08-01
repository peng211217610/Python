from selenium import webdriver



chrome_options = webdriver.ChromeOptions()

# 选择一种存在的模拟手机设备类型
chrome_options.add_experimental_option(
    "mobileEmulation",
    {"deviceName": "Pixel 2"})

driver = webdriver.Chrome(
    desired_capabilities = chrome_options.to_capabilities()
)

driver.implicitly_wait(10)


driver.get('http://www.baidu.com')

element_keyword = driver.find_element_by_id("index-kw")

# 输入字符
element_keyword.click()
element_keyword.send_keys('松勤\n')




input('press to continue...')
driver.quit()