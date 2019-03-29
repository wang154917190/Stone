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
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    print(alist)


def shortBubbleSort(alist):
    """
    具有识别排序列表和停止优点的冒泡排序算法，冒泡排序时间复杂度O(n^2)
    如果某次遍历，未发生 交换操作，则说明列表已经有序，则可以停止后期遍历。
    :param alist:
    :return:
    """
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchanges = True
        passnum -= 1


def selectionSort(alist):
    """
    选择排序，选择排序时间复杂度O(n^2)
    :param alist:
    :return:
    """
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    """
    插入排序
    :param alist:
    :return:
    """
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue


def shellSort(alist):

    def gapInsertionSort(alist, start, gap):
        for i in range(start + gap, len(alist), gap):
            currentvalue = alist[i]
            position = i
            while position >= gap and alist[position - gap] > currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap
            alist[position] = currentvalue

    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increment of size", sublistcount, "the list is", alist)
        sublistcount = sublistcount // 2


def mergeSort(alist):
    """
    注意，合并操作通过重复从排序列表中取最小的项目，将项目逐个放回原始列表
    :param alist:
    :return:
    """
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[: mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

        print("Merging", alist)


def quickSort(alist):

    def quickSortHelper(alist, first, last):
        if first < last:
            splitpoint = partition(alist, first, last)
            quickSortHelper(alist, first, splitpoint - 1)
            quickSortHelper(alist, splitpoint+1, last)

    def partition(alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last
        done = False

        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        return rightmark

    quickSortHelper(alist, 0, len(alist) - 1)


if __name__ == '__main__':
    testlist = [1, 3, 5, 32, 12, 35, 22, 14]
    # print(len(testlist))
    # print(sequentialSearch(testlist, item=5))
    #
    # print(list(range(7, 0, -1)))
    # print(list(range(0, 7, 1)))
    # bubbleSort(testlist)
    # insertionSort(testlist)
    # shellSort(testlist)
    mergeSort(testlist)
    print(testlist)










































