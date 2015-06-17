import os
import Image

def replaceText(string,noun_list):
	file_list = os.listdir(r"/Users/shabadlamba/fullstack/vagrant/MyProjects/Iconify/images/")
	string =string.split(' ')
	for index,word in enumerate(string):
		if word in noun_list:
			for item in file_list:
				if word.lower() in item:
					print item
					string[index] = "<img src='/static/images/%s' width='40px' />" % (item)
	return ' '.join(string)