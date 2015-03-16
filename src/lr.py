#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 10:29:01 PM$"

import numpy
#import pickle
import cPickle as pickle
from sklearn import cross_validation
#from sklearn import metrics
from sklearn import preprocessing
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import SelectPercentile
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data.pkl", "rb"))

    train_data = dataset[0]
    train_target = dataset[1]
    
#    print 'Poly feature.'
#    train_data = preprocessing.PolynomialFeatures(2).fit_transform(train_data)
    
    print 'Scaling train data.'
    min_max_scaler = preprocessing.MinMaxScaler()    
    
    train_data = numpy.mat(min_max_scaler.fit_transform(train_data), numpy.float32)
#    train_data = preprocessing.OneHotEncoder().fit_transform(train_data)
#    train_data = numpy.mat(preprocessing.StandardScaler().fit_transform(train_data), numpy.float32)
#    train_data = numpy.mat(preprocessing.normalize(train_data, norm='l1'), numpy.float32)
#    train_data = numpy.mat(preprocessing.scale(train_data), numpy.float32)
    
#                           
#    print 'Feature selection.'
#    train_data = SelectPercentile(percentile=70).fit_transform(train_data, 
#                                                               train_target)

#    X_train, X_test, y_train, y_test = \
#        cross_validation.train_test_split(train_data, train_target, 
#                                          test_size=0.3, random_state=42)

    X_train = train_data
    y_train = train_target
     

    model = LogisticRegression(penalty='l2', C=0.7)
#    model = GaussianNB()
#    model = AdaBoostClassifier(n_estimators=100)
#    model = GradientBoostingClassifier(n_estimators=50, learning_rate=0.6,
#                                        max_depth=2, random_state=0)
    
    print 'Train model.'
    
    clf = model.fit(X_train, y_train)

#    print 'Test model. Use cross validation.'
#
#    print clf.score(X_test, y_test)
    
#    print 'Test model. Use test data.'
#    
#    test_dataset = pickle.load(open("../localdata/test_data.pkl", "rb"))
#
#    test_data = test_dataset[0]
#    test_target = test_dataset[1]
#    
#    print 'Scaling test data.'
#    
#    test_data = numpy.mat(min_max_scaler.fit_transform(test_data), numpy.float32)
##    test_data = preprocessing.OneHotEncoder().fit_transform(test_data)
##    test_data = numpy.mat(preprocessing.StandardScaler().fit_transform(test_data), numpy.float32)
##    test_data = numpy.mat(preprocessing.scale(test_data), numpy.float32)
##    test_data = numpy.mat(preprocessing.normalize(test_data, norm='l1'), numpy.float32)
#    
#                           
#    print clf.score(test_data, test_target)
    
#    print 'Classification report.'
#    y_predicted = clf.predict(X_test)
#    print(metrics.classification_report(y_test, y_predicted))
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/lr_model.pkl', 'wb'))
