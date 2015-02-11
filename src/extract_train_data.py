#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 12:33:57 AM$"

import pickle
import csv

def getDif(wteam, lteam):
    return [wteam[i] - lteam[i] for i in range(len(wteam))]

def extractTrainDataRow(row, X, Y, teamStatsByKey):
    wkey = int(row[2])
    lkey = int(row[4])

    wteam = teamStatsByKey[wkey]
    lteam = teamStatsByKey[lkey]

    # negative features row
    wdiff = getDif(lteam, wteam)
    X.append(wdiff + [wdiff[1]*wdiff[2], wdiff[3]*wdiff[4], wdiff[5]*wdiff[6], 
            wdiff[7]*wdiff[9], wdiff[8]*wdiff[12]])
    Y.append(0)
    # positive feature row
    ldiff = getDif(wteam, lteam)
    X.append(ldiff + [ldiff[1]*ldiff[2], ldiff[3]*ldiff[4], ldiff[5]*ldiff[6], 
            ldiff[7]*ldiff[9], ldiff[8]*ldiff[12]])
    Y.append(1)
    
    print '%s_%s' % (wkey, lkey)

if __name__ == "__main__":    
    
    teamStatsByKey = pickle.load(open('../localdata/teamStatsByKey.pkl', 'rb'))
    
    X = []
    Y = []
    with open('../data/regular_season_detailed_results.csv', 'r') as tdf:
        firstRow = True
        for row in csv.reader(tdf):
            if firstRow:
                firstRow = False
                continue
                
            extractTrainDataRow(row, X, Y, teamStatsByKey)
            
    with open('../data/tourney_detailed_results.csv', 'r') as tdf:
        firstRow = True
        for row in csv.reader(tdf):
            if firstRow:
                firstRow = False
                continue
                
            extractTrainDataRow(row, X, Y, teamStatsByKey)
            
    pickle.dump((X, Y), open('../localdata/train_data.pkl', 'wb'))
            
    
