import random
f1 		 = open('../auxillary-data/bookings_without_pos.txt', 'r')
f2 		 = open('../auxillary-data/directions_without_pos.txt', 'r')
f3 		 = open('../auxillary-data/flights_without_pos.txt', 'r')
#f5 		 = open('../auxilary-data/others.txt', 'r')
f_en  	 = open('english.txt', 'w')
f_ner    = open('ner-tags.txt', 'w')
all_data = []

for line in f1:
	all_data.append(line)
for line in f2:
	all_data.append(line)
for line in f3:
	all_data.append(line)

random.shuffle(all_data)
#print len(all_data)
for line in all_data:
	new_line_en = ''
	new_line_ner  = ''
	words_in_line = line.split()
	for word in words_in_line:
		words = word.split('(')
		#print words
		new_line_en+=words[0]+' '
		if(len(words)>1):
			new_line_ner+=words[1].replace(')', '')+' '
		else: new_line_ner+='loc '
	f_en.write(new_line_en+'\n')
	f_ner.write(new_line_ner+'\n')
