#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

pythonPath = r'D:\TDdownload\Document\Python'

import os, sys

sys.path.append(pythonPath)
import configure as cfg

import threading
import time

def do_something(num):
    print(num)




t1 = threading.Thread(target=do_something,args=(1,))
t2 = threading.Thread(target=do_something,args=(2,))





if __name__ == "__main__":
    t1.start()
    t2.start()

    print(t1.getName())



'''
t1.join()  --------t1的父线程将会被阻塞，在这里是创建t1的这个主线程，直到t1运行完，父线程再往下运行
t1.setdeamon()----------守护线程，需要在t1线程start之前设置，当主线程结束时，会检测当前的所有线程，如果检测到t2没结束，
主线程会等待t2，因为t1被设置为守护线程，所以主线程不会检测t1，t1是否结束对主线程是否结束没有影响。

'''



'''
#同步锁Lock
r = threading.Lock()          #一把锁
r.acquire()  #锁上
r.release()  #释放锁

#递归锁RLock
死锁：在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。


r = threading.Condition()
r.wait()
r.notify()
r.notifyAll()





#信号量
r = threading.BoundedSemaphore(5)      最多允许5把锁















'''




































