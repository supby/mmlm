#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 11:08:40 PM$"

import pickle
import csv

if __name__ == "__main__":
    
    #load sample submission
    games2predict = []
    with open('../data/sample_submission.csv', 'r') as incsv:
        with open('../data/submission1.csv', 'w') as outcsv:
            
            teamStatsByKey = pickle.load(open('../data/teamStatsByKey.pkl', 'rb'))
            clf = pickle.load(open('../data/lr_model.pkl', 'rb'))
            
            writer = csv.writer(outcsv)
            firstRow = True
            writer.writerow(['id', 'pred'])
            for row in csv.reader(incsv):
                if firstRow:
                    firstRow = False
                    continue
                    
                ids = row[0].split('_')
                wkey = int(ids[1])
                lkey = int(ids[2])
                
                wteam = teamStatsByKey[wkey]
                lteam = teamStatsByKey[lkey]
                
                p = clf.predict_proba([[wteam[i] - lteam[i] 
                                      for i in range(len(wteam))]])[0][1]
                                      
                writer.writerow(['%s_%s_%s' % (ids[0], wkey, lkey), p])
                
                print '%s_%s_%s => %s' % (ids[0], wkey, lkey, p)
                
                
                    
                
