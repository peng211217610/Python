# coding=utf8
import threading
from time import sleep, ctime,time


def thread1_entry(nsec):
    print('child thread 1, start at:', ctime())
    sleep(nsec)
    print('child thread 1, end at:', ctime())


def thread2_entry(nsec):
    print('child thread 2, start at:', ctime())
    sleep(nsec)
    print('child thread 2, end at:', ctime())


print('main thread start.')
# 创建线程对象， 指定了新线程的入口函数
t1 = threading.Thread(target=thread1_entry, args=(1,))
t2 = threading.Thread(target=thread2_entry, args=(2,))

# 启动新线程
t1.start()
t2.start()

start = time()
# 等t1 线程结束
t1.join()
# 等t2 线程结束
t2.join()

end = time()

print(end-start)
print('main thread end.')
