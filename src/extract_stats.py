# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 6, 2015 11:46:06 PM$"

import csv
import numpy as np
import pickle

def extractTeamsStats(teamRecsByKey, row):
    # W team
    wkey = int(row[2])
    recsList = teamRecsByKey.get(wkey, [])
    recsList.append([float(v) for v in [row[3], row[8], row[9], 
                    row[10], row[11], row[12], row[13], row[14], 
                    row[15], row[16], row[17], row[18], row[19], 
                    row[20]]])
    teamRecsByKey[wkey] = recsList
            
    #L team
    lkey = int(row[4])
    recsList = teamRecsByKey.get(lkey, [])
    recsList.append([float(v) for v in [row[5], row[21], row[22], 
                    row[23], row[24], row[25], row[26], row[27], 
                    row[28], row[29], row[30], row[31], row[32], 
                    row[33]]])
    teamRecsByKey[lkey] = recsList    
            
    print '%s_%s' % (wkey, lkey)
    
if __name__ == "__main__":
    # extract stat data for each team
    
    teamRecsByKey = {}
    with open('../data/regular_season_detailed_results.csv', 'r') as tdf:
        firstRow = True
        for row in csv.reader(tdf):
            if firstRow:
                firstRow = False
                continue
            
            extractTeamsStats(teamRecsByKey, row)
            
    with open('../data/tourney_detailed_results.csv', 'r') as tdf:
        firstRow = True
        for row in csv.reader(tdf):
            if firstRow:
                firstRow = False
                continue
            
            extractTeamsStats(teamRecsByKey, row)
    
    #agregate
    print 'agregate'
    
    teamStatsByKey = {}
    for k, v in teamRecsByKey.iteritems():
        teamStatsByKey[k] = np.sum(v, axis=0, dtype=np.float) / len(v)
            
    pickle.dump(teamStatsByKey, open('../localdata/teamStatsByKey.pkl', 'wb'))
