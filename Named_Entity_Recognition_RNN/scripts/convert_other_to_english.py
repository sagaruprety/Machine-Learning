f1 = open('train.en', 'r')
f2 = open('train.ner', 'r')
f3 = open('test.en', 'r')
f4 = open('test.ner', 'r')
f5 = open('train2.ner', 'w')
f6 = open('test2.ner', 'w')
f1 = open('english.txt', 'r')
f2 = open('ner-tags.txt', 'r')
f5 = open('ner-tags2.txt', 'w')

def makeWordList(s):
	sent = []
	word = ''
	for c in s:
		if c!=' ' and c!='\n':
			word+=c
		else:
			sent.append(word)
			word = ''

	return sent

while True:
	l1 = (f1.readline())
	l2 = (f2.readline())
	if (l1 == '' or l2 == ''): break
	l1 = makeWordList(l1)
	l2 = makeWordList(l2)
	l3 = [' ']*len(l1)
	for i in range(len(l1)):
		if l2[i] == 'loc' or l2[i] == 'listing' or l2[i] == 'date':
			l3[i] = l2[i]
			continue
		else:
			l3[i] = l1[i]
	f5.write(" ".join(l3)+'\n')


while False:
	l1 = (f3.readline())
	l2 = (f4.readline())
	if (l1 == '' or l2 == ''): break
	l1 = makeWordList(l1)
	l2 = makeWordList(l2)
	l3 = [' ']*len(l1)
	for i in range(len(l1)):
		if l2[i] == 'loc' or l2[i] == 'listing' or l2[i] == 'date':
			l3[i] = l2[i]
			continue
		else:
			l3[i] = l1[i]
	f6.write(" ".join(l3)+'\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
