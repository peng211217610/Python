
import requests

r = requests.get('http://www.santostang.com/')

'''

pytest-xdist:并行执行测试用例


响应状态码
r.status_code
(200)


文本编码
r.encoding
(UTF-8)


r.headers['content-type']

字符串响应体
r.text
(HTML内容),r.text的类型是unicode

r.json()


r.url

r.cookies

r.headers



#get

key_dict = {'key1':'value1','key2':'value2'}
r = request.get(url,params=key_dict)




获取响应时间的正确姿势应该是：r.elapsed.total_seconds()


https安全证书
请求地址为https，就会校验安全证书，所以，需要在请求中加上参数verify=False，忽略安全证书
但是requests库会强制验证安全证书，所以需要加上如下内容
import urllib3
urllib3.disable_warnings()
忽略告警信息





'''





































































