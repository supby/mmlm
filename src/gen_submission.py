#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 11:08:40 PM$"

import csv
import pickle

def getDif(wteam, lteam):
    return [wteam[i] - lteam[i] for i in range(len(wteam))]

if __name__ == "__main__":
    
    #load sample submission
    games2predict = []
    with open('../data/sample_submission.csv', 'r') as incsv:
        with open('../localdata/submission1.csv', 'w') as outcsv:
            
            teamStatsByKey = pickle.load(open('../localdata/teamStatsByKey.pkl', 'rb'))
            clf = pickle.load(open('../localdata/lr_model.pkl', 'rb'))
            
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
                
                wdiff = getDif(wteam, lteam)
                p = clf.predict_proba([wdiff + [wdiff[1] * wdiff[2], 
                                      wdiff[3] * wdiff[4], wdiff[5] * wdiff[6], 
                                      wdiff[7] * wdiff[9], wdiff[8] * wdiff[12]]])[0][1]
                                      
                writer.writerow(['%s_%s_%s' % (ids[0], wkey, lkey), p])
                
                print '%s_%s_%s => %s' % (ids[0], wkey, lkey, p)
                
                
                    
                
