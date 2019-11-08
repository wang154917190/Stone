#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/6 9:16
# @desc:

import os, time
from tqdm import tqdm
import sys
sys.path.append(r"D:\PycharmProjects\python_for_text_process\chapter5")
from REdealText import textParse


def readFile(path):
    with open(path, "r", encoding="utf-8") as f:
        str_doc = f.read()
    return str_doc



def TraversalDir(rootDir):
    """
    function: 使用递归调用的方式读取文件夹中的数据
    :param rootDir:
    :return:
    """
    #
    for i, lists in enumerate(os.listdir(rootDir)):
        path = os.path.join(rootDir, lists)
        if os.path.isfile(path):
            print('{t} *** {i} \t docs has been read'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            # str_doc = readFile(path)
        if os.path.isdir(path):
            TraversalDir(path)


# 使用循环读取数据
def read_text_dir(rootDir):
    """
    function: 循环读取文件夹中的文件
    :param rootDir:
    :return:
    """
    text_dir = {}
    for i, lists in tqdm(enumerate(os.listdir(rootDir)), desc=" recycle read text..."):
        cat = lists
        text = []
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            for text_name in os.listdir(path):
                text_path = os.path.join(path, text_name)
                text.append(readFile(text_path))
        text_dir[cat] = text
    return text_dir


# 使用生成器读取数据
class loadFolders(object):
    def __init__(self, par_path):
        self.par_path = par_path

    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_absparh = os.path.join(self.par_path, file)
            if os.path.isdir(file_absparh):
                yield file_absparh


class loadFiles(object):
    def __init__(self, par_path):
        self.par_path = par_path

    def __iter__(self):
        folders = loadFolders(self.par_path)
        for folder in folders:
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    content = readFile(file_path)
                    yield catg, content


def generate_text_dir(rootDir, isClear=False):
    text_dir = {}
    files = loadFiles(rootDir)
    n = 5
    for i, msg in tqdm(enumerate(files), desc="yield read text..."):
        if (i / n) % 1000 == 0:
            # content = textParse(content) # 正则清洗
            print('{t} *** {i} \t docs has been dealed'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

        # 保存数据
        catg = msg[0]  # 文章类别
        content = msg[1]  # 文章内容
        if isClear:
            content = textParse(content)
        if catg in text_dir.keys():
            text_dir[catg].append(content)
        else:
            text = []
            text.append(content)
            text_dir[catg] = text
    return text_dir


if __name__ == '__main__':
    start = time.time()
    # TraversalDir("../CSCMNews")
    filepath = os.path.abspath(r"../CSCMNews")
    generate_text_dir(filepath)
    end = time.time()