#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from copy import deepcopy
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from ARMA_Model import ARMA_Model
from statsmodels.tsa.arima_model import ARIMA, ARMA
from dateutil.relativedelta import relativedelta
import datetime
import warnings
warnings.filterwarnings(action="ignore")


def draw_ts(timeSeries, label="None"):
    f = plt.figure(facecolor="white")
    timeSeries.plot(color="blue", label=label)
    plt.title(label)
    plt.show()


def draw_trend(timeSeries, size):
    """
    function: 绘制时间序列趋势，函数内部分别对其进行移动平均与加权移动平均处理
    :param timeSeries:
    :param size:
    :return:
    """
    f = plt.figure(facecolor="white")
    # 对size个数据进行移动平均
    rol_mean = timeSeries.rolling(window=size).mean()
    # 对size个数据进行加权移动平均
    rol_weighted_mean = timeSeries.ewm(span=size).mean()

    timeSeries.plot(color="blue", label="Original")
    rol_mean.plot(color="red", label="Rolling Mean")
    rol_weighted_mean.plot(color="black", label="Rolling weights Mean")
    plt.legend(loc="best")
    plt.title("Rolling Mean")
    plt.show()


def test_stationarity(timeSeries):
    """
    function: 时间序列平稳性检验
    :param timeSeries:
    :return:
    """
    # 平稳性检验
    dftest = adfuller(timeSeries)   # Augmented Dickey–Fuller test 扩展迪基-福勒检验,原假设是序列非平稳的
    dfoutput = pd.Series(dftest[0:4], index=["Test Statistic", "p_value", "#Lags Used", "Number of Observations Used"])
    for key, value in dftest[4].items():
        dfoutput["Critical Value {key}=".format(key=key)] = value
    print(dfoutput)
    return dfoutput


def draw_acf_pacf(ts, lags=31):
    """
    function: 绘制时间序列的自相关与偏相关图
    :param ts:
    :param lags:
    :return:
    """
    # 绘制自相关 、偏相关图，默认31阶
    f = plt.figure(facecolor="white")
    ax1 = f.add_subplot(211)
    plot_acf(ts, lags=lags, ax=ax1)

    ax2 = f.add_subplot(212)
    plot_pacf(ts, lags=lags, ax=ax2)
    plt.show()


def rool_predict(ts, predict_n, p=None, q=None, plog=True, pList=[12, 1, 1]):
    """
    function:进行滚动预测
    :param ts: 时间序列data
    :param predict_n: 预测的未来predict_n个单位数，默认单位为月，如果需要预测其他单位，只需修改end变量即可
    :param p:
    :param q:
    :param plog: 是否进行log处理
    :param pList: process 列表:移动平均、差分、差分
    :return: 预测序列
    """
    original_data = deepcopy(ts)
    pre = pd.Series()
    for i in np.arange(predict_n):
        # 取log
        if plog:
            ts_log = np.log(ts)
        else:
            ts_log = ts
        # 移动平均
        rol_mean = ts_log.rolling(window=pList[0]).mean()
        rol_mean.dropna(inplace=True)
        # 一阶差分
        ts_diff_1 = rol_mean.diff(pList[1])
        ts_diff_1.dropna(inplace=True)
        # 一阶差分
        ts_diff_2 = ts_diff_1.diff(pList[2])
        ts_diff_2.dropna(inplace=True)

        model = ARMA_Model(ts_diff_2)
        model.create_model(p, q)
        predict_ts = model.properModel.predict()

        start = datetime.datetime.date(ts_diff_2.index[-1])
        end = datetime.datetime.date(ts_diff_2.index[-1] + relativedelta(months=1))

        predict_ts = predict_ts.append(model.properModel.predict(start=start, end=end, dynamic=True)[-1:])
        # 一阶差分还原
        ts_diff_1 = ts_diff_1.append((pd.Series({end: 0})))
        ts_diff_1.index = pd.to_datetime(ts_diff_1.index)
        diff_shift_ts = ts_diff_1.shift(pList[2])
        diff_recover_1 = predict_ts.add(diff_shift_ts)
        # 一阶差分还原
        rol_mean = rol_mean.append(pd.Series({end: 0}))
        rol_mean.index = pd.to_datetime(rol_mean.index)
        rol_shift_ts = rol_mean.shift(pList[1])
        diff_recover = diff_recover_1.add(rol_shift_ts)
        # 移动平均还原
        rol_sum = ts_log.rolling(window=(pList[0] - 1)).sum()
        rol_sum = rol_sum.append(pd.Series({end: 0}))
        rol_sum.index = pd.to_datetime(rol_sum.index)
        rol_recover = diff_recover * pList[0] - rol_sum.shift(1)

        if plog:
            log_recover = np.exp(rol_recover)
        else:
            log_recover = rol_recover
        log_recover.dropna(inplace=True)  # 还原后的数据长度并不等于原数据，将减少一个单位（windows）的移动平均

        if i == 0:
            original_predict = log_recover
        # 保存预测值
        pre = pre.append(log_recover[-1:])
        # 重新定义时间序列数据（原始数据 + 预测数据（1条））
        ts = original_data.append(pre)
    return original_predict.append(pre[1:])


