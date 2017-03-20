import numpy as np
f = open('../data/worldcitiespop.txt', 'r')
all_cities = []
for line in f:
	all_cities.append(line.split(',')[1])
np.save('all_cities.npy', all_cities)
f.close()