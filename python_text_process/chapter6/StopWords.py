#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/6 15:11
# @desc: 文本剔除停用词
import jieba
import itertools
import sys
sys.path.append(r"D:\PycharmProjects\python_for_text_process\chapter5")
from REdealText import textParse
from FileRead import readFile
from FeatureWord import get_stop_words

# 加载自定义分词词典
jieba.load_userdict("../user_dict.txt")


def seg_doc(str_doc):
    # 文章应该切分成单独句子，然后针对每个句子处理
    sent_list = str_doc.split("\n")

    # map内置高阶函数：一个函数f和迭代器list，函数f依次作用在迭代器每个元素中
    sent_list = list(map(textParse, sent_list))

    # 获取停用词
    stwlist = get_stop_words()

    # 分词去除停用词
    word_2dlist = [rm_tokens(jieba.cut(part, cut_all=False), stwlist) for part in sent_list]

    word_list = []
    for word in word_2dlist:
        word_list.extend(word)
    return word_list


def rm_tokens(words, stwlist):
    words_list = []
    words = list(words)
    for word in words:
        # 去除停用词、数字、单字符串、空字符串
        if word in stwlist or word.isdigit() or len(word) == 1 or word == "":
            continue
        else:
            words_list.append(word)
    return words_list


if __name__ == '__main__':
    path = r"../CSCMNews/体育/0.txt"
    str_doc = readFile(path)
    print(str_doc)
    seg_word = seg_doc(str_doc)
    print(seg_word)