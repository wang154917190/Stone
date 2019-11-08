#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/6 14:30
# @desc:
import jieba
import jieba.posseg as ps
import sys
sys.path.append(r"D:\PycharmProjects\python_for_text_process\chapter5")
from REdealText import readFile


def extract_feature_words(str_doc):
    """
    function: 抽取特定词性的非停用词的词语
    :param str_doc:
    :return:
    """
    featWord = ""
    stwlist = get_stop_words()
    user_pos_list = ["nr", "ns", "nt", "nz"]    # 用户自定义特征词列表

    for word, pos in ps.cut(str_doc):
        if word not in stwlist and pos in user_pos_list:
            if word + " " + pos + "\n" not in featWord:
                featWord += word + " " + pos + "\n"
    return featWord


def get_stop_words(path="../stop_words.txt"):
    stop_words = readFile(path)
    stop_words.split("\n")
    return set(stop_words)


if __name__ == '__main__':
    path = r"../CSCMNews/体育/0.txt"
    str_doc = readFile(path)
    print(str_doc)
    featWord = extract_feature_words(str_doc)
    print(featWord)
