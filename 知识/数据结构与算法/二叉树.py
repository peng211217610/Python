#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark=''''''

# 引入包
class TreeNode(object):

    def __init__(self,data,left=None,right=None):
        self.data,self.left,self.right=data,left,right

#先序遍历-使用递归
def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

#中序遍历-使用递归
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

#后序遍历-使用递归
def posorder(root):
    if root is not None:
        posorder(root.left)
        posorder(root.right)
        print(root.data)


































if __name__=="__main__":
    pass
