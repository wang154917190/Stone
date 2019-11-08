#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/3 19:37
# @desc: 使用正则处理文本数据

import re
import itertools


'''
re.I    使匹配对大小写不敏感
re.L    做本地化识别（locale-aware）匹配
re.M    多行匹配，影响 ^ 和 $
re.S    使 . 匹配包括换行在内的所有字符
re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''


def readFile(path):
    with open(path, "r", encoding="utf-8") as f:
        str_doc = f.read()
    return str_doc


def textParse(str_doc):
    # 正则过滤特殊符号、标点、英文、数字
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'

    # 去除空格
    r2 = "\s+"

    # 去除换行符
    str_doc = re.sub(r1, " ", str_doc)

    # 多个空格成1个
    str_doc = re.sub(r2, " ", str_doc)

    # 去除换行符
    # str_doc = str_doc.replace("\n", " ")
    return str_doc


if __name__ == '__main__':
    path = r"../CSCMNews/体育/0.txt"
    str_doc = readFile(path)
    print(str_doc)
    print("*" * 40)
    word_list = textParse(str_doc)
    print(word_list)


















