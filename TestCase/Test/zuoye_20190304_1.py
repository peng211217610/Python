'''
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面
'''
#方法一
def mySort(myList):
    newList = []
    for i in range(len(myList)):
        value = min(myList)
        newList.append(value)
        myList.remove(value)
    return newList
print(mySort([5,4,3,3,2,1,0,8,4,5,6,11,16,17,29,108,2]))


#方法二
# def mySort(myList):
#     i = 1
#     while i <= len(myList) - 1:             #i代表第几次轮询,总共可以轮询元素个数减1（不包含）
#         for j in range(0, len(myList) - i): #j代表第i次轮询时，只需要最多轮询元素个数减1（不包含）
#             if myList[j] > myList[j + 1]:
#                 myList[j], myList[j + 1] = myList[j + 1], myList[j]
#         i += 1
#     return myList
# print(mySort([5,4,3,3,2,1,0,8,4,5,6,11,16,17,29,108,2]))