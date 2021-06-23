'''
要求大家用面向对象的设计编写一个python程序，实现一个文字游戏系统。
动物园里面有10个房间，房间号从1 到 10。
每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
然后随机给出房间号，要求游戏者选择敲门还是喂食。
如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤
如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。
游戏3分钟结束后，显示每个房间的动物和它们的体重。
实现过程中，有什么问题，请通过课堂上讲解的调试方法，尽量自己发现错误原因。
'''
'''
思路：
10个房间设置一个类，实例化1-10
房间里可能是老虎，也可能是羊，是随机的
老虎设置一个类，个数未知，体重200斤
羊设置一个类，个数未知，体重100斤
游戏者可以在房间号1-10之间随机选择，可以做出动作有：敲门或者喂食
动作：
a.喂老虎，喂羊，结果，如果跟动物类型匹配，动物体重加10，否则减10
b.敲门，不论什么动物，体重都会减5斤，但是这个动作要判断是老虎还是羊
游戏目的是，每次游戏者都能知道这个房间号的动物类型
限制：时间只有3分钟,所以每次选择之前判断时间
结果：打印出每个房间的动物类型以及体重。
'''
#定义老虎和羊两个类
class Tiger:
    className = 'Tiger'
    def __init__(self,inweight=200):
        self.weight = inweight

    def feed(self,food):
        if food == 'meat':
            self.weight += 10
        else:
            self.weight -= 10

    def roar(self):
        self.weight -= 5

    @staticmethod
    def staticRoar():
        print('Wow !!')

class Sheep:
    className = 'Sheep'
    def __init__(self,inweight=100):
        self.weight = inweight

    def feed(self,food):
        if food == 'grass':
            self.weight += 10
        else:
            self.weight -= 10

    def roar(self):
        self.weight -= 5

    @staticmethod
    def staticRoar():
        print('mie~~')

#定义房间类
class Room:
    def __init__(self,innumber,inanimal):
        self.number = innumber
        self.animal = inanimal

from random import randint
#游戏开始时，初始化每个房间，放入列表
roomList = []
for num in range(1,11):
    if randint(0,1) == 0:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(num,ani)
    roomList.append(room)


#游戏进行时，每次做出选择，判断时间,如果超时了游戏退出
import time
startTime = time.time()
while True:
    room = roomList[randint(0, 9)]
    print('当前的房间号为：%2d' % room.number)
    option = input('喂食输入0，敲门输入1：')
    if time.time() - startTime > 10:
        print('已经超过游戏时间，游戏退出！')
        break
    else:
        if option == '0':
            infood = input('请输入meat或grass：')
            if infood not in ('meat','grass'):
                print('输入错误，仅可输入meat或者grass!')
                continue
            if time.time() - startTime > 10:
                print('已经超过游戏时间，游戏退出！')
                break
            else:
                room.animal.feed(infood)
        elif option == '1':
            room.animal.roar()
            room.animal.staticRoar()
        else:
            print('输入错误！')

#打印出需要的内容
from pprint import pprint
resultDict = {}
resultList = []
for one in roomList:
    animalType = one.animal.className
    animalWeight = one.animal.weight
    resultDict['room_%2d' % one.number] = [animalType,animalWeight]
    #resultList.append((animalType,animalWeight))
pprint(resultDict)