#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''api相关登陆函数'''

#引入包
from Function.Oppty.function_oppty_database import *

#
# headers={
#     "common":{
#         "User-Agent":userAgent,
#         "Content-Type":contentType,
#         "Origin":origin,
#         "Referer":referer
#     },
#     "imf":{
#         "User-Agent":userAgent
#     }
# }

headers={
        "User-Agent":userAgent,
        "Content-Type":None,
        "Origin":origin,
        "Referer":referer
}

headers_of_imf={
    "User-Agent":userAgent
}


#这个要更新，用一个函数获取，函数读文件，从配置文件转换成列表
# headers_list = [headers,headers_with_refer,headers_govd,headers_ostms]
headers_list = [headers,headers_of_imf]




#构建session池
class SessionManager:

    def __init__(self):
        self.sessions = {}

    def get_session(self,username,password) -> requests.Session:
        if username in self.sessions:
            return self.sessions[username]
        s = requests.Session()
        s.post("http://api.com/login", data={"user": username, "pwd": password})#替换为正确的登陆接口
        self.sessions[username] = s
        return self.sessions[username]

manager = SessionManager()
#session = manager.get_session("user_A", "pwd_A")



'''鉴权'''
def get_basic_auth(username,password):
    return str(base64.b64encode((username+':'+password).encode('utf-8')),'utf-8')


#API请求函数
#'''myheaders类型值有：['headers','headers_with_refer','headers_govd','headers_ostms']'''
def api_common_requests(method,myheaders,mydata,url,my_session=None,cook=None,print_mydata='Y',print_result='Y'):
    method = method.upper()
    #获取Content-Type
    contenttype = myheaders.get("Content-Type") if myheaders else None
    #GET 请求防呆：如果传入嵌套字典，直接抛出异常
    if method == 'GET' and isinstance(mydata, dict) and any(isinstance(v, (dict, list)) for v in mydata.values()):
        raise ValueError(f"GET请求的params不支持嵌套结构！请检查参数: {mydata}")
    client = my_session if my_session else requests
    #准备好相关参数
    cookies_param = cook if (myheaders in headers_list and not my_session) else None
    #对于get请求，传入的字典必须是扁平的一维字典（比如 {"a": 1, "b": 2}）代码会自动拼接成?a=1&b=2
    params_param = mydata if method == 'GET' else None
    json_param = mydata if method != 'GET' and 'json' in contenttype.lower() else None
    data_param = mydata if method != 'GET' and not json_param else None
    #requests 对于传入 None 的参数，处理方式等同于“不传这个参数”，所以不用担心会带上空值。
    r = client.request(
        method=method,
        url=url,
        headers=myheaders,
        verify=False,
        cookies=cookies_param,
        params=params_param,
        data=data_param,
        json=json_param
    )
    # print(r.url)
    # print(r.content)
    # print(r.status_code)
    # 打印接口响应时间
    # print('接口响应时间(秒):'+str(r.elapsed.total_seconds()))
    if print_mydata=='Y':
        print(method)
        print(url)
        print(mydata)
    #判断is_json是否为真
    try:
        res_data = r.json()
        is_json = True
    except ValueError:
        res_data = r.text
        is_json = False
    #打印并写入文件
    if is_json:
        format_output = json.dumps(res_data, sort_keys=True, indent=2, ensure_ascii=False)
        if print_result == 'Y':
            print(format_output)
        File().write_to_file(os.path.join(ultra_dir, 'json文件.json'), 'w', format_output)
    else:
        if print_result == 'Y':
            print(res_data)
        File().write_to_file(os.path.join(ultra_dir, '响应体.txt'), 'w', res_data)
    return res_data





if __name__ == "__main__":
    pass
