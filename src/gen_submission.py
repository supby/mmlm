#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Feb 7, 2015 11:08:40 PM$"

import cPickle as pickle
import csv
from sklearn import preprocessing
import numpy

def get_dif(wteam, lteam):
    return [wteam[i] - lteam[i] for i in range(len(wteam))]

if __name__ == "__main__":
    
    #load sample submission
    games2predict = []
    with open('../data/sample_submission_2015.csv', 'r') as incsv:
        with open('../localdata/submission1.csv', 'w') as outcsv:            

            ts_by_season_key = pickle.load(open('../localdata/team_stats.pkl', 'rb'))
            clf = pickle.load(open('../localdata/lr_model.pkl', 'rb'))            
            
            writer = csv.writer(outcsv)
            firstRow = True
            writer.writerow(['id', 'pred'])
            
            data_to_predict = []
            idsl = []
            for row in csv.reader(incsv):
                if firstRow:
                    firstRow = False
                    continue
                
                idsl.append(row[0])
                ids = row[0].split('_')
                wkey = int(ids[1])
                lkey = int(ids[2])
                season = ids[0]
                
                wteam = ts_by_season_key[(float(season),float(wkey))]
                lteam = ts_by_season_key[(float(season),float(lkey))]
                
                diff = get_dif(wteam, lteam)
                data_to_predict.append(diff)
                
            print 'Scaling the data.'                
            data_to_predict = numpy.mat(preprocessing.MinMaxScaler()
                                            .fit_transform(data_to_predict), 
                                            numpy.float32)
                           
            probs = clf.predict_proba(data_to_predict)            
            for i in range(len(probs)):
                p = probs[i]
                writer.writerow([idsl[i], '{:.9f}'.format(p[1])])
                print '%s_%s_%s => %.9f' % (ids[0], wkey, lkey, p[1])
                
                
                    
                
