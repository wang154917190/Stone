#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:31
import requests

# API 中添加数据预处理过程
years_exp = [
        {"Pclass": 3, "Sex": "male", "Age": 22, "SibSp": 1, "Parch": 0, "Fare": 7.25, "Embarked": "S"},
        {"Pclass": 1, "Sex": "female", "Age": 38, "SibSp": 1, "Parch": 0, "Fare": 71.2833, "Embarked": "S"},
        {"Pclass": 3, "Sex": "female", "Age": 26, "SibSp": 0, "Parch": 0, "Fare": 7.925, "Embarked": "S"}
    ]
response = requests.post(url="http://127.0.0.1:8000/predict", json=years_exp)
result = response.json()
print(result)