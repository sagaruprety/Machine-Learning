flights = {

'text' : ['book(intent) me(pronoun) a(article) flight(activity) ',
'flight(activity) booking(intent) ',
'flight(activity) tickets(noun) ' ,
'flight(activity) ticket(noun) ',
'get(intent) me(pronoun) a(article) flight(activity) ticket(noun) ',
'flight(activity) ticket(noun) ',
'flight(activity) ke(other) tickets(noun) chahiye(other) ',
'flight(activity) book(intent) karni(other) hai(other) ',
'flight(activity) ticket(noun) book(intent) karna(other) hai(other) ',
'I(pronoun) want(intent) to(preposition) fly(activity) ',
'Hey(other) can(other) you(other) get(intent) me(pronoun) flight(activity) tickets(noun) ',
'hi(other) I(pronoun) to(preposition) book(intent) flight(activity) ticket(noun) ',
'can(other) you(other) get(intent) me(pronoun) a(article) flight(activity) ',
'flights(activity) ',
'hey(other) man(other) book(intent) me(pronoun) flight(activity) tickets(noun) ' ],

'conjunctions3': ['2(num-adults) adults(adults) and(conjunction) 1(num-infant) infant(infant) ',
	'3(num-adults) adults(adults) and(conjunction) 2(num-infant) infants(infant) ',
	'2(num-adults) adults(adults) and(conjunction) 1(num-child) child(child) ',
	'1(num-adults) adult(adults) and(conjunction) 2(num-child) children(child) '
	],

'conjunctions1': ['from(preposition) '],

'conjunctions2' : ['to(preposition) ', 'for(preposition) '],

'dates': ['1(date) ', '2(date) ', '3(date) ', '4(date) ', '5(date) ', '6(date) ',
'7(date) ', '8(date) ', '9(date) ', '10(date) ',
 '11(date) ', '12(date) ', '13(date) ', '14(date) ', '15(date) ', '16(date) ', '17(date) ', '18(date) ', '19(date) ', '20(date) ',
 '21(date) ', '22(date) ', '23(date) ', '24(date) ', '25(date) ', '26(date) ', '27(date) ', '28(date) ', '29(date) ', '30(date) ', '31(date) '],

'months' : ['january(month) ',
'february(month) ',
'march(month) ',
'april(month) ',
'may(month) ',
'june(month) ',
'july(month) ',
'august(month) ',
'september(month) ',
'october(month) ',
'november(month) ',
'december(month) '],

'day': ['Monday(day) ',
'Tuesday(day) ',
'Wednesday(day) ',
'Thursday(day) ',
'Friday(day) ',
'Saturday(day) ',
'Sunday(day) ',
'next(day) Sunday(day)',
'next(day) Friday(day) ',
'next(day) Wednesday(day) ',
'tomorrow(day)',
'day(day) after(day) tomorrow(day)',
'next(day) day(day)',
'next(day) evening(day)',
'tomorrow(day) morning(day)'],

'target' : '../data/flights.txt'

}

hotels = {

'text' :['book(intent) room(activity) ',
'get(intent) me(pronoun) a(article) room(activity) ',
'I(pronoun) want(intent) to(preposition) book(intent) a(article) room(activity) ',
'book(intent) a(article) double(other) bed(other) room(activity) ',
'book(intent) me(pronoun) an(article) AC(other) room(activity) ',
'book(intent) two(count) rooms(activity) ',
'room(activity) booking(intent) ',
'hey(other) man(other) can(other) you(other) book(intent) me(pronoun) a(article) room(activity) ',
'hi(other) please(other) book(intent) a(article) room(activity) '],

'conjunctions' :['in(preposition) ', 'at(preposition) '],

'target' : '../data/hotels.txt'

}

cabs = {

'text' :['book(intent) cab(activity) ',
'book(intent) ola(activity) cab(activity) ',
'book(intent) uber(activity) ',
'book(intent) ola(activity) ',
'get(intent) me(pronoun) an(article) uber(activity) ',
'find ola(activity) cab(activity) for(preposition) me(pronoun) ',
'taxi(activity) bookings(intent) ',
'book(intent) a(article) taxi(activity) ',
'find(intent) me(pronoun) a(article) taxi(activity) ',
'book(intent) uber(activity) cabs(activity)',
'book(intent) a(article) cab(activity) online ']

}

doctors = {

'text': ['book(intent) appointment(activity) ',
'book(intent) an(article) appointment(activity) ',
'I(pronoun) want(intent) to(preposition) book(intent) an(article) appointment(activity) ',
'get(intent) me(pronoun) an(article) appointment(activity) ',
'fix(intent) an(article) appointment(activity) ',
'hi(other) please(other) book(intent) a(article) appointment(activity) ',
'hey(other) man(other) book(intent) appointment(activity) ',
'appointment(activity) booking(intent) '
],

'conjunctions' : [' ', 'with(conjunction) ', 'at(preposition) '],

'target': '../data/doctors.txt'

}

restaurants = {

'text': ['book(intent) a(article) table(activity) ',
'book(intent) a(article) table(activity) for(preposition) 2(count) ',
'book(intent) 2(count) tables(activity) ',
'table(activity) booking(intent) for(preposition) 2(count) people(noun) ',
'restaurant(activity) table(activity) booking(intent) ',
'reserve(intent) table(activity) ',
'restaurant(activity) reservations(intent) of(preposition) 2(count) tables(activity) ',
'I(pronoun) want(intent) to(preposition) make(intent) table(activity) reservation(intent) ',
'book(intent) me(pronoun) a(article) table(activity) ',
'reserve(intent) a(article) table(activity) ',
'hey(other) man(other) book(intent) a(article) table(activity) ',
'table(activity) booking(intent) ',
'please(other) reserve(intent) table(activity) ',
'I(pronoun) want(intent) to(preposition) eat(activity) ',
'I(pronoun) to(preposition) book(intent) restaurant(activity) ',
'book(intent) restaurant(activity) '],

'conjunctions' : ['with(conjunction) ', 'at(preposition) ', 'in(preposition) ', 'for(preposition) '],

'target':'../data/restaurants.txt'

}

maps = {
	
	'text' : ['driving(activity) direction(activity) to(preposition) ',
	'directions(activity) to(preposition) ',
	'get(intent) direction(activity) to(preposition) ',
	'how(intent) to(preposition) get(activity) to(preposition) ',
	'shortest(count) route(activity) to(preposition) ',
	'fastest(count) route(activity) to(preposition) ',
	'how(intent) to(preposition) reach(activity) ',
	'I(pronoun) want(intent) to(preposition) go(activity) to(preposition) ' ,
	'map(activity) of(preposition) ',
	'show(intent) me(pronoun) the(article) map(activity) of(preposition) ',
	'take(activity) me(pronoun) to(preposition) ',
	'hey(other) man(other) give(intent) me(pronoun) directions(activity) for(preposition) ',
	'nearby(activity) ',
	'nearest(activity) ']
}

food = {
	'text' : ['order(activity) food(activity) ',
	'I(pronoun) want(intent) to(preposition) order(activity) food(activity) ',
	'order(activity) ',
	'place an(article) order(activity) ',
	'hey(other) I(pronoun) want(intent) to(preposition) order(activity) ',
	'hey(other) man(other) order(activity) '
	],

	'conjunctions': ['from(preposition) ', 'at(preposition) '],

	'target': '../data/restaurants.txt'
}

