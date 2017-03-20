f = open('new_dataset-tickets2.txt', 'a')
import random
from product_list_new import flights
f_read   = open(flights['airports'], 'r')
city_list = []
for city_flight in f_read:
			city_list.append(city_flight.replace('\n', ' '))

date = [str(w+1) for w in range(31)]
date_modified = []
for num in date:
	if int(num)%10==1:
		date_modified.append(num+'st'+'' )
		continue
	elif int(num)%10==2:
		date_modified.append(num+'nd'+'' )
		continue
	elif int(num)%10==3:
		date_modified.append(num+'rd'+'' )
		continue
	else:
		date_modified.append(num+'th'+'' )

count = [str(i+1) for i in range(3)]


months = ['January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September ',
'October',
'November',
'December']

day = ['Monday ',
'Tuesday ',
'Wednesday ',
'Thursday ',
'Friday ',
'Saturday ',
'Sunday ',
'next Sunday',
'next Friday ',
'next Wednesday ',
'tomorrow',
'next day',
'next evening',
'tomorrow morning']

counter  = 0
break_flag = False
new_data_list = []
random.shuffle(flights['text2'])
for i in range(4000):
	for text in flights['text2']:
		city1_count = 0
		random.shuffle(city_list)
		for city1 in city_list:
			if city1_count==1:break
			if random.random()<0.2:continue
			if '#' in text: new_text_city1 = text.replace('#', city1,1)
			else:
				new_text_city1 = text
				#new_data_list.append(new_text_city1)
				#break
			city1_count+=1
			random.shuffle(city_list)
			city2_count = 0
			for city2 in city_list:
				if(city2_count==1):break
				if random.random()<0.2 or city1==city2:continue
				if '#' in new_text_city1: new_text_city2 = new_text_city1.replace('#', city2)
				else:
					new_text_city2 = new_text_city1
					#new_data_list.append(new_text_city2)
					#break
				city2_count+=1
				date1_count = 0
				for date1 in date_modified:
					if(date1_count==1):break
					if random.random()<0.7:continue
					if '*' in new_text_city2: new_text_date1 = new_text_city2.replace('*', date1,1)
					else:
						new_text_date1 = new_text_city2
						#new_data_list.append(new_text_date1)
						#break
					date1_count+=1
					month1_count = 0
					for month1 in months:
						if(month1_count==1):break
						if random.random()<0.4:continue
						if '&' in new_text_date1: new_text_month1 = new_text_date1.replace('&', month1,1)
						else:
							new_text_month1 = new_text_date1
							#new_data_list.append(new_text_month1)
							#break
						month1_count+=1
						day1_count = 0
						for day1 in day:
							if(day1_count==1):break
							if random.random()<0.2:continue
							if '$' in new_text_month1: new_text_day1 = new_text_month1.replace('$', day1,1)
							else:
								new_text_day1 = new_text_month1
								#new_data_list.append(new_text_day1)
								#break
							day1_count+=1
							random.shuffle(day)
							random.shuffle
							random.shuffle(months)
							date2_count=0
							for date2 in date_modified:
								if(date2_count==1):break
								if random.random()<0.7 or date1 == date2:continue
								if '*' in new_text_day1: new_text_date2 = new_text_day1.replace('*', date2)
								else:
									new_text_date2 = new_text_day1
									#new_data_list.append(new_text_date2)
									#break
								date2_count+=1
								day2_count = 0
								for day2 in day:
									if(day2_count>=1):break
									if random.random()>0.2 or day1 == day2:continue
									if '$' in new_text_date2: new_text_day2 = new_text_date2.replace('$', day2)
									else:
										new_text_day2 = new_text_date2
										#new_data_list.append(new_text_day2)
										#break
									day2_count+=1
									month2_count = 0

									for month2 in months:
										break_flag = False
										if(month2_count>=1):break
										if random.random()<0.4:continue
										if '&' in new_text_day2: new_text_month2 = new_text_day2.replace('&', month2)
										else:
											new_text_month2 = new_text_day2
											#new_data_list.append(new_text_month2)
											#break
										month2_count+=1
										for count1 in count:
											if break_flag: break
											if '@' in new_text_month2: new_text_count1 = new_text_month2.replace('@', count1,1)
											else:
												new_text_count1 = new_text_month2
												new_data_list.append(new_text_count1)
												break_flag = True
												break
											random.shuffle(count)
											for count2 in count:
												if break_flag: break
												if '@' in new_text_count1: new_text_count2 = new_text_count1.replace('@', count2,1)
												else:
													new_text_count2 = new_text_count1
													new_data_list.append(new_text_count2)
													break_flag = True
													break
												random.shuffle(count)
												for count3 in count:
													if break_flag: break
													#if(counter%10000 == 0): print counter
													if '@' in new_text_count2:
														new_text_count3 = new_text_count2.replace('@', count3)
														new_data_list.append(new_text_count3)
														break_flag = True
														break
														counter+=1
													else:
														new_text_count3 = new_text_count2
														new_data_list.append(new_text_count3)
														break_flag = True
														break
												

f = open('new-flight-data2.txt', 'w')
for i in new_data_list:
	f.write(i+'\n')
f.close()

