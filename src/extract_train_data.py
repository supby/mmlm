#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 12:33:57 AM$"

import csv
import pickle

def getDif(wteam, lteam):
    """get diff in fetures for teams"""
    return [wteam[i] - lteam[i] for i in range(len(wteam))]

def extractTrainDataRow(row, X, Y, teamStatsByKey):
    """extract data row from csv"""
    wkey = int(row[2])
    lkey = int(row[4])

    wteam = teamStatsByKey[wkey]
    lteam = teamStatsByKey[lkey]

    # negative features row
    wdiff = getDif(lteam, wteam)
    X.append(wdiff)
    Y.append(0)
    # positive feature row
    ldiff = getDif(wteam, lteam)
    X.append(ldiff)
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
            
    pickle.dump((X, Y), open('../localdata/train_data_0.pkl', 'wb'))
            
    
