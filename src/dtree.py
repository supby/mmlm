#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 15, 2015 11:53:58 PM$"

import pickle
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data.pkl", "rb"))

    train_data = dataset[0]
    train_target = dataset[1]

    X_train, X_test, y_train, y_test = \
        cross_validation.train_test_split(train_data, train_target, 
                                          test_size=0.3, random_state=0)

#    lr = DecisionTreeClassifier()
    clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                         algorithm="SAMME.R",
                         n_estimators=10000)
    
    print 'Train model.'
    
    clf = clf.fit(X_train, y_train)

    print 'Test model.'
    print 'Use cross validation.'

    print clf.score(X_test, y_test)    
    
    print 'Save model.'    
    pickle.dump(clf, open('../localdata/dtree_model.pkl', 'wb'))
