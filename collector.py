# -*- coding: utf-8 -*- 
import got 
import json 
import codecs

def main(): 
	
	def receiveBuffer(tweets):
		for t in tweets:
			outputFile.write(('\n%s;%s;%d;%d;"%s";%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.id)))
		outputFile.flush();
		print 'More %d saved on file...\n' % len(tweets)
		

	tweetCriteria = got.manager.TweetCriteria().setUsername("realDonaldTrump") 
	outputFile = codecs.open("output.csv", "w+", "utf-8")
	outputFile.write('username;date;retweets;favorites;text;id')
	print 'Searching...\n'
	
	got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
	outputFile.close()
	print 'Done. Output file generated "output_got.csv".'

if __name__ == '__main__':
	main() 
