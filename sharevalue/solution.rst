Objective
=========
Write a python script to print the latest share value of a company whose NASDAQ symbol would be given as command line arguement.

The python program can be executed by using:-

::

    $ python sharevalue.py [Nasdaq Symbol]

or

::

    $ chmod +x sharevalue.py
    $ ./sharevalue.py [Nasdaq Symbol]

The coded program is given at the `link <https://github.com/shaliniroy/repo/blob/master/sharevalue/sharevalue.py>`_

Explnation of the code
----------------------

::

    #!/usr/bin/env python

    import urllib2     # the module is imported for opening url
    import sys         # sys module is imported for command line arguments

    def share(symbol):     # The function is defined for opening and reading the url, and for printing sharevalue
        try:               # Used for handle exception and error may be due to problems like url not opening
            b = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')     # opens the url
            a = float(b.read())                   # Reads the url
            if a == 0.00: # if any wrong symbol is entered then it print the sharevalue zero , which is not right, so removing it by if-else statement
                print "wrong nasdaq symbol"
            else:
                print "The current sharevalue is %f" % (a)
        except:
            print "something went wrong or internet connection not available or url not opening"

    if __name__ == '__main__':  
            if len(sys.argv) !=2:
                    print "incorrect entry"
                    sys.exit(1)
            else:
                    share(sys.argv[1])
                    sys.exit(1)
