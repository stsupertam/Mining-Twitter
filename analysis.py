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
        
    d = OrderedDict(sorted(total.items(), key=itemgetter(1), reverse=True))
    #print d.values()[0]
    if d.values()[0] == 0:
        return "Unknown"
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
    tweets['text'] = map(lambda tweet: tweet.get('text', None), tweets_data)
    tweets['id'] = map(lambda tweet: tweet.get('id', None), tweets_data)
    tweets['link'] = map(lambda tweet: tweet.get('permalink', None), tweets_data)
    tweets['tag'] = tweets['text'].apply(lambda tweet: group_tweet(tweet))
    tweets['attention'] = map(lambda tweet: tweet.get('attention', None), tweets_data)

    crime = tweets['tag'].str.contains('crimes')    
    environment = tweets['tag'].str.contains('environment')    
    education = tweets['tag'].str.contains('education')
    families = tweets['tag'].str.contains('families')
    unknown = tweets['tag'].str.contains('unknown')

    tweets[crime].to_csv("crime_out.csv", index=False)
    tweets[environment].to_csv("environment_out.csv", index=False)
    tweets[education].to_csv("education_out.csv", index=False)
    tweets[families].to_csv("families_out.csv", index=False)
    tweets[unknown].to_csv("unknown_out.csv", index=False)

if __name__ == '__main__':
    main(sys.argv[1:])
