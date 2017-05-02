# -*- coding: utf-8 -*-

import sys
import csv
import os.path
import re
import numpy
import json
import pandas as pd
import matplotlib.pyplot as plt


def main(argv):

    length = len(argv)
    if length == 0:
        print 'Plese input data file.'
        return

    filename = "./dataset/" + argv[0]
    tweets_data = []
    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                try:
                    count = count + 1
                    tweets_data.append(row)
                    if count % 100 == 0:
                        sys.stdout.write('.')
                    if count % 5000 == 0:
                        sys.stdout.write('\n')
                except Exception as e:
                    print e
                    continue
    except Exception as e:
        print e
        return

    print '\n'
    tweets = pd.DataFrame()
    tweets['date'] = map(lambda tweet: tweet.get('date', None), tweets_data)
    tweets['attention'] = map(lambda tweet: tweet.get('attention', None), tweets_data)
    tweets['text'] = map(lambda tweet: tweet.get('text', None), tweets_data)
    tweets['tag'] = map(lambda tweet: tweet.get('tag', None), tweets_data)
    print tweets.head()

if __name__ == '__main__':
    main(sys.argv[1:])
