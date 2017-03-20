import random
import time
#from product_list import maps
maps = {
		'text':[
			'how to get to *',
			'how to reach *',
			'quickly take me to *',
			'how can I go to *',
			'travel to *',
			'can you take me to *',
			'where can I find *',
			'where is *',
			'how far is *',
			'can you tell me the distance to *',
			'show me the distance to *',
			'can you give me directions to *',
			'I have to travel to *',
			'I have to go to *',
			'which way to *',
			'what is the way to reach *',
			'show me the way to reach *',
			'I want to reach * quickly',
			'* driving directions',
			'I want to travel to *',
			'please take me to *'
		]
	}
f1 = open('../data/listings_filtered_unique.txt', 'r')
f2 = open('../data/localities_sorted_unique.txt', 'r')
f3 = open('../data/cities.txt', 'r')
data_file = 'new-dataset-directions2-'+str(time.time())+'.txt'
f4 = open(data_file, 'w')
directions_list = []
for line in f1:
	line = line.replace('\n','')
	listing = ''
	words = line.split()
	for word in words:
		listing=listing+word+ ' '
	directions_list.append(listing)

i = 0
for line in f2:
	line = line.replace('\n','')
	listing = ''
	words = line.split()
	for word in words:
		listing=listing+word+' '
		#print listing
	directions_list.append(listing)
for line in f3:
	directions_list.append(line.replace('\n',''))

random.shuffle(directions_list)

for i in range(4000):
	for text in maps['text']:
		text = text.replace('*',random.choice(directions_list))
		f4.write(text+'\n')


