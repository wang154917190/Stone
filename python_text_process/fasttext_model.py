#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2019/11/15 11:15
# @desc:
import os
from chapter5.FileRead import generate_text_dir
from chapter6.StopWords import seg_doc
from gensim.models import fasttext as fasttext_gensim
import fasttext


def write_data(data, file_name):
    assert isinstance(data, list), "数据data应为list格式，请检查数据格式"
    with open(file_name, "w", encoding="utf-8") as f:
        for sentence in data:
            f.write(sentence + "\n")
    print("write done!")


def propre_text():
    root_dir = os.path.abspath(r"D:\BaiduNetdiskDownload\CSCMNews")
    text_dir = generate_text_dir(root_dir, isClear=True)
    sentences = []
    cate_dict = {"体育": 1, "教育": 2, "时政": 3, "科技": 4, "财经": 5, "娱乐": 6}
    for category, texts in text_dir.items():
        for text in texts:
            text_seg = seg_doc(text)
            sentences.append("__label__" + str(cate_dict[category]) + " " + " ".join(text_seg))
    return sentences


def fasttext_model():
    print("create fasttext model...")
    model = fasttext.FastText.train_supervised("./fasttext.txt")

    # model.quantize("./fasttext.txt", retrain=True)   # 保存监督模型文件时，fastText可以通过牺牲一点点性能来压缩它以获得更小的模型文件。
    model.save_model("./fastText1.kpt")


def fasttext_model_gensim(sentences):

    # 使用gensim创建fastText模型
    model = fasttext_gensim.FastText(sentences, size=200, window=6, min_count=1, iter=10, min_n=3, max_n=6)
    print(model.wv["体育"])           # 词向量获得的方式
    print(model["体育"])              # 词向量获得的方式
    print(model.wv.word_vec("体育"))  # 词向量获得的方式
    model.save("./fastText1.kpt")
    # model = fasttext.FastText.load("./fastText.kpt")
    # print(model["体育"])
    # print(len(model["体育"]))
    # 输出词向量词典
    # print(model.wv.vocab)        # 以dict 的格式
    # print(model.wv.index2word)   # 以list的格式

    #  pip install pyemd
    # print(model.wmdistance(["篮球"], ["足球"]))

    # 求词附近的相似词
    # print(model.similar_by_vector("体育"))
    # print(model.similar_by_word("体育"))


if __name__ == '__main__':
    # # 模型训练
    # sentences = propre_text()
    # write_data(data=sentences, file_name="./fasttext.txt")
    # fasttext_model()
    # exit()
    # 模型测试

    test_txt = """今晚辽宁男篮将在主场迎战吉林队。八轮比赛过后，辽宁仅以4胜4负的成绩排名积分榜第十位，这与上赛季前八轮所取得的成绩一样。但相比今年大手笔的投入，这样的成绩很难让人满意。本轮面对实力稍逊于自己的吉林队，取胜是必须完成的任务。但竞技比赛世事难料，今日话题：辽宁男篮能否赢得东北德比。
    """
    text_seg = " ".join(seg_doc(test_txt))
    print(text_seg)
    model = fasttext.FastText.load_model("./fastText1.kpt")
    print(len(model.get_word_vector("比赛")))
    print(len(model.words))
    exit()
    pred = model.predict(text_seg, k=1)   # k 用于输出概率最高的预测结果
    print("predict result\n", pred)
