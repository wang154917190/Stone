#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/5 17:06
# @desc:

import re
from chapter5.REdealText import readFile


def filter_tags(htmlstr):

    # 过滤 DOCTYPE
    htmlstr = " ".join(htmlstr.split())
    re_doctype = re.compile(r'<!DOCTYPE .*?> ', re.S)
    s = re_doctype.sub("", htmlstr)

    # 过滤CDATA
    re_cdata = re.compile("//<!CDATA\[[ >]∗ //\] > ", re.I)
    s = re_cdata.sub("", s)

    # style
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
    s = re_style.sub('', s)  # 去掉style

    # 处理换行
    re_br = re.compile('<br\s*?/?>')
    s = re_br.sub('', s)  # 将br转换为换行

    # HTML标签
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('', s)  # 去掉HTML 标签

    # HTML注释
    re_comment = re.compile('<!--[^>]*-->')
    s = re_comment.sub('', s)

    # 多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('', s)

    blank_line_l = re.compile('\n')
    s = blank_line_l.sub('', s)

    blank_kon = re.compile('\t')
    s = blank_kon.sub('', s)

    blank_one = re.compile('\r\n')
    s = blank_one.sub('', s)

    blank_two = re.compile('\r')
    s = blank_two.sub('', s)

    blank_three = re.compile(' ')
    s = blank_three.sub('', s)

    # 剔除超链接
    http_link = re.compile(r'(http://.+.html)')
    s = http_link.sub('', s)
    return s


if __name__ == '__main__':
    str_doc = readFile("./html.txt")
    clear_str = filter_tags(str_doc)
    print(clear_str)









