# -*- coding: utf-8 -*-

import sys
import csv
import os.path
import re
import numpy
import json
import pandas as pd
import matplotlib.pyplot as plt
from mykeyword import dictionary
from collections import OrderedDict
from operator import itemgetter


def create_outputfile(df, tag):

    t = df['tag'].str.contains(tag)
    output = tag + "_out.csv"
    if os.path.exists(output):
        df[t].to_csv(output, mode='a', header=False, index=False)
    else:
        df[t].to_csv(output, index=False)


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

    d = OrderedDict(sorted(total.items(), key=itemgetter(1), reverse=True))
    #print d.values()[0]
    if d.values()[0] == 0:
        return "unknown"
    else:
        return d.keys()[0]


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

    print '\n'
    tweets = pd.DataFrame()
    tweets['date'] = map(lambda tweet: tweet.get('date', None), tweets_data)
    tweets['attention'] = map(lambda tweet: tweet.get('attention', None),
                              tweets_data)
    tweets['text'] = map(lambda tweet: tweet.get('text', None), tweets_data)
    tweets['tag'] = tweets['text'].apply(lambda tweet: group_tweet(tweet))

    create_outputfile(tweets, 'crimes')
    create_outputfile(tweets, 'environment')
    create_outputfile(tweets, 'families')
    create_outputfile(tweets, 'education')
    create_outputfile(tweets, 'government')
    create_outputfile(tweets, 'unknown')


if __name__ == '__main__':
    main(sys.argv[1:])
