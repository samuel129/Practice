'''
This program takes a 2d list of golfers put into groups, with each letter representing a golfer.
It analyzes the list and checks to see whether the groups are valid within the following conditions:

Condition 1: Each golfer plays exactly once every day.
-- A dictionary with all of the possible letters in the list
-- function compares the number of occurences between all the letters and returns true or false depending on whether 

Condition 2: The number and size of the groups is the same every day
-- Compare the lengths of all rows to see if they are all the same
-- Compare the size of all strings to see if they are all the same

Condition 3: That each player plays with every other player at most once.
-- checking with  a list
-- for loop that will traverse through all of the strings, and will keep track of all pairs, creating new ones when necessary.
-- if an existing pair is found within the list, return false else return true.
'''

# This function checks to see which last letter is even in the list of golfers and returns the last latter inclusively

def condition1(s):
	alpha = ''
	for column in range(len(s[0])):
		for letter in s[0][column]:
			alpha += letter
	wordCount = dicts = dict((el, 0) for el in alpha)
	for row in range(len(s)):
		for column in range(len(s[0])):
			for letter in s[row][column]:
				if letter not in wordCount:
					return False
				wordCount[letter] += 1
	for entry in wordCount:
		if wordCount[entry] != len(s):
			return False
	else:
		return True

def condition2(s):
	groupCheck = {}
	for row in s:
		if len(row) not in groupCheck:
			groupCheck[len(row)] = 1
		elif len(row) in groupCheck:
			groupCheck[len(row)] += 1
	if len(groupCheck) > 1:
		return False
	sizeCheck = {}
	for row in range(len(s)):
		for column in range(len(s[0])):
			if len(s[row][column]) not in sizeCheck:
				sizeCheck[len(s[row][column])] = 1
			else:
				sizeCheck[len(s[row][column])] += 1
	if len(sizeCheck) > 1:
		return False
	else:
		return True

def condition3(s):
	sets = []
	for row in range(len(s)):
		for column in range(len(s[0])):
			for letter in s[row][column]:
				for rest in s[row][column][s[row][column].find(letter) + 1::]:
					if (letter + rest) in sets:
						return False
					else:
						sets.append(letter + rest)
	return True

def valid(s):
	if not condition2(s):
		return False
	if condition1(s) and condition3(s):
		return True
	else:
		return False