# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 02:59:14 2019

@author: Petra
"""

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
import numpy as np


def get_data_with_salinity(mode):
    """
        Extracting data  for model that includes salinity

        mode:
            'nb' for naive bayes result
            'dtc' for decision tree classifier
            'dtr' for decision tree regressor
            'data' for returning dataset
            'result' for result provided in excel
            'result_bin' for result provided in excel as classes
            'dtc_bin' for results as classes
    

    """
    data_with_salinity = []
    salinity_bin_result = []
    salinity_result = []
    #bez suhih dana
    data = pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Slanoca-bez suhih prosjek')
    
    for i in data.index:
        data_with_salinity.append([data['Sunce zracenje cijeli'][i], data['Padaline 72h'][i], data['Salinitet'][i]])
        salinity_bin_result.append(data['Zagadenost binarno cijeli'][i])
        salinity_result.append(data['Zagadenost cijeli'][i])
    
    X = data_with_salinity[:int(2*len(data_with_salinity)/3)]
    Y = salinity_result[:int(2*len(data_with_salinity)/3)]
    
    Y_bin = salinity_bin_result[:int(2*len(data_with_salinity)/3)]
    
    
    predict_data = data_with_salinity[2*int(len(data_with_salinity)/3)+1:]
    result_data = salinity_result[2*int(len(data_with_salinity)/3)+1:]  
    
    result_data_bin = salinity_bin_result[2*int(len(data_with_salinity)/3)+1:]

    
    if mode =='evaluacija':
        return data_with_salinity,salinity_result
    if mode=='evaluacija-bin-slanoca-bez':
        return data_with_salinity,salinity_bin_result
    
    #sa suhim danima
    data_with_salinity2 = []
    salinity_bin_result2 = []
    salinity_result2 = []
    
    data2 = pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Slanoca-suhi prosjek')
    
    for i in data2.index:
        #print(i)
        data_with_salinity2.append([data2['Sunce zracenje cijeli'][i], data2['Padaline 72h'][i], data2['Salinitet'][i]])
        salinity_bin_result2.append(data2['Zagadenost binarno cijeli'][i])
        salinity_result2.append(data2['Zagadenost cijeli'][i])
    
    X2 = data_with_salinity2[:int(2*len(data_with_salinity2)/3)]
    Y2 = salinity_result2[:int(2*len(data_with_salinity2)/3)]
    
    Y2_bin = salinity_bin_result2[:int(2*len(data_with_salinity2)/3)]
    
    
    predict_data2 = data_with_salinity2[2*int(len(data_with_salinity2)/3)+1:]
    result_data2 = salinity_result2[2*int(len(data_with_salinity2)/3)+1:]  
    
    result_data2_bin = salinity_bin_result2[2*int(len(data_with_salinity2)/3)+1:]



    if mode =='evaluacija-suhi':
        return data_with_salinity2,salinity_result2
    if mode=='evaluacija-bin-slanoca-sa':
        return data_with_salinity2,salinity_bin_result2

    # if only data is wanted, do not run model creation
    if mode == 'data':
        return X, Y, predict_data
    elif mode == 'result':
        return result_data,result_data2
    elif mode == 'result_bin':
        return result_data_bin, result_data2_bin

    # naive bayes
    if mode == 'nb':
        gaussian_nb_salinity = GaussianNB()
        gaussian_prediction_bez = gaussian_nb_salinity.fit(X, Y).predict(predict_data)
        gaussian_prediction = gaussian_nb_salinity.fit(X2, Y2).predict(predict_data2)

        return gaussian_prediction_bez,gaussian_prediction

    # decision tree regression

    if mode == 'dtr':
        regression_tree = DecisionTreeRegressor()
        regression_tree_prediction_bez = regression_tree.fit(X, Y).predict(predict_data)
        regression_tree_prediction = regression_tree.fit(X2, Y2).predict(predict_data2)
        return regression_tree_prediction_bez,regression_tree_prediction

    # decision tree classification
    if mode == 'dtc':
        classification_tree = DecisionTreeClassifier()
        classification_tree_prediction_bez = classification_tree.fit(X, Y).predict(predict_data)
        classification_tree_prediction = classification_tree.fit(X2, Y2).predict(predict_data2)
        return classification_tree_prediction_bez,classification_tree_prediction
    
    if mode == 'dtc_bin':
        classification_tree = DecisionTreeClassifier()
        classification_tree_prediction_bez_bin = classification_tree.fit(X, Y_bin).predict(predict_data)
        classification_tree_prediction_bin = classification_tree.fit(X2, Y2_bin).predict(predict_data2)
        return classification_tree_prediction_bez_bin, classification_tree_prediction_bin


def get_data_with_salinity_leave_one(mode):
    
    data_with_salinity = []
    salinity_bin_result = []
    salinity_result = []
    #bez suhih dana
    data = pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Slanoca-bez suhih prosjek')

    for i in data.index:
        data_with_salinity.append([data['Sunce zracenje cijeli'][i], data['Padaline 72h'][i], data['Salinitet'][i]])
        salinity_bin_result.append(data['Zagadenost binarno cijeli'][i])
        salinity_result.append(data['Zagadenost cijeli'][i])

    X=np.empty(shape=(len(data_with_salinity),3))
    Y=np.empty(shape=(len(salinity_result),1))
    
    Y_bin=np.empty(shape=(len(salinity_bin_result),1))
    
    for i in range(len(data_with_salinity)):
        X[i][0]=data_with_salinity[i][0]
        X[i][1]=data_with_salinity[i][1]
        X[i][2]=data_with_salinity[i][2]
    for i in range(len(salinity_result)):
        Y[i]=salinity_result[i]
    for i in range(len(salinity_bin_result)):
        Y_bin[i]=salinity_bin_result[i]
    #sa suhim danima
    data_with_salinity2 = []
    salinity_bin_result2 = []
    salinity_result2 = []
    
    data2 = pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Slanoca-suhi prosjek')

    for i in data2.index:
        #print(i)
        data_with_salinity2.append([data2['Sunce zracenje cijeli'][i], data2['Padaline 72h'][i], data2['Salinitet'][i]])
        salinity_bin_result2.append(data2['Zagadenost binarno cijeli'][i])
        salinity_result2.append(data2['Zagadenost cijeli'][i])
        
    X2=np.empty(shape=(len(data_with_salinity2),3))
    Y2=np.empty(shape=(len(salinity_result2),1))
    
    Y_bin2=np.empty(shape=(len(salinity_bin_result2),1))
    
    for i in range(len(data_with_salinity2)):
        X2[i][0]=data_with_salinity2[i][0]
        X2[i][1]=data_with_salinity2[i][1]
        X2[i][2]=data_with_salinity2[i][2]
    for i in range(len(salinity_result2)):
        Y2[i]=salinity_result2[i]
    for i in range(len(salinity_bin_result2)):
        Y_bin2[i]=salinity_bin_result2[i]        
    #naive bayes
    
    if mode=="nb":        
        gaussian_nb_salinity = GaussianNB()        
        test_result=[]
        test_result2=[]
        izmjereno2=[]
        for i in range(len(data_with_salinity)):
        
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y[i]
            Y=np.delete(Y,i,axis=0)    
            gaussian_prediction_bez = gaussian_nb_salinity.fit(X, Y).predict(X_t)
            test_result.append(gaussian_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y=np.insert(Y,i,y_t)
        
        for i in range(len(data_with_salinity2)):
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y2[i]
            Y2=np.delete(Y2,i,axis=0)    
            gaussian_prediction_bez2 = gaussian_nb_salinity.fit(X2, Y2).predict(X_t2)
            test_result2.append(gaussian_prediction_bez2)
            izmjereno2.append(y_t2)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y2=np.insert(Y2,i,y_t2)
        return test_result,test_result2
    
    # decision tree regression
    if mode == 'dtr':
        test_result=[]
        test_result2=[]
        regression_tree = DecisionTreeRegressor()

        for i in range(len(data_with_salinity)):
            
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y[i]
            Y=np.delete(Y,i,axis=0)    
            regression_tree_prediction_bez = regression_tree.fit(X, Y).predict(X_t)
            test_result.append(regression_tree_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y=np.insert(Y,i,y_t)
        
        for i in range(len(data_with_salinity2)):
            
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y2[i]
            Y2=np.delete(Y2,i,axis=0)    
            regression_tree_prediction_sa = regression_tree.fit(X2, Y2).predict(X_t2)
            test_result2.append(regression_tree_prediction_sa)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y2=np.insert(Y2,i,y_t2)
            
        return test_result,test_result2        
        
        
    # decision tree classification
    if mode == 'dtc':
        classification_tree = DecisionTreeClassifier()
        test_result=[]
        test_result2=[]
        
        for i in range(len(data_with_salinity)):
            
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y[i]
            Y=np.delete(Y,i,axis=0)    
            classification_tree_prediction_bez = classification_tree.fit(X, Y).predict(X_t)
            test_result.append(classification_tree_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y=np.insert(Y,i,y_t)
        
        for i in range(len(data_with_salinity2)):
            
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y2[i]
            Y2=np.delete(Y2,i,axis=0)    
            classification_tree_prediction_sa = classification_tree.fit(X2, Y2).predict(X_t2)
            test_result2.append(classification_tree_prediction_sa)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y2=np.insert(Y2,i,y_t2)
        
        return test_result,test_result2
        
    if mode == 'dtc_bin':
        classification_tree = DecisionTreeClassifier()
        test_result=[]
        test_result2=[]
        
        for i in range(len(data_with_salinity)):
            
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y_bin[i]
            Y_bin=np.delete(Y_bin,i,axis=0)    
            classification_tree_prediction_bez = classification_tree.fit(X, Y_bin).predict(X_t)
            test_result.append(classification_tree_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y_bin=np.insert(Y_bin,i,y_t)
        
        for i in range(len(data_with_salinity2)):
            
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y_bin2[i]
            Y_bin2=np.delete(Y_bin2,i,axis=0)    
            classification_tree_prediction_sa = classification_tree.fit(X2, Y_bin2).predict(X_t2)
            test_result2.append(classification_tree_prediction_sa)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y_bin2=np.insert(Y_bin2,i,y_t2)
        
        return test_result,test_result2
        
   
    
    if mode == 'data':
        return X, Y
    elif mode == 'result':
        return Y,Y2
    elif mode =='bin_result':
        return Y_bin,Y_bin2


def get_data_for_original_leave_one(mode):
    """
        Data used for original model s leave one out

        mode:
            'nb' for naive bayes result
            'dtc' for decision tree classifier
            'dtr' for decision tree regressor
            'data' for returning dataset
            'result' for result provided in excel
    """
    data = pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Obicno-bez suhi prosjek')
    original_data = []
    original_data_result = []
    original_data_result_bin = []
    
    for i in data.index:
        original_data.append([data['sunce cijeli'][i], data['padaline'][i]])
        original_data_result.append(data['zag cijeli'][i])
        original_data_result_bin.append(data['zag bin cijeli'][i])
    
    #sa suhim danima
    data2= pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Obicno-suhi prosjek')
    original_data2 = []
    original_data_result2 = []
    original_data_result_bin2 = []
    for i in data2.index:
        original_data2.append([data2['sunce cijeli'][i], data2['padaline'][i]])
        original_data_result2.append(data2['zag cijeli'][i])
        original_data_result_bin2.append(data2['zag bin cijeli'][i])
    
    X=np.empty(shape=(len(original_data),2))
    Y=np.empty(shape=(len(original_data_result),1))
    Y_bin=np.empty(shape=(len(original_data_result),1))
    
    #print(original_data_result_bin)
    
    for i in range(len(original_data)):
        X[i][0]=original_data[i][0]
        X[i][1]=original_data[i][1]
    for i in range(len(original_data_result)):
        Y[i]=original_data_result[i]
    for i in range(len(original_data_result_bin)):
        Y_bin[i]=original_data_result_bin[i]
        
    X2=np.empty(shape=(len(original_data2),2))
    Y2=np.empty(shape=(len(original_data_result2),1))
    Y_bin2=np.empty(shape=(len(original_data_result2),1))
    for i in range(len(original_data2)):
        X2[i][0]=original_data2[i][0]
        X2[i][1]=original_data2[i][1]
    for i in range(len(original_data_result2)):
        Y2[i]=original_data_result2[i]

    for i in range(len(original_data_result_bin2)):
        Y_bin2[i]=original_data_result_bin2[i]
    #naive bayes
    
    if mode=="nb":        
        gaussian_nb_salinity = GaussianNB()        
        test_result=[]
        test_result2=[]
        izmjereno2=[]
        for i in range(len(original_data)):
        
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y[i]
            Y=np.delete(Y,i,axis=0)    
            gaussian_prediction_bez = gaussian_nb_salinity.fit(X, Y).predict(X_t)
            test_result.append(gaussian_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y=np.insert(Y,i,y_t)
        
        for i in range(len(original_data2)):
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y2[i]
            Y2=np.delete(Y2,i,axis=0)    
            gaussian_prediction_bez2 = gaussian_nb_salinity.fit(X2, Y2).predict(X_t2)
            test_result2.append(gaussian_prediction_bez2)
            izmjereno2.append(y_t2)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y2=np.insert(Y2,i,y_t2)
        return test_result,test_result2
    
    # decision tree regression
    if mode == 'dtr':
        test_result=[]
        test_result2=[]
        regression_tree = DecisionTreeRegressor()

        for i in range(len(original_data)):
            
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y[i]
            Y=np.delete(Y,i,axis=0)    
            regression_tree_prediction_bez = regression_tree.fit(X, Y).predict(X_t)
            test_result.append(regression_tree_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y=np.insert(Y,i,y_t)
        
        for i in range(len(original_data2)):
            
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y2[i]
            Y2=np.delete(Y2,i,axis=0)    
            regression_tree_prediction_sa = regression_tree.fit(X2, Y2).predict(X_t2)
            test_result2.append(regression_tree_prediction_sa)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y2=np.insert(Y2,i,y_t2)
            
        return test_result,test_result2        
        
        
    # decision tree classification
    if mode == 'dtc':
        classification_tree = DecisionTreeClassifier()
        test_result=[]
        test_result2=[]
        
        for i in range(len(original_data)):
            
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y[i]
            Y=np.delete(Y,i,axis=0)    
            classification_tree_prediction_bez = classification_tree.fit(X, Y).predict(X_t)
            test_result.append(classification_tree_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y=np.insert(Y,i,y_t)
        
        for i in range(len(original_data2)):
            
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y2[i]
            Y2=np.delete(Y2,i,axis=0)    
            classification_tree_prediction_sa = classification_tree.fit(X2, Y2).predict(X_t2)
            test_result2.append(classification_tree_prediction_sa)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y2=np.insert(Y2,i,y_t2)
        
        return test_result,test_result2
        
    if mode=='dtc_bin':
        classification_tree = DecisionTreeClassifier()
        test_result=[]
        test_result2=[]
        
        for i in range(len(original_data)):
            
            X_t=X[[i],:]
            X=np.delete(X,(i),axis=0)
            y_t=Y_bin[i]
            Y_bin=np.delete(Y_bin,i,axis=0)    
            classification_tree_prediction_bez = classification_tree.fit(X, Y_bin).predict(X_t)
            test_result.append(classification_tree_prediction_bez)
            X = np.insert(X, i, X_t, axis = 0) 
            Y_bin=np.insert(Y_bin,i,y_t)
        
        for i in range(len(original_data2)):
            
            X_t2=X2[[i],:]
            X2=np.delete(X2,(i),axis=0)
            y_t2=Y_bin2[i]
            Y_bin2=np.delete(Y_bin2,i,axis=0)    
            classification_tree_prediction_sa = classification_tree.fit(X2, Y_bin2).predict(X_t2)
            test_result2.append(classification_tree_prediction_sa)
            X2 = np.insert(X2, i, X_t2, axis = 0) 
            Y_bin2=np.insert(Y_bin2,i,y_t2)
        
        return test_result,test_result2
    
    if mode == 'data':
        return X, Y
    elif mode == 'result':
        return Y,Y2
    elif mode =='bin_result':
        return Y_bin,Y_bin2
        
def get_data_for_original_model(mode):
    """
        Data used for original model

        mode:
            'nb' for naive bayes result
            'dtc' for decision tree classifier
            'dtr' for decision tree regressor
            'data' for returning dataset
            'result' for result provided in excel
            'result_bin' for result provided in excel as classes
            'dtc_bin' for results as classes
    """
    #otvaaramo za bez suhih dana, dobijemo sve i spremimo to zasebno i onda jos podijelimo na 1/3+2/3
    data = pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Obicno-bez suhi prosjek')
    original_data = []
    original_data_result = []
    original_data_result_bin = []

    for i in data.index:
        original_data.append([data['sunce cijeli'][i], data['padaline'][i]])
        original_data_result.append(data['zag cijeli'][i])
        original_data_result_bin.append(data['zag bin cijeli'])

    X = original_data[:int(2*len(original_data)/3)]
    Y = original_data_result[:int(2*len(original_data)/3)]
    
    Y_bin = original_data_result_bin[:int(2*len(original_data)/3)]

    predict_data = original_data[2*int(len(original_data)/3)+1:]
    original_result = original_data_result[2*int(len(original_data)/3)+1:]

    original_result_bin = original_data_result_bin[2*int(len(original_data)/3)+1:]

    #2/3  idu na trening otpocetka, a onda preostala 1/3 za predvidanje

    if mode =='evaluacija':
        return original_data,original_data_result
    if mode=="evaluacija-bin-bez":
        return original_data,original_data_result_bin
    #sa suhim danima
    data2= pd.read_excel(io='All_data(svi21.7).xlsx', sheet_name='Obicno-suhi prosjek')
    #print(data2)
    original_data2 = []
    original_data_result2 = []
    original_data_result_bin2 = []
    #print(data)
    for i in data2.index:
        original_data2.append([data2['sunce cijeli'][i], data2['padaline'][i]])
        original_data_result2.append(data2['zag cijeli'][i])
        original_data_result_bin2.append(data2['zag bin cijeli'])
    

    X2 = original_data2[:int(2*len(original_data2)/3)]
    Y2 = original_data_result2[:int(2*len(original_data2)/3)]
    
    Y2_bin = original_data_result_bin2[:int(2*len(original_data2)/3)]

    predict_data2 = original_data2[2*int(len(original_data2)/3)+1:]
    original_result2 = original_data_result2[2*int(len(original_data2)/3)+1:]
    #print(len(original_result2))
    #print("****")
    #print(len(X2))
    original_result2_bin = original_data_result_bin2[2 * int(len(original_data2) / 3) + 1:]


    if mode =='evaluacija-suhi':
        return original_data2,original_data_result2
    if mode=="evaluacija-bin-suhi":
        return original_data2,original_data_result_bin2

    if mode == 'data':
        return X, Y, predict_data
    elif mode == 'result':
        return original_result,original_result2
    elif mode == 'result_bin':
        return original_result_bin,original_result2_bin

    # naive bayes

    if mode == 'nb':
        gaussian_nb_salinity = GaussianNB()
        gaussian_prediction_bez = gaussian_nb_salinity.fit(X, Y).predict(predict_data)
        gaussian_prediction=gaussian_nb_salinity.fit(X2,Y2).predict(predict_data2)
        return gaussian_prediction_bez,gaussian_prediction

    # decision tree regression
    if mode == 'dtr':
        regression_tree = DecisionTreeRegressor()
        regression_tree_prediction_bez = regression_tree.fit(X, Y).predict(predict_data)
        regression_tree_prediction = regression_tree.fit(X2, Y2).predict(predict_data2)
        return regression_tree_prediction_bez,regression_tree_prediction

    # decision tree classification
    if mode == 'dtc':
        classification_tree = DecisionTreeClassifier()
        classification_tree_prediction_bez = classification_tree.fit(X, Y).predict(predict_data)
        classification_tree_prediction = classification_tree.fit(X2, Y2).predict(predict_data2)

        return classification_tree_prediction_bez,classification_tree_prediction
    
    if mode == 'dtc_bin':
        classification_tree = DecisionTreeClassifier()
        classification_tree_prediction_bez_bin = classification_tree.fit(X, Y_bin).predict(predict_data)
        classification_tree_prediction_bin = classification_tree.fit(X2, Y2_bin).predict(predict_data2)
        return classification_tree_prediction_bez_bin, classification_tree_prediction_bin
 


if __name__ == '__main__':
    get_data_with_salinity_leave_one(mode='data')
    get_data_for_original_leave_one(mode='data')
    get_data_for_original_model(mode='data')
    get_data_with_salinity(mode='data')
