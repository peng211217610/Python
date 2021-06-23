
import os

#调用系统程序，如果该程序不退出，代码不往下执行
os.system('mspaint')  #可以打开画图工具

#Linux上$?代表上个命令的退出码


#判断路径是否存在
if not os.path.exists(os.getcwd()):
    os.mkdir(os.getcwd())


#创建文件夹
#



list = ['1','2','3','4']

print(' '.join(list))
























