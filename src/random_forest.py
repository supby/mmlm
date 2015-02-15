#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 16, 2015 12:00:10 AM$"

import pickle
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data.pkl", "rb"))

    train_data = dataset[0]
    train_target = dataset[1]

    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=0)


    clf = RandomForestClassifier(n_estimators=50)
    
    print 'Train model.'
    
    clf = clf.fit(X_train, y_train)

    print 'Test model.'
    print 'Use cross validation.'

    print clf.score(X_test, y_test)    
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/rf_model.pkl', 'wb'))
