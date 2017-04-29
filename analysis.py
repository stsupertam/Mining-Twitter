# -*- coding: utf-8 -*-

import sys
import csv
import re
import numpy
import json
import pandas as pd
import matplotlib.pyplot as plt
from mykeyword import dictionary
from collections import OrderedDict
from operator import itemgetter

def group_tweet(text):

    total = {}
    for title in dictionary:
        total[title] = 0
        try:
            for word in dictionary[title]:
                word = word.lower()
                text = text.lower()
                match = re.search(word, text)
                if match:
                    total[title] += 1
        except Exception as e:
            print e
            continue
        
    d = OrderedDict(sorted(total.items(), key=itemgetter(1)))
    print d.keys()[3]
    if d.values()[3] == 0:
        return 0
    else:
        if d.keys()[3] == "crimes":
            return 1
        if d.keys()[3] == "environment":
            return 2
        if d.keys()[3] == "families":
            return 3
        if d.keys()[3] == "education":
            return 4
        else:
            return -1

def main(argv):

    length = len(argv)
    if length == 0:
        print 'Plese input data file.'
        return

    filename = argv[0]
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
    
    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet.get('text', None), tweets_data)
    tweets['tag'] = tweets['text'].apply(lambda tweet: group_tweet(tweet))
    for i in tweets['tag']:
        print i
    #print tweets.head()



if __name__ == '__main__':
    main(sys.argv[1:])
