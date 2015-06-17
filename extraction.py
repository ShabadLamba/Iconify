import nltk
from pprint import pprint
from re import sub

def extraction(string):
	tokens = nltk.word_tokenize(string)
	tagged = nltk.pos_tag(tokens)
	parse = '' 
	for item in tagged:
		for words in item:
			parse = parse + " " + words
	parse = parse.split (' ')
	noun_list = []
	for index,item in enumerate(parse):
		if (item == 'NNP' or item =='NN'):
			noun_list.append(parse[index-1])
	print noun_list
	return noun_list