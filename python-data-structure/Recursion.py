#!/usr/bin/env python
# -*- coding: utf-8 -*-


import turtle
import time
myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, leneLen):
    time.sleep(0.3)
    if leneLen > 0:
        myTurtle.forward(leneLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, leneLen-5)


def main():
    """
    绘制分形树
    :return:
    """
    def tree(branchLen, t):
        if branchLen > 5:
            t.forward(branchLen)
            t.right(20)
            tree(branchLen - 15, t)
            t.left(40)
            tree(branchLen - 10, t)
            t.right(20)
            t.backward(branchLen)

    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()


def moveTower(height, fromPole, toPole, withPole):
    """
    使用递归实现汉诺塔
    :param height:汉诺塔高度
    :param fromPole:起始杆
    :param toPole:目标杆
    :param withPole:中间杆
    :return:
    """
    def moveDisk(fp, tp):
        print("Moving disk from", fp, "to ", tp)

    if height >= 1:                                         # 当塔高度为0时，检测到的基本情况
        moveTower(height - 1, fromPole, withPole, toPole)   # 将初始杆上的底部圆盘移动到中间
        moveDisk(fromPole, toPole)                          # 将底部盘移动到其最终的位置
        moveTower(height - 1, withPole, toPole, fromPole)   # 将塔从中间杆移动到最大盘子的顶部


if __name__ == '__main__':
    # drawSpiral(myTurtle, 100)
    # myWin.exitonclick()  # 这是一个方便的缩小窗口的方法，使乌龟进入等待模式，直到你单机窗口，然后程序清理并退出

    main()
