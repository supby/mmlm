#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 12:33:57 AM$"

import csv
import cPickle as pickle

def get_dif(wteam, lteam):
    """get diff in fetures for teams"""
    return [wteam[i] - lteam[i] for i in range(len(wteam))]

def extract_train_datarow(row, X, Y, 
                team_stats, start_season=None, end_season=None):
    """extract data row from csv"""
    season = int(row[0])
    
    if start_season and season < start_season:
        return
    
    if end_season and season >= end_season:
        return
    
    wkey = int(row[2])
    lkey = int(row[4])

    if not team_stats.get((float(row[0]),float(wkey)), None) or \
        not team_stats.get((float(row[0]),float(lkey)), None):
            return
        
    wteam = team_stats[(float(row[0]),float(wkey))]
    lteam = team_stats[(float(row[0]),float(lkey))]

    # negative features row
    wdiff = get_dif(lteam, wteam)
    X.append(wdiff)
    Y.append(0)
    # positive feature row
    ldiff = get_dif(wteam, lteam)
    X.append(ldiff)
    Y.append(1)
    
    print '%s_%s' % (wkey, lkey)

if __name__ == "__main__":    
    
    ts_by_season_key = pickle.load(open('../localdata/team_stats.pkl', 'rb'))
    
    X = []
    Y = []
    X_test = []
    Y_test = []
    with open('../data/regular_season_detailed_results.csv', 'r') as tdf:
        firstRow = True
        for row in csv.reader(tdf):
            if firstRow:
                firstRow = False
                continue
                
            extract_train_datarow(row, X, Y, ts_by_season_key, 
                    start_season=2003, end_season=2014)
            extract_train_datarow(row, X_test, Y_test, ts_by_season_key, 
                    start_season=2014)
            
    with open('../data/tourney_detailed_results.csv', 'r') as tdf:
        firstRow = True
        for row in csv.reader(tdf):
            if firstRow:
                firstRow = False
                continue
                
            extract_train_datarow(row, X, Y, ts_by_season_key, 
                    start_season=2003, end_season=2014)
            extract_train_datarow(row, X_test, Y_test, ts_by_season_key, 
                    start_season=2014)
            
    pickle.dump((X, Y), open('../localdata/train_data.pkl', 'wb'))
    pickle.dump((X_test, Y_test), open('../localdata/test_data.pkl', 'wb'))
            
    
