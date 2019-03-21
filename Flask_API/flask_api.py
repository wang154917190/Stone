#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 12:02
import traceback
import sys
import pandas as pd
from flask import request
from flask import Flask
from flask import jsonify

from sklearn.externals import joblib

def Data_Preprocessing(data):
    """
    数据预处理函数，此函数无法处理字符串替换操作：如 输入数据 Embarked 只包含"S"一种情况，则代码会由于
    data.ix[data["Embarked"] == "C", "Embarked"]  不包含数据而报错，程序无法运行
    :param data:
    :return:
    """
    data["Age"] = data["Age"].fillna(data["Age"].median())
    data.ix[data["Sex"] == "male", "Sex"] = 0
    data.ix[data["Sex"] == "female", "Sex"] = 1

    data["Embarked"] = data["Embarked"].fillna("S")
    data.ix[data["Embarked"] == "S", "Embarked"] = 0
    data.ix[data["Embarked"] == "C", "Embarked"] = 1
    data.ix[data["Embarked"] == "Q", "Embarked"] = 2
    return data

def Data_Preprocessing1(data):
    """
    输出预处理函数
    :param data:
    :return:
    """
    data["Age"] = data["Age"].fillna(data["Age"].median())
    data["Embarked"] = data["Embarked"].fillna("S")

    gender_values = {"male": 0, "female": 1}
    embarked_values = {"S": 0, "C": 1, "Q": 2}
    data.replace({"Sex": gender_values,
                  "Embarked": embarked_values}, inplace=True)
    return data


app = Flask(__name__)   # 创建一个flask对象
@app.route("/predict", methods=["POST"])
def predict():
    if model:
        try:
            json_ = request.json
            query = pd.DataFrame(json_, columns=model_columns)
            # 对输入数据进行预处理（字符串替换为数字）
            query = Data_Preprocessing1(data=query)

            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = list(model.predict(query))
            return jsonify({"prediction": str(prediction)})
        except Exception as e:
            print(e, "\n")
            return jsonify({"trace": traceback.format_exc()})
    else:
        print("Train the model first")
        return "No model here to use"


if __name__ == '__main__':
    # 设定端口号
    try:
        port = int(sys.argv[1])
        print(port)
    except:
        port = 8000
    print("导入模型")
    model = joblib.load("./model.pkl")
    model_columns = joblib.load("./model_columns.pkl")
    app.run(host="127.0.0.1", port=port, debug=True)