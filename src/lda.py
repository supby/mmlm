#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 15, 2015 9:27:13 PM$"

import cPickle as pickle
import numpy
from sklearn import metrics
from sklearn import cross_validation
from sklearn.lda import LDA
from sklearn.qda import QDA
from sklearn import preprocessing

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data_0.pkl", "rb"))

    train_data = dataset[0]
    train_target = dataset[1]

    print 'Scaling the data.'
    min_max_scaler = preprocessing.MinMaxScaler()
    train_data = numpy.mat(min_max_scaler.fit_transform(train_data), 
                           numpy.float32)
                           
    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=42)
                                          
#    clf = LDA()
    clf = QDA()
    
    print 'Train model.'
    
    clf = clf.fit(X_train, y_train)

    print 'Test model.'
    print 'Use cross validation.'

    print clf.score(X_test, y_test)
    
    print 'Classification report.'
    y_predicted = clf.predict(X_test)
    print(metrics.classification_report(y_test, y_predicted))
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/lda_model.pkl', 'wb'))
