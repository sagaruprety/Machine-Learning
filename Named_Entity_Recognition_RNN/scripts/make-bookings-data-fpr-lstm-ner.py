import time 
import random
data_file = 'new_dataset-bookings-hotel-'+str(time.time())+'.txt'
f = open(data_file, 'w')
from product_list import hotels
hotel = {'text': ['book(intent) hotel(activity) ']}
f_read = open(hotels['target'], 'r')
hotel_listings = []
file = []

for i in f_read:
	file.append(i)

for i in range(len(file)):
	if '*' in file[i]:
		rest_tuple = []
		for j in range(3):
			i+=1
			to_add = file[i].split(':')[1].replace('\n', '').split()
			if j!=0:
				word_to_add = ''
				for word in to_add:
					word_to_add = word_to_add+word +'(loc) '
				rest_tuple.append(word_to_add)
			else:
				word_to_add = ''
				for word in to_add:
					word_to_add = word_to_add+word+'(listing) '
				rest_tuple.append(word_to_add)
		hotel_listings.append(tuple(rest_tuple))


break_flag = False
for text in hotel['text']:
	break_flag = False
	#for conjunction in doctors['conjunctions']:
		#rest_count = 0
	random.shuffle(hotel_listings)
	for rest in hotel_listings:
		if random.random()>0.3:
			f.write(text+rest[0]+' '+rest[1]+'\n')
		else: continue
			#rest_count+=1