import numpy as np
import re
from nltk.tag import StanfordNERTagger
import time
start_time = time.time()
st = StanfordNERTagger('/Users/sagaruprety/Downloads/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/sagaruprety/Downloads/stanford-ner-2015-12-09/stanford-ner.jar')
data_dir = '/Users/sagaruprety/Downloads/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled/'
file_name_prefix = data_dir+'news.en-0000'
file_name_postfix = '-of-00100'
date = [str(w+1) for w in range(31)]
date_modified = []
#all_cities = np.load('all_cities.npy')
#common_20k_words = np.load('common_20k_words.npy')
#Create list of all dates
for num in date:
	if int(num)%10==1:
		date_modified.append(num+'st'+'' )
		continue
	elif int(num)%10==2:
		date_modified.append(num+'nd'+'' )
		continue
	elif int(num)%10==3:
		date_modified.append(num+'rd'+'' )
		continue
	else:
		date_modified.append(num+'th'+'' )

months = ['January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September ',
'October',
'November',
'December',
'january',
'february',
'march',
'april',
'may',
'june',
'july',
'august',
'september ',
'october',
'november',
'december']

day = ['Monday',
'Tuesday',
'Wednesday',
'Thursday',
'Friday',
'Saturday',
'Sunday',
'tomorrow',
'monday',
'tuesday',
'wednesday',
'thursday',
'friday',
'saturday',
'sunday',
'Tomorrow']

f_new_data = open('new_data_google_tags', 'w')
f_new_data_train = open('new_data_google_en', 'w')
print ('Going for it...')
total_loc = 0
total_date = 0
total_listing = 0
counter = 0
for i in range(1):
	print "File "+str(i)
	file_name = file_name_prefix+str(i)+file_name_postfix
	f = open(file_name, 'r')
	for line in f:
		line = re.sub(r'[^A-Za-z0-9 \n\']+', '', line)
		line = re.sub(r'[\s][\s]+', ' ', line)
		line = re.sub(r'[\s][\']', '\'', line)
		line = re.sub(r'[\s][\n]', '', line)
		line = line.strip()
		line+='\n'
		f_new_data_train.write(line)
		tagged_line = st.tag(line.split())
		new_line = ''
		for word,tag in tagged_line:
			if str(tag) == 'O':
				if str(word) in months or word in date_modified or word in day:
					new_line=new_line+'date'+' '
					total_date+=1
				else: new_line=new_line+word+' '
			if str(tag) == 'LOCATION':
				new_line=new_line+'loc'+' '
				total_loc+=1
			if str(tag) == 'ORGANIZATION':
				new_line=new_line+'listing'+' '
				total_listing+=1
			if str(tag) == 'PERSON':
				new_line=new_line+'listing'+' '
				total_listing+=1 
				
		new_line+='\n'
		new_line = re.sub(r'[\s][\n]', '\n', new_line)
		f_new_data.write(new_line)
		counter+=1
		if counter%100==0:
			print "Lines scanned- "+str(counter)
			print "Locations replaced- "+str(total_loc)
			print "Listings replaced- "+str(total_listing)
			print "Dates replaced- "+str(total_date)
			print "Time elapsed- "+str(time.time() - start_time)+" seconds"
f_new_data.close()
f.close()




