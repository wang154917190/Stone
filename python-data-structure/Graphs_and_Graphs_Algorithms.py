#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用python实现邻接表（图的一种数据结构表示）
"""


class Vertex:
    """
    保存图中的每个定点
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}        # 使用字典来跟踪它连接的顶点和每个边的权重

    def addNeighbor(self, nbr, weight=0):
        """
        用于将这个顶点添加到一个连接到另一个
        :param nbr:
        :param weight:
        :return:
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + "connectedTo: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        返回邻接表中的所有顶点
        :return:
        """
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        """
        从这个顶点到作为参数传递的顶点的边的权重
        :param nbr:
        :return:
        """
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
