#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

#引入包
# from Function.Oppty.function_oppty_common import *

from locust import FastHttpUser,between,task
import lib.exporter

class ZtlooUser(FastHttpUser):

    host="http://ztloo.com/wp-json/wp/v2"

    wait_time = between(1,2)

    @task(3)

    def categories(self):
        self.client.get("/categories")

    @task(6)

    def tags(self):
        self.client.get("tags")




'''
locust -f ./ztloo.py
locust -f ./ztloo.py --headless --users 5 --spawn-rate 1 -H https://www.ztloo.com/wp-json/wp/v2
如果有配置文件，则是：locust --config ztloo.conf


'''










if __name__=="__main__":
    pass