import random
f1 = open('new-flight-data.txt', 'r')
f2 = open('../auxillary-data/new_dataset-bookings.txt', 'r')
f3 = open('../auxillary-data/new_dataset-tickets.txt', 'r')
f4 = open('../auxillary-data/new-dataset-directions.txt', 'r')
f5 = open('../total-data.txt', 'w')

total_data = []
for line in f1:
	total_data.append(line)
for line in f2:
	total_data.append(line)
for line in f3:
	total_data.append(line)
for line in f4:
	total_data.append(line)

random.shuffle(total_data)

for line in total_data:
	f5.write(line)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

