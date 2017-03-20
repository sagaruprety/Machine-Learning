27f = open('new_dataset-tickets.txt', 'a')
import random
from product_list import flights
###print flights
f_read   = open(flights['target'], 'r')
city_list = []
for city_flight in f_read:
			city_list.append(city_flight.replace('\n', ' '))
random.shuffle(city_list)
random_skip = 0.1
break_flag = False
for text in flights['text']:
	#print text
	break_flag = False
	#if break_flag:break
	for conjunction in flights['conjunctions1']:
		city1_count = 0
		break_flag = False
		random.shuffle(city_list)
		for city1 in city_list:
			if city1_count > 1:
				break_flag = True
			else:
				break_flag = False
			if break_flag: 
				city1_count = 0
				continue
			#if random.random()<random_skip:
			#	continue
			#print city1
			city1_count+=1
			#print city1_count
			for join1 in [' to(preposition) ']:
				break_flag = False
				city2_count = 0
				random.shuffle(city_list)
				for city2 in city_list:
					if city2_count > 1:
						break_flag = True
					else: break_flag = False
					if break_flag: 
						city2_count  = 0
						break
					#if random.random()<random_skip:
					#	continue
					if city1==city2:
						continue
					city2_count+=1
					#print city2
					break_flag = False
					for connector in [' on(preposition) ', ' for(preposition) ']:
						if break_flag:break
						if random.random()<random_skip:
							continue
						date1_count = 0
						random.shuffle(flights['dates'])
						for date1 in flights['dates']:
							if date1_count>4:break_flag=True
							if break_flag:break
							if random.random()<random_skip:
								continue
							#print date1
							date1_count+=1
							month1_count=0
							random.shuffle(flights['months'])
							for month1 in flights['months']:
								if month1_count>4:break_flag=True
								if break_flag:break
								if random.random()<random_skip:
									continue
								#print month1
								month1_count+=1
						# day1_count = 0
						# random.shuffle(flights['day'])
						# for day1 in flights['day']:
						# 	if break_flag:break
						# 	if day1_count>2: 
						# 		break_flag = True
						# 		break
						# 	if random.random<0.25:continue
						# 	day1_count+=1
						 		for join2 in [' and(conjunction) return(other) on(preposition) ', ' return(other) ', ' and(conjunction) return(other) ticket(noun) of(preposition) ']:
									if break_flag:break
								# day2_count = 0
								# random.shuffle(flights['day'])
								# for day2 in flights['day']:
								# 	if break_flag:break
								# 	if day2_count>2:
								# 		break_flag = True
								# 		break
								# 	if random.random<0.15 or day1==day2:continue
								# 	day2_count+=1
								# 	f.write(text+conjunction+city1+join1+city2+connector+day1+join2+day2+'\n')	

											# #print join2
									date2_count = 0
									random.shuffle(flights['dates'])
									for date2 in flights['dates']:
										if date2_count>4: break_flag = True
										if break_flag:break
										if random.random()<random_skip:
											continue
										if date1>=date2:
											continue
										#print date2
										date2_count+=1
										month2_count = 0
										random.shuffle(flights['months'])
										for month2 in flights['months']:
											if month2_count > 4: break_flag = True
											if break_flag:break
											if random.random()>0.005:
												month2_count+=1
												f.write(text+conjunction+city1+join1+city2+connector+str(date1)+' '+month1+join2+str(date2)+' '+month2+'\n')

