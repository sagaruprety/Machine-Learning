import random
f1 = open('english.txt', 'r')
f2 = open('ner-tags.txt', 'r')
en = []
ner = []
f_test_ner = open('test.ner', 'w')
f_test_en = open('test.en', 'w')
f_train_ner = open('train.ner', 'w')
f_train_en = open('train.en', 'w')



# for line in f1:
# 	form_line  = ''
# 	for word in line.split():
# 		form_line+=word+' '
# 	en.append(form_line+'\n')

# for line in f2:
# 	form_line  = ''
# 	for word in line.split():
# 		form_line+=word+'  '
# 	ner.append(form_line+'\n')

# rand_line_numbers = random.sample(range(len(ner)), len(ner)/10)

# for i in range(len(en)):
# 	if i in rand_line_numbers:
# 		f_test_en.write(en[i])
# 		f_test_ner.write(ner[i])
# 	else:
# 		f_train_en.write(en[i])
# 		f_train_ner.write(ner[i])

en = []
for line in f1:
	en.append(line)
ner = []
for line in f2:
	ner.append(line)
c = 0
while c<70000:
	f_test_en.write(en[c])
	f_test_ner.write(ner[c])
	c+=1

while c<len(en):
	f_train_en.write(en[c])
	f_train_ner.write(ner[c])
	c+=1
	

f1.close()
f2.close()
f_test_en.close()
f_train_ner.close()
f_test_ner.close()
f_train_en.close()


