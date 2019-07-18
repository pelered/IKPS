# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:34:07 2019

@author: Petra
"""

import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
import create_models

X, Y = create_models.get_data_for_double_time(mode='evaluacija-bin')

seed = 7
models = []
models.append(('Naive Bayes', GaussianNB()))
models.append(('DT Class.', DecisionTreeClassifier()))
models.append(('DT Regr.', DecisionTreeRegressor()))

results = []
names = []
print("Original data, sa suhim,1/3+2/3-binarno")
for name, model in models:
    kfold = model_selection.KFold(n_splits=3, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='f1')
    results.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Orginal data-binarno')
fig.suptitle('Usporedba rezultata dobivenih za podatke koristeci 2 uzastopna vremena mjerenja')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

X, Y = create_models.get_data_for_double_time(mode='evaluacija-bin')

results2 = []
names = []
print("Original data, sa suhim,leave one out-binarno")
for name, model in models:
    kfold = model_selection.KFold(n_splits=len(X), random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='f1')
    results2.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Orginal data-leave one out-binarno')
fig.suptitle('Usporedba rezultata dobivenih za podatke koristeci 2 uzastopna vremena mjerenja')
ax = fig.add_subplot(111)
plt.boxplot(results2)
ax.set_xticklabels(names)
plt.show()
