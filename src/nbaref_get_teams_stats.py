#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Mar 4, 2015 9:42:21 PM$"

from pyquery import PyQuery as pq
import cPickle as pickle
import csv

__GET_STAT_URL_FORMAT = 'http://www.basketball-reference.com/leagues/NBA_{0}.html'

__OUT_FILE_PATH_FORMAT = '../data/nhlref/ts_{0}.csv'

if __name__ == "__main__":
    
    seasons = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
    
    for season in seasons:
        d = pq(url=__GET_STAT_URL_FORMAT.format(season))
        with open(__OUT_FILE_PATH_FORMAT.format(season), 'w') as outcsv:
            
            ths = d('table#misc thead tr:eq(1) th')
            heder_row = [ths[i].text.strip() for i in range(len(ths))]
            
            writer = csv.writer(outcsv)
            writer.writerow(','.join(heder_row))
            
            trs = d('table#misc tbody tr')
            for tr in trs:
                tds = pq(tr)('td')
                print tds[1].text
                row = [tds[i].text.strip() for i in range(len(tds))]
                writer.writerow(','.join(row))
                
            print 'season => %s' % season
            
            
            
            
    
    
