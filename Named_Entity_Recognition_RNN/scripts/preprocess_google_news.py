import time
import re
start_time = time.time()

data_dir = '/Users/sagaruprety/Downloads/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled/'
file_name_prefix = data_dir+'news.en-0000'
file_name_postfix = '-of-00100'
date = [str(w+1) for w in range(31)]
date_modified = []
total_date = 0
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
'December']

day = ['Monday',
'Tuesday',
'Wednesday',
'Thursday',
'Friday',
'Saturday',
'Sunday',
'tomorrow']

#f_new_data_train = open('new_data_google_en30000.txt', 'w')

counter = 0
for i in range(1):
	f_new_data_train = open('new_data_google_en_'+str(i)+'_10000.txt', 'w')
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
		words = line.split()
		for j in range(len(words)):
			if str(words[j]) in months or words[j] in date_modified or words[j] in day:
					words[j]='date'
					total_date+=1
		counter+=1
		if counter%10000==0:
			words.append('.')
			words.append('\n')
			f_new_data_train.write(" ".join(words))
			f_new_data_train.close()
			f_new_data_train = open('new_data_google_en_'+str(i)+'_'+str(counter)+'.txt', 'w')
			print "Lines scanned- "+str(counter)
			print "Dates replaced- "+str(total_date)
			print "Time elapsed- "+str(time.time()-start_time)
		else:
			words.append('.')
			words.append('\n')
			f_new_data_train.write(" ".join(words))
			