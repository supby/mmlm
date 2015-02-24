#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 24, 2015 10:10:28 PM$"

import pickle
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

if __name__ == "__main__":
    print 'Load train dataset.'
    
    dataset = pickle.load(open("../localdata/train_data_0.pkl", "rb"))

    train_data = dataset[0][:200]
    train_target = dataset[1][:200]
    
    print 'PCA.'
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(train_data)
    
#    print 'Scale'
#    scaler = preprocessing.StandardScaler()
#    X_pca = scaler.fit_transform(X_pca)
    
    X_pca_0 = [X_pca[i] for i in range(len(X_pca)) if train_target[i] == 0]
    X_pca_1 = [X_pca[i] for i in range(len(X_pca)) if train_target[i] == 1]
    
    print 'Plot.'
    plt.plot([x[0] for x in X_pca_0], [x[1] for x in X_pca_0], 
            'rs', [x[0] for x in X_pca_1], [x[1] for x in X_pca_1], 'bs')
    plt.show()
    
    
    
    
