# coding=utf-8

import os
import fnmatch
from win32com import client as wc
from win32com.client import Dispatch


def Word2Txt(filePath, savePath=''):
    """
    function: word文件转存txt文件，默认存储当前路径下；用户可以指定存储文件路径。
    :param filePath: word文件路径
    :param savePath: 生成的txt文件保存路径
    :return:
    """
    # 1 切分文件上级目录和文件名
    dirs, filename = os.path.split(filePath)
    # print(dirs,'\n',filename)

    # 2 修改转化后的文件名
    new_name = ''
    if fnmatch.fnmatch(filename, '*.doc'):
        new_name = filename[:-4] + '.txt'
    elif fnmatch.fnmatch(filename, '*.docx'):
        new_name = filename[:-5] + '.txt'
    else:
        return
    print('->', new_name)

    # 3 文件转化后的保存路径
    if savePath == '':
        savePath = dirs
    else:
        savePath = savePath
    word_to_txt = os.path.join(savePath, new_name)
    print('->', word_to_txt)

    # 4 加载处理应用,word转化txt
    wordapp = wc.Dispatch('Word.Application')
    mytxt = wordapp.Documents.Open(filePath)
    mytxt.SaveAs(word_to_txt, 4)
    mytxt.Close()


if __name__ == '__main__':
    filepath = os.path.abspath(r'../dataSet/Corpus/wordtotxt/一种改进的朴素贝叶斯文本分类方法研究.doc')
    # savepath = ''
    Word2Txt(filepath)