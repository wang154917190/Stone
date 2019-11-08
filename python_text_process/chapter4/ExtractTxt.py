# coding=utf-8


import os, fnmatch
from win32com import client as wc
from win32com.client import Dispatch,gencache
import jieba


def Files2Txt(filePath,savePath=''):
    """
    function: 抽取文件文本信息
    :param filePath: filePath：文件路径
    :param savePath: savePath： 指定保存路径
    :return:
    """
    try:
        # 1 切分文件上级目录和文件名
        dirs,filename = os.path.split(filePath)
        # print('目录：',dirs,'\n文件名：',filename)

        # 2 修改转化后的文件名
        typename = os.path.splitext(filename)[-1].lower() # 获取后缀
        new_name = TranType(filename,typename)
        # print('新的文件名：',new_name)

        # 3 文件转化后的保存路径
        if savePath=="": savePath = dirs
        else: savePath = savePath
        new_save_path = os.path.join(savePath,new_name)
        print('保存路径：',new_save_path)

        # 4 加载处理应用
        wordapp = wc.Dispatch('Word.Application')
        mytxt = wordapp.Documents.Open(filePath)
        mytxt.SaveAs(new_save_path,4)
        mytxt.Close()
    except Exception as e:
        pass


def TranType(filename, typename):
    """
    function: 根据文件后缀修改文件名
    :param filename: filePath：文件路径
    :param typename: typename 文件后缀
    :return: new_name 返回修改后的文件名
    """
    # 新的文件名称
    new_name = ""
    if typename == '.pdf' : # pdf->txt
        if fnmatch.fnmatch(filename,'*.pdf') :
            new_name = filename[:-4]+'.txt' # 截取".pdf"之前的文件名
        else:
            return
    elif typename == '.doc' or typename == '.docx' :  # word->txt
        if fnmatch.fnmatch(filename, '*.doc') :
            new_name = filename[:-4]+'.txt'
        elif fnmatch.fnmatch(filename, '*.docx'):
            new_name = filename[:-5]+'.txt'
        else:
            return
    else:
        print('警告：\n您输入[',typename,']不合法，本工具支持pdf/doc/docx格式,请输入正确格式。')
        return
    return new_name


if __name__ == '__main__':

    filePath1 = os.path.abspath(r'../dataSet/Corpus/wordtotxt/一种改进的朴素贝叶斯文本分类方法研究.doc')
    filePath2 = os.path.abspath(r'../dataSet/Corpus/pdftotxt/改进朴素贝叶斯文本分类方法研究.pdf')
    filePath3 = os.path.abspath(r'../dataSet/Corpus/wordtotxt/科技项目数据挖掘决策架构.docx')
    Files2Txt(filePath3)