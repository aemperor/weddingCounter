#!/usr/bin/python

import csv
import sys
import getopt

fileErrorMessage = 'Error opening file'
nameRow = 1
rsvpRow = 5
plusOneRow = 7
mealChoiceRow = 6
plusOneMealChoiceRow = 10
mealNames = ['Chicken with Shrimp', 'Steak', 'Vegan']


def main (argv):
	file = 'responses.csv'
	opts = []

	try:
		opts, args = getopt.getopt(argv, "f:c:t:m:")
	except getopt.GetoptError:
		print 'Option not specified'
	if(opts):
		for opt, arg in opts:
			#-f filename
			if (opt == '-f'):
				file = arg
			#-meal meal name
			elif (opt == '-m'):
				meal = arg
				if (meal.lower() == 'chicken'):
					meal = 'Chicken with Shrimp'
				if (meal in mealNames):
					countTotalMealChoice(file, meal)
				else:
					print 'Meal choice is not in the list'
					print 'Here are the meal choices: ', ', '.join(mealNames)
					sys.exit(2)

	for arg in argv:
		if (arg == '-c'):
			countGuestsAttending(file)
		elif (arg == '-t'):
			countTotalRsvp(file)
		elif (arg == '-m' and not opts):
			countTotalMealChoice(file)


# guests attending
def countGuestsAttending(filename):
	try:
		file = open(filename, 'r')
	except IOError:
		print fileErrorMessage
		sys.exit(2)
	reader = csv.reader(file, delimiter=',')

	total = 0
	for row in reader:
		if (row[rsvpRow] == 'Yes'):
			total += 1
		if (row[plusOneRow] == 'Yes'):
			total += 1
	print total
	file.close()

# total RSVPs
def countTotalRsvp(filename):
	try:
		file = open(filename, 'r')
	except IOError:
		print fileErrorMessage
		sys.exit(2)
	reader = csv.reader(file, delimiter=',')

	# start at -2 because of header for yes/no column for rsvp and plus one
	total = -2 
	for row in reader:
		if (row[rsvpRow]):
			total += 1
		if (row[plusOneRow]):
			total += 1

	print total
	file.close()

# total chicken meals
def countTotalMealChoice(filename, mealName='nothing'):
	try:
		file = open(filename, 'r')
	except IOError:
		print fileErrorMessage
		sys.exit(2)
	reader = csv.reader(file, delimiter = ',')

	total = 0
	if (mealName == 'nothing'):
		steak = 0
		chicken = 0
		vegan = 0
		for row in reader:
			mealChoice = row[mealChoiceRow]
			plusOneMealChoice = row[plusOneMealChoiceRow]

			# meal choices
			if (mealChoice == mealNames[0]):
				chicken += 1
				total += 1
			elif (mealChoice == mealNames[1]):
				steak += 1
				total += 1
			elif (mealChoice == mealNames[2]):
				vegan += 1
				total += 1

			# plus one meal choices
			if (plusOneMealChoice == mealNames[0]):
				chicken += 1
				total += 1
			elif (plusOneMealChoice == mealNames[1]):
				steak += 1
				total += 1
			elif (plusOneMealChoice == mealNames[2]):
				vegan += 1
				total += 1

		print 'Total: ', total , ', Chicken: ', chicken , ', Steak: ', steak, ', Vegan: ', vegan
	else:
		for row in reader:
			if (row[mealChoiceRow] == mealName):
				total += 1
			if (row[plusOneMealChoiceRow] == mealName):
				total += 1
		print mealName, ': ', total

	file.close()


main(sys.argv[1:])