import numpy as np
import random
import re
# mapping = {
# 	'$': 'locality',
# 	'#': 'listing',
# 	'*': 'category'
# 	}
# other = {
# 	'texts': [
# 	'*',
# 	'* in $',
# 	'* near $',
# 	'# $',
# 	'*',
# 	'I want to buy *',
# 	'buy *',
# 	'get me a list of * in $',
# 	'*'	,
# 	'can you get me *', 
# 	'are there any * in $',
# 	'show me a list of *',
# 	'show me some * in $'
# 	],
# 	'text2': [
# 	'buy tickets for ^',
# 	'book tickets for ^',
# 	'I want to watch ^',
# 	'I want to buy 2 tickets for ^',
# 	'^ movie tickets',
# 	'book tickets for the movie ^',
# 	'get me bookings for ^',
# 	'ticket bookings for ^',
# 	'buy tickets for movie ^',
# 	'buy ^ tickets',
# 	'buy ^ movie tickets',
# 	'book tickets in PVR Cinemas',
# 	'book movie tickets',
# 	'what are the latest movies in town',
# 	'book english movie ticket',
# 	'film tickets',
# 	'movie tickets',
# 	'tickets for 2 people for ^ tomorrow',
# 	'book 2 tickets for ^ at Inox',
# 	'I want to watch the movie ^',
# 	],
# 	'text3': [
# 	'can you book me a !',
# 	'book me a !',
# 	'please book me a !',
# 	'I want to book !',
# 	'can you check out some ! for me',
# 	'I want to book a ! for a party',
# 	'book !',
# 	'tickets for !'],

# 	'text_maps': [
# 			'how to get to $',
# 			'how to reach #',
# 			'can you get me to $',
# 			'quickly take me to $',
# 			'how can I go to $',
# 			'$ pahunchne ka rasta batao',
# 			'$ kaise pahunchna hai',
# 			'$ kaise jana hai',
# 			'mujhe $ jana hai',
# 			'can you show * near me',
# 			'* near me',
# 			'go to $',
# 			'take me to $'
# 		]
# }


# listing = np.load('listings.npy')
# locality = np.load('locality.npy')
# category = np.load('category.npy')

# random.shuffle(locality)
# random.shuffle(listing)
# random.shuffle(category)


# f1 = open('../data/listings_filtered_unique.txt', 'r')
# f2 = open('../data/localities_sorted_unique.txt', 'r')
# f3 = open('../data/categories.txt', 'r')
# f4 = open('others_latest', 'w')

# verticals = ['taxi', 'cab', 'movie', 'comedy show', 'caterer', 'house keeping', 'fruit shops', 'language classes', 'electrician', 'pest control', 'travel agent',  'plumber', 'packers and movers', '',  'workshop ticket',  'movie ticket', 'marriage hall', 'show', 'party hall']
# listing = []
# locality = []
# category = []

# for line in f1:
# 	listing.append(line.replace('\n',''))

# print 'Done with listings'

# for line in f2:
# 	locality.append(line.replace('\n',''))

# print 'Done with localities'

# for line in f3:
# 	category.append(line.replace('\n',''))

# print 'Done with categories'

# np.save('listings.npy', listing)
# np.save('locality.npy', locality)
# np.save('category.npy',category)
# category = []
# # category.append('restaurants')
# # category.append('doctors')
# # category.append('dentists')
# # category.append('hotels')
# category.append('bars')
# category.append('estate agents')
# category.append('salons')
# category.append('beauty parlors')
# category.append('pharmacy shops')
# category.append('general stores')
# category.append('flats')
# movies = []
# f = open('films', 'r')
# for line in f:
# 	movies.append(line.split('\n')[0])

# texts = other['texts']
# new_txt= ''
# for i in range(2000):
# 	for text in texts:
# 		if '#' in text:
# 			new_txt = text.replace('#', random.choice(listing))
# 		else: new_txt = text
# 		if '$' in new_txt:
# 			new_txt = new_txt.replace('$', random.choice(locality))
# 		if '*' in new_txt:
# 			cat = random.choice(category)
# 			if '-' in cat:
# 				if random.random()>0.5:
# 					cat = cat.split('-')[0]
# 				else: cat = cat.split('-')[1]
# 			new_txt = new_txt.replace('*', cat)
# 			new_txt = re.sub(r'[(][A-Za-z0-9 ]+[)]', '', new_txt)
# 		f4.write(new_txt+'\n')

# # for i in range(2000):
# # 	for vert in verticals:
# # 		for text in texts:
# # 			if '!' in text:
# # 				new_txt = text.replace('!', vert)
# # 			new_txt = re.sub(r'[(][A-Za-z0-9 ]+[)]', '', new_txt)
# # 			f4.write(new_txt+'\n')

if __name__ == '__main__':
	listing = np.load('listings.npy')
	locality = np.load('locality.npy')
	category = np.load('category.npy')
	random.shuffle(listing)
	random.shuffle(category)
	random.shuffle(locality)
	print len(listing)
	print len(locality)
	print len(category)
	f4 = open('others_latest_direct', 'w')
	for i in range(80000):
		f4.write(listing[i]+'\n')
	for i in range(5000):
		f4.write(locality[i]+'\n')
	for i in range(20000):
		f4.write(category[i]+'\n')

