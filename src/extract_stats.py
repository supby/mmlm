# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 6, 2015 11:46:06 PM$"

import cPickle as pickle
import csv
import itertools
import numpy as np
from operator import itemgetter
from operator import add

loc2feature = {'N': 0, 'H': 1, 'A': 2}

def extract_data_rows(row):    
    locFeature = loc2feature[row[6]]
    # W team    
    wkey = row[2]
    yield [float(v) for v in [row[0], wkey, row[1], row[3], row[7], 
        row[8], row[9], row[10], row[11], row[12], 
        row[13], row[14], row[15], row[16], row[17], 
        row[18], row[19], row[20]] + [locFeature]]   
            
    #L team  
    lkey = row[4]
    yield [float(v) for v in [row[0], lkey, row[1], row[5], row[7], row[21], 
        row[22], row[23], row[24], row[25], row[26], row[27], 
        row[28], row[29], row[30], row[31], row[32], 
        row[33]] + [locFeature]]    
            
    print 'extract_data_rows => %s_%s' % (wkey, lkey)
    
def extract_teams_stats(teamRecsByKey, row):
    locFeature = loc2feature[row[6]]
    # W team
    wkey = int(row[2])
    recsList = teamRecsByKey.get(wkey, [])
    recsList.append([float(v) for v in [row[1], row[3], row[7], 
                    row[8], row[9], row[10], row[11], row[12], 
                    row[13], row[14], row[15], row[16], row[17], 
                    row[18], row[19], row[20]] + [locFeature]])
    teamRecsByKey[wkey] = recsList
            
    #L team
    lkey = int(row[4])
    recsList = teamRecsByKey.get(lkey, [])
    recsList.append([float(v) for v in [row[1], row[5], row[7], row[21], 
                    row[22], row[23], row[24], row[25], row[26], row[27], 
                    row[28], row[29], row[30], row[31], row[32], 
                    row[33]] + [locFeature]])
    teamRecsByKey[lkey] = recsList    
            
    print '%s_%s' % (wkey, lkey)
    
if __name__ == "__main__":
    # extract stat data for each team
    
#    team_recs_by_key = {}
#    data = []
#    with open('../data/regular_season_detailed_results.csv', 'r') as tdf:
#        first_row = True
#        for row in csv.reader(tdf):
#            if first_row:
#                first_row = False
#                continue
#            
#            for li in extract_data_rows(row):                
#                data.append(li)
##            extract_teams_stats(teamRecsByKey, row)
#            
#    with open('../data/tourney_detailed_results.csv', 'r') as tdf:
#        first_row = True
#        for row in csv.reader(tdf):
#            if first_row:
#                first_row = False
#                continue
#                
#            for li in extract_data_rows(row):                
#                data.append(li)
##            extract_teams_stats(teamRecsByKey, row)
#    
#    pickle.dump(data, open('../localdata/ts_data.pkl', 'wb'))
    
    data = pickle.load(open('../localdata/ts_data.pkl', 'rb'))
    
    print np.shape(data)
    
    print 'agregate'
    
    gr = itertools.groupby(data, key=itemgetter(0, 1))
    ts_by_season_key = {}
    for k, v in gr:
        l = list(v)
        ln = len(l)
        ts_by_season_key[k] = [float(r) / ln for r in reduce(lambda x1, x2: map(add, x1, x2), 
                                                [vi[2:] for vi in l])]
    
    
    pickle.dump(ts_by_season_key, open('../localdata/tstat_by_season_key.pkl', 'wb'))
    
#    team_stats_by_key = {}
#    for k, v in team_recs_by_key.iteritems():
#        team_stats_by_key[k] = np.sum(v, axis=0, dtype=np.float) / len(v)
#            
#    pickle.dump(team_stats_by_key, open('../localdata/teamStatsByKey.pkl', 'wb'))
