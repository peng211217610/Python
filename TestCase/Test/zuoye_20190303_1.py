#20190303作业
'''
请实现一个程序，实现如下需求点：

1.程序开始的时候提示用户输入学生年龄信息 格式如下：

Jack Green ,   21  ;  Mike Mos, 9;

我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）

2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零

'''

#思路

# 请输入一个字符串
# 如果没有分号，重新输入
# 如果切割后的字符串没有逗号，重新输入
# 如果切割列表不是2个，重新输入
# 如果切割出来第二位不是数字，重新输入
# 如果条件都满足，打印出结果，然后轮询下一个。


nameAge = input('请输入学生姓名和年龄信息：')
while nameAge.find(';') == -1:#输入字符串需包含分号
    nameAge = input('学生信息之间用分号隔开，请重新输入：')
else:
    i = 0
    Stlist = nameAge.split(';')
    while i <= len(Stlist)-1:
        StInfo = Stlist[i]
        if StInfo != '':
            while StInfo.find(',') == -1:
                nameAge = input('学生姓名和年龄用逗号隔开，请重新输入：')
                break
            else:
                str2 = StInfo.split(',')
                while len(str2) != 2:
                    nameAge = input('学生信息输入格式有误，请重新输入：')
                    break
                else:
                    name = str2[0].strip()
                    age = str2[1].strip()
                    while not age.isdigit():
                        nameAge = input('学生%s年龄不为整数，请重新输入：' % name)
                        break
                    print('%-20s:%02d' % (name, int(age)))
            i += 1
        else:
            quit()