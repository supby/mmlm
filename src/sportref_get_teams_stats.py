#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrej"
__date__ = "$Mar 4, 2015 9:42:21 PM$"

import cPickle as pickle
import csv
from pyquery import PyQuery as pq

__GET_STAT_URL_FORMAT = 'http://www.sports-reference.com/cbb/seasons/{0}-advanced-school-stats.html'

__OUT_FILE_PATH_FORMAT = '../data/cbbref/ts_{0}.csv'

if __name__ == "__main__":
    
    seasons = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
    
    for season in seasons:
        d = pq(url=__GET_STAT_URL_FORMAT.format(season))
        with open(__OUT_FILE_PATH_FORMAT.format(season), 'w') as outcsv:
            
            ths = d('table#adv_school_stats thead tr:eq(1) th')
            heder_row = [ths[i].text.strip() for i in range(len(ths)) 
                if ths[i].text and ths[i].text.strip()]
            
            writer = csv.writer(outcsv)
            writer.writerow(heder_row)
            
            trs = d('table#adv_school_stats tbody tr')
            for i in range(len(trs)):
                tr = trs[i]
                if tr.attrib['class']:
                    continue
                    
                tds = pq(tr)('td')
                row = []
                for j in range(len(tds)):
                    td = tds[j]
                    val = pq(td)('a')[0].text if j == 1 else td.text
                    if val:
                        row.append(val.strip())
                
                writer.writerow(row)
                
            print 'season => %s' % season
            
            
            
            
    
    