def main(ts):
    predict = rool_predict(ts=ts, predict_n=11, p=1, q=1)
    original_predict = predict[ts.index]  # 过滤没有预测的记录
    original_predict.dropna(inplace=True)

    plt.figure(facecolor='white')
    predict.plot(color='blue', label='Predict')
    ts.plot(color='red', label='Original')
    plt.legend(loc='best')
    plt.title('RMSE: %.4f' % np.sqrt(sum((original_predict - ts[original_predict.index]) ** 2) / original_predict.size))
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("1.csv", index_col="date", encoding="utf-8")
    data.index = pd.to_datetime(data.index)
    ts = data["sales"]

    main(ts)
    exit()


    # # 数据预处理
    # draw_ts(ts)
    # # 取log
    # ts_log = np.log(ts)
    #
    # test_stationarity(ts_log)
    # draw_ts(ts_log)
    #
    # # 平滑
    # draw_trend(ts, size=12)
    # draw_trend(ts_log, size=12)
    #
    # # 差分
    # diff_12 = ts.diff(12)
    # diff_12.dropna(inplace=True)
    # # diff_12_1 = diff_12.diff(1)
    # # diff_12_1.dropna(inplace=True)
    # test_stationarity(diff_12)
    # # draw_acf_pacf(diff_12)
    # model = ARMA(diff_12, order=(8, 2))
    # result_arma = model.fit(disp=-1, method='css')
    # predict_ts = result_arma.predict()
    #
    # # 分解
    # decomposition = seasonal_decompose(ts_log, model="additive")
    # trend = decomposition.trend
    # seasonal = decomposition.seasonal
    # residual = decomposition.resid
    # draw_ts(trend, label="trend")
    # draw_ts(seasonal, label="seasonal")
    # draw_ts(residual, label="residual")
    #
    # #
    # rol_mean = ts_log.rolling(window=12).mean()
    # rol_mean.dropna(inplace=True)
    # ts_diff_1 = rol_mean.diff(1)
    # ts_diff_1.dropna(inplace=True)
    # test_stationarity(ts_diff_1)
    #
    # ts_diff_2 = ts_diff_1.diff(1)
    # ts_diff_2.dropna(inplace=True)
    # test_stationarity(ts_diff_2)
    #
    # model = ARMA_Model(diff_12)
    # model.get_proper_model()
    # print('bic:', model.bic, 'p:', model.p, 'q:', model.q)
    #
    # # 移动平均
    # rol_mean = ts_log.rolling(window=12).mean()
    # rol_mean.dropna(inplace=True)
    #
    # # 一阶差分
    # ts_diff_1 = rol_mean.diff(1)
    # ts_diff_1.dropna(inplace=True)
    #
    # # 一阶差分
    # ts_diff_2 = ts_diff_1.diff(1)
    # ts_diff_2.dropna(inplace=True)
    #
    # # test_stationarity(ts_diff_2)
    # # draw_acf_pacf(ts_diff_2)
    #
    # model = ARMA_Model(ts_diff_2)
    # # model.get_proper_model()
    # # print('bic:', model.bic, 'p:', model.p, 'q:', model.q)
    # model.create_model(p=1, q=1)
    # predict_ts = model.properModel.predict()     # 区别predict() 与 forecast()

