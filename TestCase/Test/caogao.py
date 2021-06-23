# data = '{"action":"delete_course","id":1017}'
# import json
# print(json.loads(data))
# print(eval(data))
#
# import requests
# print(requests.codes.ok)

import requests
# from PIL import Image
# from io import BytesIO
# r = requests.get('http://vip.ytesting.com/randCodeImage',params={'a':'1553411974263'})
# print(r.content)
# with open(r'D:\TDdownload\Document\Python\test\file_object\aaa.jpg','wb+') as jpgf:
#     jpgf.write(r.content)
#
import json
import re
import requests
from PIL import Image
from selenium import webdriver

chromedriver = r'C:\Myprograms\J-计算机\Python36\chromedriver.exe'
loginurl = 'http://vip.ytesting.com/loginController.do?login'

#验证码保存地址
screenImg = r'D:\TDdownload\Document\Python\test\file_object\aaa.png'

#打开浏览器
driver = webdriver.Chrome(chromedriver)
driver.get(loginurl)
driver.implicitly_wait(2)

driver.get_screenshot_as_file(screenImg)
location = driver.find_element_by_id('randCodeImage').location
size = driver.find_element_by_id('randCodeImage').size
left = location['x']
top = location['y']
right = left + size['width']
botoom = top + size['height']

im = Image.open(screenImg)
cropedIm = im.crop((left,top,right,botoom))
cropedIm.save(screenImg)

from aip import AipOcr

config = {
    'appId': '15835934',
    'apiKey': '8xIVBewH3VHYABGGN58ikBKd',
    'secretKey': 'ZrfNRQKlRzgxHsV4ncX1QVEwTGjL1xaK'
}

client = AipOcr(**config)

def get_file_content(screenImg):
    with open(screenImg, 'rb') as fp:
        return fp.read()

def img_to_str(screenImg):
    image = get_file_content(screenImg)
    result = client.basicGeneral(image)
    print(result)
    print(type(result))
    YanzhengMa = result['words_result'][0]['words'].replace(' ', '')
    if ':' in YanzhengMa:
        YanzhengMa_result = YanzhengMa.replace(':','')
    else:
        YanzhengMa_result = YanzhengMa
    print(YanzhengMa)
    # if 'words_result' in result:
    #     return '\n'.join([w['words'] for w in result['words_result']])

img_to_str(screenImg)

driver.quit()
































