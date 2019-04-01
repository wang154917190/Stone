#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sequentialSearch(alist, item):
    """
    顺序查找算法
    :param alist:
    :param item:
    :return:
    """
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


def orderSequentialSearch(alist, item):
    """
    顺序列表的顺序查找
    :param alist:
    :param item:
    :return:
    """
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found


def binarySearch(alist, item):
    """
    二分查找算法
    :param alist:
    :param item:
    :return:
    """
    first = 0
    last = len(alist) - 1   # 列表末尾的下标
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                last = midpoint + 1
    return found


def binarySearch2(alist, item):
    """
    二分查找的递归版本
    :param alist:
    :param item:
    :return:
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                binarySearch2(alist[: midpoint], item)
            else:
                binarySearch2(alist[midpoint+1:], item)


def bubbleSort(alist):
    for index in range(0, len(alist)):
        for i in range(index, len(alist)):
            if alist[index] > alist[i]:
                alist[index], alist[i] = alist[i], alist[index]
    print(alist)


def shortBubbleSort(alist):
    exchanges = True
    passnum = 0

    while passnum < len(alist) and exchanges:
        exchanges = False
        for i in range(passnum, len(alist)):
            if alist[passnum] > alist[i]:
                alist[passnum], alist[i] = alist[i], alist[passnum]
                exchanges = True
        passnum += 1


def selectionOfMaxSort(alist):
    """
    选择排序，选择排序时间复杂度O(n^2)
    选择一个最大值所在的位置与当前位置进行交换,也可选择一个最小值与当前位置进行交换
    :param alist:
    :return:
    """
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0            # 记录最大值的下标

        # 遍历找到列表最大值所在的下标位置
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        # 只交换一次：最大值与当前遍历值
        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]

def selectOfMinSort(alist):
    """
    选择最小值放在列表较低位置
    :param alist:
    :return:
    """
    for index in range(0, len(alist)-1):
        positionOfMin = index

        for location in range(index + 1, len(alist)):
            if alist[location] < alist[positionOfMin]:
                positionOfMin = location
        alist[positionOfMin], alist[index] = alist[index], alist[positionOfMin]

def insertionSort(alist):
    """
    插入排序
    :param alist:
    :return:
    """
    for index in range(1, len(alist)):
        # 提取出当前值以及下标,
        currentvalue = alist[index]
        position = index

        # 确定将当前值插入到之前子序列的位置
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]         # 如果当前位置之前值大于当前值，则将前一位置值后移，然后循环
            position = position-1
        alist[position] = currentvalue                  # 最后将当前值插入到合适位置


def shellSort(alist):

    def gapInsertionSort(alist, start, gap):
        for i in range(start + gap, len(alist), gap):
            currentvalue = alist[i]
            position = i
            while position >= gap and alist[position - gap] > currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap
            alist[position] = currentvalue

    sublistcount = len(alist) // 2   # gap 从列表中值处开始
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increment of size", sublistcount, "the list is", alist)
        sublistcount = sublistcount // 2


def mergeSort(alist):
    """
    归并排序算法分为两步：（1）拆分操作 （2）合并操作
    注意，合并操作通过重复从排序列表中取最小的项目，将项目逐个放回原始列表
    :param alist:
    :return:
    """
    print("Splitting", alist)
    if len(alist) > 1:
        # (1) 拆分操作
        mid = len(alist) // 2
        lefthalf = alist[: mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # (2)合并操作
        i = 0         # 定义lefthalf下标
        j = 0         # 定义righthalf下标
        k = 0         # 定义排序后alist下标

        # 在 lefthalf 与 rightlalf  中循环遍历一个较小值，放到最终的排序比列表中
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        # 检查是否左侧已遍历完毕，否则直接将lefthalf追加到排序列表后
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        # 检查是否右侧已遍历完毕，否则直接将righthalf追加到排序列表后
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

        print("Merging", alist)


def quickSort(alist):
    def quickSortHelper(alist, first, last):
        if first < last:
            splitpoint = partition(alist, first, last)     # 将列表在 splitpoint 处切分为两部分
            quickSortHelper(alist, first, splitpoint - 1)  # 对左半部分列表进行快速排序
            quickSortHelper(alist, splitpoint + 1, last)   # 对右半部分列表进行快速排序

    def partition(alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last
        done = False

        while not done:  # 循环移动左右标记位
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:  # 左标记位值小于等于枢纽值，左标记位右移
                leftmark = leftmark + 1
            while rightmark >= leftmark and alist[rightmark] >= pivotvalue:  # 右标记位值大于等于枢纽值，右标记位左移
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                # temp = alist[leftmark]
                # alist[leftmark] = alist[rightmark]
                # alist[rightmark] = temp
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        # 将枢纽值与右标记位互换值
        alist[first], alist[rightmark] = alist[rightmark], alist[first]
        return rightmark

    quickSortHelper(alist, 0, len(alist) - 1)


if __name__ == '__main__':
    testlist = [13, 1, 3, 5, 32, 12, 35, 22, 14]
    # print(len(testlist))
    # print(sequentialSearch(testlist, item=5))
    #
    # print(list(range(7, 0, -1)))
    # print(list(range(0, 7, 1)))
    # bubbleSort(testlist)
    # insertionSort(testlist)
    shellSort(testlist)
    # mergeSort(testlist)
    # print(testlist)
    # quickSort(testlist)
    print(testlist)









































