# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 6, 2015 11:46:06 PM$"

import cPickle as pickle
import csv
import itertools
from operator import add
from operator import itemgetter

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
    
if __name__ == "__main__":
    # extract stat data for each team
    
    team_recs_by_key = {}
    data = []
    with open('../data/regular_season_detailed_results.csv', 'r') as tdf:
        first_row = True
        for row in csv.reader(tdf):
            if first_row:
                first_row = False
                continue
            
            for li in extract_data_rows(row):                
                data.append(li)
            
    with open('../data/tourney_detailed_results.csv', 'r') as tdf:
        first_row = True
        for row in csv.reader(tdf):
            if first_row:
                first_row = False
                continue
                
            for li in extract_data_rows(row):                
                data.append(li)
                
    with open('../data/regular_season_detailed_results_2015.csv', 'r') as tdf:
        first_row = True
        for row in csv.reader(tdf):
            if first_row:
                first_row = False
                continue
                
            for li in extract_data_rows(row):                
                data.append(li)
    
    pickle.dump(data, open('../localdata/ts_data.pkl', 'wb'))
    
    data = pickle.load(open('../localdata/ts_data.pkl', 'rb'))
    
    print 'Agregate.'    
    
#    seasons_to_predict = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 
#        2010, 2011, 2012, 2013, 2014, 2015]
    seasons_to_predict = [2015]
#    seasons_to_predict = [2010, 2011, 2012, 2013, 2014]
    
    ts_by_season_key = {}
    for season in seasons_to_predict:        
#        gr = itertools.groupby([d for d in data if int(d[0]) < season], 
#                                key=itemgetter(1))
        gr = itertools.groupby([d for d in data if int(d[0]) == season - 1], 
                               key=itemgetter(1))
        for k, v in gr:
            print "agregate => %s,%s" % (season, k)
            l = list(v)
            ln = len(l)
            ts_by_season_key[(float(season), k)] = [float(r) / ln for r in 
                reduce(lambda x1, x2: map(add, x1, x2), 
                       [vi[2:] for vi in l])]
    
pickle.dump(ts_by_season_key, open('../localdata/team_stats.pkl', 'wb'))

