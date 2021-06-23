#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = ''''''

#变量


#引入相关包
# 爬取微博 Duebass的图片

from urllib import request
import re
import ssl

file_path = 'D:\TDdownload\Blog'
# http://wallpaper.apc.360.cn/index.php?c=WallPaper&a=getAppsByCategory&cid=6&start=6590&count=50
base_url = 'https://m.weibo.cn/api/container/getIndex?is_hot[]=1&is_hot[]=1&jumpfrom=weibocom&type=uid&value=1268075087&containerid=1078031268075087&page='

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Accept':'application/json, text/plain, */*',
    'Referer':'https://m.weibo.cn/p/1005051268075087/photos?from=page_100505&from=page_100505&mod=TAB&mod=TAB&jumpfrom=weibocom'
}

context = ssl._create_unverified_context()

for i in range(5,6):
    try:
        realurl = base_url + str(i)
        req = request.Request(url=realurl,headers=header)
        # resp = requests.get(realurl, headers=header)
        resp = request.urlopen(req,context=context).read().decode()
        print('==============正在下载第' + str(i) + '页的图片===============')
        # 先获取所有的large里面的url，注意观察，大图的url中都包含/large,那么我们获取所有的url然后过虐掉不包含/large的url就行了
        pat = '"url":"(.*?)"'
        list1 = re.compile(pat).findall(resp)
        list2 = filter(lambda url:url.find('/large') != -1,list1)
        list2 = list(list2)
        for j in range(0,len(list2) - 1):
            pic_url = list2[j].replace('\/','/')
            request.urlretrieve(pic_url,file_path + str(i) + str(j) + '.jpg')
        print('============第' + str(i) + '页的图片下载完成===============')

    except Exception as error:
        print(error)












if __name__=="__main__":
    pass