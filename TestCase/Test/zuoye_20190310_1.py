'''
现有一个数据库记录文件（见附件0005_1.txt），保存了学生课程签到的数据库记录。 内容格式如下 ，

('2017-03-13 11:50:09', 271, 131),
('2017-03-14 10:52:19', 273, 131),
('2017-03-13 11:50:19', 271, 126),
每一行记录保存了学生的一次签到信息。

每一次签到信息的记录，分为三个部分， 分别是签到时间、签到课程的id号、签到学生的id号

要求大家实现下面的函数。其中参数fileName 为 数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。

def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：
key 是各个学生的id号， value是 该学生的签到信息
   其中value，里面保存着该学生所有签到的信息
       其中每个签到的信息是字典对象，有两个元素： key 是lessonid的 记录课程id，key是checkintime的 记录签到时间
比如，对于上面的示例中的3条记录，相应的返回结果如下：
{
    131: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
        {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
    ],


    126: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
    ],

}

'''

'''
思路：
先创建一个文件0005_1.txt，存放学生签到信息
分割出每一行，获取这一行的签到时间，课程号，学号
根据学号查找所有行，如果目标字典中没有这个学号，添加上去，如果有了，将签到时间和课程号添加在值里。
'''
import pprint
fileName = r'D:\TDdownload\Document\Python\test\file_object\0005_1.txt'
# with open(fileName,'w+') as tf:
#     print('open OK')

#定义函数体
def putInfoToDict(fileName):
    with open(fileName) as tf:
        signList = tf.read().strip().splitlines()       #将文件内容删除前后空格，分割成多行
        stu = {}      #最终需要输出的字典
        for one in signList:
            signInfo = {}
            str = one[one.find('(')+1:one.find(')')]    #对每一行处理，保留（）内部的内容
            signTime = str.split(',')[0].strip()[1:20]  #获取签到时间
            lessonid = int(str.split(',')[1].strip())   #获取课程号
            stuId = int(str.split(',')[2].strip())      #获取学生编号
            signInfo['lessonid'] = lessonid             #将课程号+签到时间作为一个字典，字典名signInfo
            signInfo['checkintime'] = signTime
            signIn = []
            #如果该学号已经在stu字典里，则只添加签到信息，如果不在，则添加学号到stu
            if stuId in stu:
                stu[stuId].append(signInfo)
            else:
                signIn.append(signInfo)
                stu[stuId] = signIn
        return stu

pprint.pprint(putInfoToDict(fileName))
