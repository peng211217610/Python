'''
现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下

name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000

每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格

现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示

name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900

要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数
'''
#定义变量，待处理文件和输出文件
operate_file = r'D:\TDdownload\Document\Python\test\file_object\file1.txt'
target_file = r'D:\TDdownload\Document\Python\test\file_object\file2.txt'
#将要处理的内容写入待处理文件
with open(operate_file,'w') as of:
    of.write('name: Jack   ;    salary:  12000\n \
 name :Mike ; salary:  12300\n \
name: Luk ;   salary:  10030\n \
  name :Tim ;  salary:   9000\n \
name: John ;    salary:  12000\n \
name: Lisa ;    salary:   11000')
#逐行读取待处理文件，追加到待输出文件
with open(target_file,'w+') as tf:
    with open(operate_file) as of:
        nameList = of.read().splitlines()
        for one in nameList:
            item = one.replace(' ','')   #去掉每个元素的所有空格
            #以分号为分隔符，将每一行字符串切成列表，目的是获取salary的值
            salary = int(item.split(';')[1].split(':')[1])
            income = round(salary*0.9)
            tax = salary - income
            name = item.split(';')[0].split(':')[1]  #获取用户姓名
            tf.write('name: %s\t  \t  salary:%7d \t tax:%5d ;\tincome:%7d\n' % (name,salary,tax,income))
#检查目标文件内容
tf = open(target_file)
print(tf.read())
tf.close()