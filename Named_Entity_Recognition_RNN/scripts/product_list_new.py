flights = {
	'mapping':{
	'#':'loc',
	'$':'day',
	'&': 'month',
	'*': 'date',
	'@': 'count'
	},
	'text2': ['I want to go to # by air',
	'I want to go to # by flight',
	'take me to # by flights',
	'take me to # by air',
	'can you take to # by air',
	'go to # by flights'
	],

	'text':['book(other) flight(other) tickets(other) to(other) #',
	'flights(other) to(other) #',
	'flight(other) tickets(other) to(other) #',
	'book(other) flights(other) to(other) #',
	'book(other) flight(other) to(other) # for(other) * &',
	'book(other) flights(other) to(other) # for(other) * & and(other) return(other) on(other) * &',
	'flight(other) tickets(other) to(other) # on(other) $ and(other) return(other) ticket(other) of(other) * &',
	'get(other) me(other) flights(other) to(other) # for(other) tomorrow(date)',
	'flights(other) between(other) # and(other) # for(other) tomorrow(date)',
	'show(other) me(other) flights(other) between(other) # and(other) #',
	'# # airfare(other)',
	'# # flights(other) for(other) next(date) $',
	'tickets(other) for(other) # for(other) next(date) $',
	'flights(other) to(other) # from(other) # on(other) * &'],


	'text1': ['I(pronoun) want(intent) to(prepostion) fly(activity) to(prepostion) # on(preposition) $',
	'get(intent) me(pronoun) flight(activity) tickets(noun) for(prepostion) my(person) mom(person) from(prepostion) # to(prepostion) # on(prepostion) $',
	'I(pronoun) want(intent) to(prepostion) go(intent) to(prepostion) # $ by(prepostion) air(activity)',
	'make(intent) me(pronoun) an(article) airline(activity) book(intent)ing(intent) for(prepostion) # on(prepostion) * of(prepostion) next(date) month(date)',
	'book(intent) tickets(noun) of(prepostion) Indigo(other) Airlines(activity) for(prepostion) a(article) flight(activity) to(prepostion) # on(prepostion) $',
	'I(pronoun) want(intent) to(prepostion) fly(activity) to(prepostion) # tomorrow(date) and(conjunction) return(other) next(date) $',
	'book(intent) ticket(noun) of(prepostion) Indigo(other) Airlines(activity) for(prepostion) a(article) flight(activity) to(prepostion) # on(prepostion) $ for(prepostion) 3(num-adults) adults(adult) and(conjunction) 1(num-child) child(child)',
	'# to(prepostion) # flight(activity) tickets(noun)',
	'book(intent) tickets(noun) from(prepostion) # to(prepostion) # for(prepostion) Jet(activity) Airways(activity)',
	'book(intent) tickets(noun) from(prepostion) # on(prepostion) * & to(prepostion) # for(prepostion) Deccan(loc) Airways(activity)',
	'book(intent) tickets(noun) from(prepostion) # on(prepostion) * & to(prepostion) # for(prepostion) Air(activity) Asia(loc)',
	'flight(activity) reservation(activity) to(prepostion) # from(prepostion) # for(prepostion) $',
	'cheap(adjective) air(activity) tickets(noun) to(prepostion) # for(prepostion) * & and(conjunction) return(other) on(prepostion) * &',
	'# to(prepostion) # airfare(activity) for(prepostion) $',
	'# to(prepostion) # airfare(activity) for(prepostion) * & for(prepostion) @(num-adults) adult(adult) @(num-child) child(child) and(conjunction) @(num-infant) infant(infant)',
	'I(pronoun) want(intent) to(prepostion) fly(activity) to(prepostion) # $ via(article) Air(activity) India(loc)',
	'book(intent) ticket(noun) of(prepostion) to(prepostion) # on(prepostion) $ for(prepostion) @(num-adults) adults(adult) and(conjunction) @(num-child) child(child) and(conjunction) return(other) on(prepostion) * &',
	'# to(prepostion) # flight(activity) tickets(noun)',
	'take(intent) me(pronoun) to(prepostion) # by(prepostion) air(activity)',
	'take(intent) me(pronoun) to(prepostion) # by(prepostion) air(activity) tomorrow(date)',
	'I(pronoun) have(intent) to(prepostion) reach(other) # by(prepostion) $ by(prepostion) air(acitivity)',
	'2(num-adults) air(activity) tickets(noun) for(prepostion) # on(prepostion) $ and(conjunction) return(other) on(prepostion) * &',
	'take(intent) me(pronoun) to(prepostion) # by(prepostion) air(activity) on(prepostion) * and(conjunction) return(other) ticket(noun) of(prepostion) *',
	'fly(activity) to(prepostion) # by(prepostion) Spice(other) Jet(activity) on(prepostion) $ with(prepostion) @(num-adults) adults(adults) and(conjunction) @(num-child) child(child)',
	'book(intent) tickets(noun) of(prepostion) Indigo(other) Airlines(activity) for(prepostion) a(article) flight(activity) to(prepostion) # on(prepostion) $ and(conjunction) return(other) on(prepostion) * of(prepostion) & for(prepostion) @(num-adults) adults(adults) and(conjunction) @(num-infant) infant(infant)',
	'Vistara(article) airlines(activity) ticket(noun) for(prepostion) @(num-adults) people(adults) to(prepostion) # on(prepostion) * & and(conjunction) return(other) next(date) Monday(date)',
	'flights(activity) to(prepostion) #',
	'cheap(adjective) air(activity) tickets(noun) to(prepostion) # from(prepostion) # on(prepostion) * & for(prepostion) @(num-adults)',
	'flights(activity) available(other) for(prepostion) $ to(prepostion) #',
	'tickets(noun) to(prepostion) # from(prepostion) # on(prepostion) next(date) Thursday(date)',
	'flights(activity) to(prepostion) #',
	'flights(activity)',
	'book(intent) tickets(noun)',
	'domestic(other) airline(activity) book(intent)ings',
	'get(intent) me(pronoun) a(article) ticket(noun) to(prepostion) #',
	'air(activity) ticket(noun) for(prepostion) @(num-adults) persons(noun) to(prepostion) # on(prepostion) * &',
	'early(time) morning(time) flights(activity) to(prepostion) # from(prepostion) #',
	'get(intent) me(pronoun) a(article) morning(time) flight(activity) to(prepostion) #',
	'book(intent) @(num-adults) flight(activity) tickets(noun) to(prepostion) # for(prepostion) $',
	'flights(activity)',
	'fly(activity) with(prepostion) Lufthansa(other) airlines(activity)',
	'flight(activity) booking(intent)'
],
'airports' : '../data/flights.txt'
}