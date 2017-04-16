#!/usr/bin/python
#shopping

salary = int(raw_input('Input u salary: '))
while True:
	print '''shopping	list
	car	200000
	iphone	6000
	ipad	2000
	coffe	32'''
	order = raw_input('what do you want to buy?')
	if order == 'car':
		if salary > 200000:
			print 'great, now u have a car!'
			salary = salary - 200000
			print 'now ,u have %s left' %salary
		else:
			'sorry ,u canot affor to buya %s, ty something else' %order
