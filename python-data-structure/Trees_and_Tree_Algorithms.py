#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 查看树如何用于实现map数据结构
# 使用列表实现树
# 使用类和引用来实现树
# 实现树作为递归数据结构
# 使用堆实现优先级队列


# 列表树,逻辑
# myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
# print(myTree)
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])

class BinaryTreeList:
    """
    使用列表作为存储结构创建树结构
    """
    def __init__(self, root, leftChild=None, rightChild=None):
        self.tree = [root, [leftChild], [rightChild]]

    def insertLeft(self, newNode):
        """
        要插入一个左子节点， 我们首先获得与当前左子节点对应的（可能为空）的列表，然后将newNode添加到新的左子树，而将旧的左子树
        作为newNode节点的左子节点。这将允许我们在任何位置将新节点拼接到树中
        :param newNode:
        :return:
        """
        t = self.tree.pop(1)
        if len(t) >= 1:
            self.tree.insert(1, BinaryTreeList(newNode, leftChild=t))
        else:
            self.tree.insert(1, BinaryTreeList(newNode))

    def insertRight(self, newNode):
        t = self.tree.pop(2)
        if len(t) >= 1:
            self.tree.insert(2, BinaryTreeList(newNode, rightChild=t))
        else:
            self.tree.insert(2, BinaryTreeList(newNode))

    def getRootVal(self):
        return self.tree[0]

    def setRootVal(self, newNode):
        self.tree[0] = newNode

    def getLeftChild(self):
        return self.tree[1]

    def getRightChild(self):
        return self.tree[2]


class BinaryTreeC:
    """
    使用节点和引用的方式创建树结构
    """
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        要插入一个左子节点， 我们首先获得与当前左子节点对应的（可能为空）的列表，然后将newNode添加到新的左子树，而将旧的左子树
        作为newNode节点的左子节点。这将允许我们在任何位置将新节点拼接到树中
        :param newNode:
        :return:
        """
        if self.leftChild == None:
            self.leftChild = BinaryTreeC(newNode)
        else:
            t = BinaryTreeC(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTreeC(newNode)
        else:
            t = BinaryTreeC(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        """
        在树结构内部实现前序遍历算法，该方法必须在递归调用之前检查左右孩子是否存在
        :return:
        """
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


# 树的遍历： 前序、中序、后序（前、中、后表示的是根节点的遍历顺序）
def preorder(tree):
    """
    前序遍历代码如下，中序，后序代码只需要交换110,111,112三行的代码即可
    :param tree:
    :return:
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())



if __name__ == '__main__':
    # # 列表树的操作
    # L = BinaryTreeList("q")
    # print(L.getRootVal())
    # L.insertLeft("aaa")
    # print(L.getLeftChild().getRootVal())
    # L.insertRight("bbb")
    # print(L.getRightChild().getRootVal())

    # 引用树的操作
    r = BinaryTreeC("a")
    print(r.getRootVal())
    r.insertLeft('b')
    print(r.getLeftChild())   # 返回一个对象
    print(r.getLeftChild().getRootVal())   # 返回节点值
    r.insertRight("r")
    print(r.getRightChild())
    r.getRightChild().setRootVal("hello")
    print(r.getRightChild().getRootVal())
    print("*" * 50)
    # 树的遍历
    r.preorder()



