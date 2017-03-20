import random
f1 = open('../auxillary-data/new-flight-data.txt', 'r')
f2 = open('travel.txt', 'r')
f3 = open('travel2.txt', 'w')
# for line in f1:
# 	if 'flight tickets' in line:
# 		if random.random()<0.18:
# 			line = line.replace('flight ', 'railway ')

# 	elif 'flight ' in line:
# 		if random.random()<0.36:
# 			if random.random()<0.5:
# 				line = line.replace('flight ', 'bus ')
# 			else:
# 				line = line.replace('flight ', 'train ')
# 	elif 'flights' in line:
# 		if random.random()<0.36:
# 			if random.random()<0.5:
# 				line = line.replace('flights', 'bus')
# 			else:
# 				line = line.replace('flights', 'trains')
# 	f2.write(line)
cities = open('../data/flights.txt')
city_list = []
for city in cities:
	city_list.append(city)
for line in f2:
	if 'Pp' in line:
		line = line.replace('Pp', random.choice(city_list).split('\n')[0])
	if 'Kk' in line:
		line = line.replace('Kk', random.choice(city_list).split('\n')[0])
	f3.write(line)