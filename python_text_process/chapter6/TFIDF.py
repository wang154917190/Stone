#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/7 10:10
# @desc:
import os
from FileRead import readFile
from StopWords import seg_doc
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from gensim import corpora, models
from gensim.sklearn_api import TfIdfTransformer


def tfidf_sklearn_feature(corpus, classVec=None):
    """
    function: 使用sklearn 中的TfidfTransformer, CountVectorizer 计算文本的tf-idf值
    :param corpus: 列表形式，每个位置为一文本字符串，如：["文本1", "文本2", "文本3"]
    :return:
    """
    corpus_tfidf = {}
    vectorizer = CountVectorizer()              # 构建词汇表, 文本数为行，所有文本去重后的单词数为列
    transformer = TfidfTransformer()            # 构建统计每个词的tf-idf 权值
    vect = vectorizer.fit_transform(corpus)     # (2, 242)   2:表示有两个文本，242: 表示两个文本去重之后的词的个数

    tfidf = transformer.fit_transform(vect)
    # word = vectorizer.get_feature_names()       # 获取词袋模型中的所有词语
    weight = tfidf.toarray()                    # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

    for i in range(len(weight)):                # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        cat = classVec[i]
        tmp = corpus_tfidf.get(cat, [])
        tmp.append(list(weight[i]))

        if tmp.__len__() == 1:
            corpus_tfidf[cat] = tmp
        # print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
        # for j in range(len(word)):
        #     print(word[j], weight[i][j])
    return corpus_tfidf


def tfidf_gensim_feature(corpus, classVec=None):
    """
    function: 使用gensim创建文本的tfidf模型，并计算tfidf权值
        gensim训练出来的tf-idf值左边是词的id，右边是词的tfidf值
        gensim有自动去除停用词的功能，比如the
        gensim会自动去除单个字母，比如i
        gensim会去除没有被训练到的词，比如name
        所以通过gensim并不能计算每个单词的tfidf值
    :param corpus: 列表形式，每个位置为一文本字列表，如：[["文本1"], ["文本2"], ["文本3"]]
    :param classVec:
    :return: 返回为每个词对应的tfidf权值，长度与对应的文本长度相同，而不是与词汇表长度相同，无法使用sklearn中的机器学习模型

    """
    dictonary = corpora.Dictionary(corpus)      # 构建词汇表，即后期每个文档的维度

    # 转换成 doc_bow
    doc_bow_corpus = [dictonary.doc2bow(doc_cut) for doc_cut in corpus]  # dictonary.doc2bow()  利用构建的词汇表对文本doc_cut进行稀疏向量,[(0, 1), (1, 2)],

    # 生成tfidf特征
    tfidf_model = models.TfidfModel(dictionary=dictonary)   # 生成tfidf模型

    corpus_tfidf = {}    # tfidf 词典
    i = 0
    for doc_bow in doc_bow_corpus:
        file_tfidf = tfidf_model[doc_bow]   # 词袋填充
        catg = classVec[i]                  # 对应文本的类别
        tmp = corpus_tfidf.get(catg, [])
        tmp.append(file_tfidf)

        if tmp.__len__() == 1:              # 字典中已经存在的类标签，仅插入一次
            corpus_tfidf[catg] = tmp
        i += 1
        # for key, value in dictonary.items():

    # print(corpus_tfidf)
    return corpus_tfidf
    # 将每一类保存到文件中
    # catgs = list(corpus_tfidf.keys())  # ['体育', '时政']
    # for catg in catgs:
    #     savepath = r'./'
    #     corpora.MmCorpus.serialize(r'{f}{s}{c}.mm'.format(f=savepath, s=os.sep, c=catg), corpus_tfidf.get(catg), id2word=dictonary)


if __name__ == '__main__':
    path = r"../CSCMNews/体育/0.txt"
    str_doc = readFile(path)

    word_list = seg_doc(str_doc)
    word_str = " ".join(word_list)

    path2 = r"../CSCMNews/时政/339764.txt"
    str_doc2 = readFile(path2)
    word_list2 = seg_doc(str_doc2)
    # print(type(word_list2))
    word_str2 = " ".join(word_list2)

    corpus = []                       # 每个文本为字符串
    classVec = ["体育", "时政"]
    corpus.append(word_str)
    corpus.append(word_str2)
    # 使用sklearn 计算词的tfidf
    a = tfidf_sklearn_feature(corpus, classVec)         # len(a["体育"][0]), len(a["时政"][0])   242, 242
    print(a)
    # # 使用gensim 计算词的tfidf
    # corpus_list = []                # 每个文本为子列表
    # corpus_list.append(word_list)
    # corpus_list.append(word_list2)
    # b = tfidf_gensim_feature(corpus_list, classVec)
    # print(b)