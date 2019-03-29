#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack:
    """
    栈的基本数据类型
    """
    def __init__(self):
        self.items = []

    def isEmpth(self):
        return self.items == []

    def push(self, item):
        """
        进栈
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
        出栈
        :return:
        """
        return self.items.pop()

    def peek(self):
        """
        只返回数据，栈中数据仍存在
        :return:
        """
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    """
    队列基本数据类型
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(namelist, num):
    """
    烫手山芋：使用队列实现，即按照num遍历队列，处于num处的值出队
    :param namelist:列表中元素依次入队
    :param num:
    :return:返回队列最后一个值
    """
    simqueue = Queue()

    for name in namelist:           # 将数据压入队列
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):                  # 循环遍历num次
            simqueue.enqueue(simqueue.dequeue())    # 将不是num处的数据出队，再压入队列
        deitem = simqueue.dequeue()          # 将位于num次的数据删除
        print("队列中删除的item", deitem)

    return simqueue.dequeue()


class Node:
    """
    定义连接节点类
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    """
    使用链表的抽象数据结构实现无序列表，
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        """
        在单链表的头部插入
        :param item:
        :return:
        """
        temp = Node(item)
        temp.setNext(self.head)   # 设置临时节点的指向链表头部
        self.head = temp          # 将临时节点的指针作为链表头指针

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        found = False
        current = self.head
        while self.head != None and not found:
            if current.getData() == item:
                found =True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class orderList(UnorderedList):
    """
    实现有序列表，部分方法继承无序列表类
    """

    def __init__(self):
        UnorderedList.__init__(self)
        # self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current               # 获取前一个节点
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)     #
            previous.setNext(temp)    # 设置前一个节点的Next()


if __name__ == '__main__':
    endItem = hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
    print(endItem)

    # mylist = UnorderedList()
    mylist = orderList()
    mylist.add(31)
    mylist.add(21)
    mylist.add(2)
    mylist.add(5)
    mylist.add(10)
    count = mylist.size()
    print(count)
    print(mylist.isEmpty())

