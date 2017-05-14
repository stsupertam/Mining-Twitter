import nltk
from nltk import PorterStemmer
test = 'this sentence is just a tester set of words'
test_tokenize = nltk.word_tokenize(test)
#test_tokenize = ['this', 'sentence', 'is', 'just', 'a', 'tester', 'set', 'of', 'words', 'killing']
port = PorterStemmer()
for word in test_tokenize:
	print port.stem(word)