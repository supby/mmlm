#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 16, 2015 10:43:34 PM$"

import pickle
from sklearn import metrics
from sklearn import cross_validation
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data_0.pkl", "rb"))

    train_data = dataset[0]
    train_target = dataset[1]

    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=0)
    
    clf = make_pipeline(PolynomialFeatures(3), LogisticRegression())
    
    print 'Train model.'
    
    clf = clf.fit(X_train, y_train)

    print 'Test model.'
    print 'Use cross validation.'

    print clf.score(X_test, y_test)
    
    print 'Classification report.'
    y_predicted = clf.predict(X_test)
    print(metrics.classification_report(y_test, y_predicted))
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/poly_model.pkl', 'wb'))
