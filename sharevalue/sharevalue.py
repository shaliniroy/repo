#!/usr/bin/env python

import urllib2
import sys

def share(symbol):
    try:
        b = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')
        a = float(b.read())
        if a == 0.00:
            print "wrong nasdaq symbol"
        else:
            print "the current share value is %f" % (a)
    except:
        print "something went wrong or internet connection not available or url not opening"

if __name__ == '__main__':
        if len(sys.argv) !=2:
                print "incorrect entry"
                sys.exit(1)
        else:
                share(sys.argv[1])
                sys.exit(1) 
