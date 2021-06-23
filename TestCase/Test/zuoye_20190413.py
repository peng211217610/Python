#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''Linux远程控制'''

'''
编写一个python程序，代码文件名为 memory.py , 该代码文件 计划在远程Linux机器运行。该程序做如下的事情：
    每隔5秒钟 打开文件 /proc/meminfo，该文件包含了系统内存使用信息，前面数行内容如下
    
MemTotal:        1920648 kB
MemFree:           87788 kB
Buffers:          229704 kB
Cached:          1180244 kB

    memory.py 程序要将 memFree 、buffers、cached 的值 相加 （结果是可用内存的数量）。
    然后除以 MemTotal的值， 得到可用内存占的百分比（赋值给变量 avaMem）。
    将 avaMem 的数值存入 结果文件ret.txt中。
    
    上面的程序一直运行，每隔 5秒钟 获取记录一次 avaMem 对应的时间戳， 格式如下
    20170315_12:10:00  77%
    20170315_12:10:05  74%
    20170315_12:10:10  70%
    20170315_12:10:15  72%

再编写一个python程序，代码文件名为 auto.py，该程序运行起来做如下工作：
    以自己名字的拼音（比如lixia） 在远程机器建立一个目录 。如果该目录已经存在则跳过此步骤
    拷贝文件memory.py 到远程机器该目录下面，
    远程在Linux主机执行文件 memory.py 
    过5分钟后，将远程文件memory.py执行产生的结果文件ret.txt 内容拷贝回本机
'''

#memory.py
'''
思路：
写一个while循环，每5秒钟，打开文件，读取出来，对整个字符串获取到相应的值
得到了需要的值以后，写一个函数，计算出结果，百分比保留2位小数
将结果写入到ret.txt中
'''

'''
思路：
Python登陆远程Linux主机
在/home下面判断是否存在penghuiming文件夹，如果没有则创建
将memory.py复制到penghuiming下面
执行memory
执行五分钟后，将ret.txt复制到本地
'''
import paramiko

#创建实例
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.145.130',22,'root','Winovs12')

cmd = '''if [ -d /home/penghuiming ];then
echo "directory already exist."
else
mkdir -p /home/penghuiming
fi
cp /home/memory.py /home/penghuiming
./home/penghuiming/memory.py
sleep 300
pid = `ps -ef | grep memory.py | grep -v grep | awk '{print $2}'`
kill -9 "${pid}"
'''

stdin,stdout,stderr = ssh.exec_command(cmd)

print(stdout.read())

sftp = ssh.open_sftp()

sftp.get('/home/ret.txt',r'D:\TDdownload\ret.txt')

ssh.close()
































































