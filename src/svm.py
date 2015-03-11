#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 9, 2015 9:27:18 PM$"

import pickle
from sklearn import cross_validation
from sklearn import svm
from sklearn import preprocessing
import numpy

if __name__ == "__main__":
    
    print 'Load train dataset'
    
    dataset = pickle.load(open("../localdata/train_data.pkl", "rb"))

    train_data = dataset[0]
    train_target = dataset[1]
    
    print 'Scaling train data.'
    min_max_scaler = preprocessing.MinMaxScaler()
    train_data = numpy.mat(min_max_scaler.fit_transform(train_data), 
                           numpy.float32)

    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=0)
    
#    clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
#                  gamma=0.0, kernel='rbf', max_iter=-1, probability=False,
#                  random_state=None, shrinking=True, tol=0.001, verbose=True)
    clf = svm.LinearSVC(verbose=1, C=0.7, loss='l2', penalty='l1', dual=False)
    
    print "Train SVC classifier"
    clf = clf.fit(X_train, y_train)
    
    print 'Test model. Use cross validation.'
    print clf.score(X_test, y_test)
    
    print 'Test model. Use test data.'
    
    test_dataset = pickle.load(open("../localdata/test_data.pkl", "rb"))

    test_data = test_dataset[0]
    test_target = test_dataset[1]
    
    print 'Scaling test data.'
    test_data = numpy.mat(min_max_scaler.fit_transform(test_data), 
                           numpy.float32)
                           
    print clf.score(test_data, test_target)    
    
    print 'Save model.'
    pickle.dump(clf, open('../localdata/svm_model.pkl', 'wb'))
