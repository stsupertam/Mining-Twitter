# -*- coding: utf-8 -*-

import sys
import csv

def test():
    print 'Hello World'

def main(argv):

    length = len(argv)
    if length == 0:
        print 'Plese input data file.'
        return

    filename = argv[0]
    print filename
    tweets_data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                print "Text : %s\n" % row['text'] 
            except Exception as e:
                print e
                continue



if __name__ == '__main__':
    main(sys.argv[1:])
