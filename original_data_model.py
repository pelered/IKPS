import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
import create_models

X, Y = create_models.get_data_for_original_model(mode='evaluacija')

seed = 7
models = []
models.append(('Naive Bayes', GaussianNB()))
models.append(('DT Class.', DecisionTreeClassifier()))
models.append(('DT Regr.', DecisionTreeRegressor()))

results = []
names = []

for name, model in models:
    kfold = model_selection.KFold(n_splits=3, shuffle=False, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Orginal data,1/3,bez suhih')
fig.suptitle('Usporedba rezultata dobivenih za podatke podijeljene 2/3 i 1/3')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
"""
promijenila sam n_splits u 3. i Uzela sam da uzima sve podatke. Razlog tomu je sljedeci.
On  sa funkcijom cross_val_score uzme podatke  X i Y. podijeli ih na 3 dijela. i 1 uzme 
kaotest a ostala 2 spoji i trenira na njima. Zatim uzme drugu po redu grupu u podjeli i 
nju tretira kao test, a ostalo kao trening. Tako Isproba 3 verzija pofjele podataka 1/3+2/3.
i onda ispise rezultate.
TAKO SAM JA SHVATILA da ovo radi.Vratina staro ako sam u krivu.
"""
results_1_test=[]
for name, model in models:
    kfold = model_selection.KFold(n_splits=len(X), shuffle=False, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    results_1_test.append(cv_results)
    names.append(name)
    print('{}: mean {} std({})'.format(name,
                               cv_results.mean(),
                               cv_results.std()))

fig = plt.figure('Orginal data,1-test,bez suhih')
fig.suptitle('Usporedba rezultata dobivenih za podatke podijeljene 2/3 i 1/3')
ax = fig.add_subplot(111)
plt.boxplot(results_1_test)
ax.set_xticklabels(names)
plt.show()
