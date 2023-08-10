#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark=''''''

# 引入包

class Node(object):

    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#单链表
class SingleNode(object):
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        return self.__head==None

    def length(self):
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.val,end=' ')
        cur=cur.next

    def add(self,item):
        node=Node(item)
        node.next=self.__head
        self.__head=node

    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def insert(self,item,pos):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            node=Node(item)
            cur=self.__head
            count=0
            while count<(pos-1):
                cur=cur.next
                count+=1
            node.next=cur.next
            cur.next=node

    def remove(self,item):
        cur=self.__head
        pre=None
        while cur!=None:
            if cur.val==item:
                if cur==self.__head:
                    self.__head=cur.next
                else:
                    pre.next=cur.next
            else:
                cur=cur.next
                pre=cur

    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.val==item:
                return True
            else:
                cur=cur.next
        return False
























if __name__=="__main__":
    pass
