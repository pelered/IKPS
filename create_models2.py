# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 02:59:14 2019

@author: Petra
"""

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
import numpy as np





if __name__ == '__main__':
    get_data_with_salinity_leave_one(mode='data')
    get_data_for_original_leave_one(mode='data')
    get_data_for_double_time(mode='data')
    get_data_for_original_model(mode='data')
    get_data_with_salinity(mode='data')
