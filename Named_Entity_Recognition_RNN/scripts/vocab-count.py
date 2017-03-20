import collections
import numpy as np
f1 = open('../ner-tagged-data.txt', 'r')
f2 = open('../en-data.txt', 'r')

words = []
# for line in f1:
# 	split_line = line.split()
# 	for word in split_line:
# 		words.append(word)
# counter  = collections.Counter(words)
# count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
# unique_words1, _ = list(zip(* ))

#print len(unique_words1)
f3 = open('all_words.txt', 'w')
for line in f2:
	split_line = line.replace('\n','').split()
	for word in split_line:
		f3.write(word+'\n')
		#words.append(word)

#print len(np.unique(words))
f3.close()
# counter  = collections.Counter(words)
# count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
# unique_words2, _ = list(zip(*count_pairs))


# print len(unique_words2)
