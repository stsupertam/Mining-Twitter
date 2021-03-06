# -*- coding: utf-8 -*-

import sys
import getopt
import got
import datetime
import codecs
import json
import re
import getopt
from collections import OrderedDict
from operator import itemgetter
from timeit import default_timer as timer

i = 0

def find_tag(text, dictionary):
    
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

    if len(argv) == 0:
        print 'You must pass some parameters. Use \"-h\" to help.'
        return

    if len(argv) == 1 and argv[0] == '-h':
        print """\nTo use this jar, you can pass the folowing attributes:
    username: Username of a specific twitter account (without @)
       since: The lower bound date (yyyy-mm-aa)
       until: The upper bound date (yyyy-mm-aa)
 querysearch: A query text to be matched
   maxtweets: The maximum number of tweets to retrieve

 \nExamples:
 # Example 1 - Get tweets by username [barackobama]
 python exporter.py --username "barackobama" --maxtweets 1\n

 # Example 2 - Get tweets by query search [europe refugees]
 python exporter.py --querysearch "europe refugees" --maxtweets 1\n

 # Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']
 python exporter.py --username "realDonaldTrump ‏" --since 2015-09-10 --until 2015-09-12 --maxtweets 1\n
 
 # Example 4 - Get the last 10 top tweets by username
 python exporter.py --username "realDonaldTrump ‏" --maxtweets 10 --toptweets\n"""
        return

    try:
        opts, args = getopt.getopt(argv, "", ("username=", "since=", "until=",
                                              "querysearch=", "toptweets",
                                              "maxtweets=", "output="))

        output = "./dataset/output"
        tweetCriteria = got.manager.TweetCriteria()

        for opt, arg in opts:
            if opt == '--username':
                tweetCriteria.username = arg

            elif opt == '--since':
                output = "./dataset/output_" + arg + ".csv"
                tweetCriteria.since = arg

            elif opt == '--until':
                tweetCriteria.until = arg

            elif opt == '--querysearch':
                tweetCriteria.querySearch = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = True

            elif opt == '--maxtweets':
                tweetCriteria.maxTweets = int(arg)

            elif opt == '--output':
                output = "./dataset/" + arg

        outputFile = codecs.open(output, 'w', 'utf-8') 

        outputFile.write(
            'username;date;attention;id;permalink;tag;text'
        )
        print 'Searching...\n'

        data = {}
        with open('mykeyword.json') as data_file:    
            data = json.load(data_file)

        def receiveBuffer(tweets):
            for t in tweets:
                attention = t.retweets + t.favorites + 1
                tag = find_tag(t.text, data)
                outputFile.write(
                    ('\n%s;%s;%d;%s;%s;%s;"%s"' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"),
                                       attention, t.id, t.permalink, tag, t.text )))
            outputFile.flush()
            global i
            i += 100
            print 'More %d saved on file...' % len(tweets)
            print 'Totaltweets %d...\n' % i

        got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

    except arg:
        print 'Arguments parser error, try -h' + arg
    finally:
        print 'Done. Output file generated "%s".' % output


if __name__ == '__main__':
    start = timer()
    main(sys.argv[1:])
    end = timer()
    print(end - start)     
