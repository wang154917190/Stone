#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/6 16:32
# @desc: 分别使用NLTK、Counter分别对词频进行统计
import nltk
from StopWords import seg_doc
from FileRead import readFile
from collections import Counter
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False


def nltk_wf_feature(word_list):
    """
    function: 使用nltk.FreqDist统计词频
    :param word_list:
    :return:
    """
    fdist = nltk.FreqDist(word_list)
    # print(fdist.keys(), fdist.values())

    # print(fdist.freq("大雨"))     # 给定样本词的频率
    # print(fdist["大雨"])          # 给定样本词的次数
    #
    # fdist.tabulate(10)            # 频率分布表
    # fdist.plot(20, cumulative=False)   # 频率分布图
    # top10 = fdist.most_common(10)
    # print(top10)
    return fdist


def counter_wf_feature(word_list):
    """
    function: 使用Counter统计词频
    :param word_list:
    :return:
    """
    word_freq = Counter(word_list)
    # print(word_freq.keys(), word_freq.values())
    # top10 = word_freq.most_common(10)
    # print(top10)
    return word_freq


def del_freq_word(word_freq, high=15, low=2):
    """
    function: 剔除高低词频
    :param word_freq:
    :param high:
    :param low:
    :return:
    """
    word_list = []
    for key in word_freq.keys():
        # print(word_freq.get(key) > low & word_freq.get(key) < high)
        # print((word_freq.get(key) > low) & (word_freq.get(key) < high))
        # exit()
        if (word_freq.get(key) > low) & (word_freq.get(key) < high):
            word_list.append(key + ":" + str(word_freq.get(key)))
    return word_list


if __name__ == '__main__':
    path = r"../CSCMNews/体育/0.txt"
    str_doc = readFile(path)
    word_list = seg_doc(str_doc)
    word_freq = nltk_wf_feature(word_list)

    # counter_wf_feature(word_list)
    word_list = del_freq_word(word_freq)
    print(word_list)