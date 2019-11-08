#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/3 19:18
# @desc: 使用yield生成器对30w 新闻文本数据清洗

import os
import time
from chapter5.FileRead import generate_text_dir


if __name__ == '__main__':
    start = time.time()
    # 获取文件夹的绝对路径
    filepath = os.path.abspath(r"../CSCMNews")
    print(filepath)
    generate_text_dir(filepath)
    end = time.time()
    print('total spent times:%.2f' % (end - start) + ' s')
