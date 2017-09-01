import nltk
from nltk import probability
from nltk.corpus import stopwords
import pandas as pd
import json
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import os
from os import path
import csv
from pandas import Series


basePath = "fetchedComments/RF_years"
files = [f for f in os.listdir(basePath) if f.endswith('.json')]
print files
print len(files)

fd = open("output_csv/RF_years.csv",'w')	

for i in xrange(len(files)):
	#print str(basePath) + '/' + str(files[i])
	open_file = pd.read_json("fetchedComments/RF_years/"+ str(files[i]))
	#open_file = pd.read_json(files[i])
	
	#print files[i]
	print "......................"
	pos_words = 0
	neg_words = 0
	neutral = 0
	stop_eng = stopwords.words('english')
	customstopwords = []
	tokens = []
	sentences =[]
	tokenizedSentences = []
	counter_lines = 0
	filter_words = ['roger', 'federer', 'he', 'his']
	if not (open_file.empty):
		for text in open_file.text:
			sentences.append(text.lower())
			stopwords_mine = [u'\ufeff']
			statement = (sentences[0])
			print statement

			if any(word in statement for word in filter_words ):
				time = open_file.publishedAt[counter_lines].split('T')
				fd.write(time[0])
				fd.write(',')
				a = TextBlob(statement).sentiment
				print str(a[0])
				fd.write(str(a[0]))
				fd.write('\n')
			
			sentences = []
			counter_lines +=1
			
		counter_lines = 0
		
fd.close()
	
	
