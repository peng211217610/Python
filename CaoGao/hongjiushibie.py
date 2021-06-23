#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''红酒识别'''

# 引入包
import requests
import base64


#获取access_token
def get_access_token():
    r=requests.get('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YvFfwDyUeiLiDzZgr7BLP2TK&client_secret=owdGDsf17M1mfGrv0RRxgfLb1HpGiKbE')
    return r.json()['access_token']


def hongjiushibie(by_upload_or_by_url,file_dir,url):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    if by_upload_or_by_url=='upload':
        with open(file_dir,'rb') as f:
            content=f.read()
            # print(content)
    data = {"image": base64.b64encode(content)} if by_upload_or_by_url=='upload' else {"url":url}
    r=requests.post('https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine?access_token=%s' % get_access_token(),data=data,headers=headers)
    print(r.text)


if __name__ == "__main__":
    # print(get_access_token())
    # hongjiushibie('upload',r'D:\TDdownload\Document\Python\File\IMG\likou.jpg','')
    hongjiushibie('url','','https://img.alicdn.com/i1/3253611887/O1CN01J4nxvT1PoHz7JEhFu_!!3253611887.jpg')
    pass
