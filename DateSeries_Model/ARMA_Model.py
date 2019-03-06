#!/usr/bin/env python
# -*- coding: utf-8 -*-

from statsmodels.tsa.arima_model import ARIMA, ARMA
import sys
from copy import deepcopy
import numpy as np

class ARMA_Model:
    def __init__(self, ts, maxLag=9):
        self.data_ts = ts
        self.resid_ts = None
        self.predict_ts = None
        self.maxLag = maxLag
        self.p = maxLag
        self.q = maxLag
        self.properModel = None
        self.bic = sys.maxsize

    def get_proper_model(self):
        self._proper_model()
        self.predict_ts = deepcopy(self.properModel.predict())
        self.resid_ts = deepcopy(self.properModel.resid)

    def _proper_model(self):
        for p in np.arange(self.maxLag):
            for q in np.arange(self.maxLag):
                print("p, q, bic:", p, q, self.bic)
                model = ARMA(self.data_ts, order=(p, q))
                try:
                    result_ARMA = model.fit(disp=-1, method="css")
                except Exception as e:
                    print("_proper_model Error!\n", e)
                    continue

                bic = result_ARMA.bic
                if bic < self.bic:
                    self.p = p
                    self.q = q
                    self.properModel = model
                    self.bic = bic
                    # self.resid_ts = deepcopy(self.properModel.resid)
                    # self.predict_ts = deepcopy(self.properModel.predict())

    def create_model(self, p=None, q=None):
        if p == None and q == None:
            self._proper_model()
            model = ARMA(self.data_ts, order=(self.p, self.q))
        else:
            model = ARMA(self.data_ts, order=(p, q))
        try:
            self.properModel = model.fit(disp=-1, method="css")
            self.p = p
            self.q = q
            self.bic = self.properModel.bic
            self.predict_ts = self.properModel.predict()
            self.resid_ts = deepcopy(self.properModel.resid)
        except Exception as e:
            print("create_model ERROR!\n", e)
