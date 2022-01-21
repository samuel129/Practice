'''
The exercise template includes the file words.txt, which contains words in English.

Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the
 search term.

The search term may include lowercase letters and the following wildcard characters:

A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield
words like ping and pong, and .a.e would yield words like sane, care and late.

An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the 
beginning of the search term means that any word which ends with the search term is acceptable. 

For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, 
insane and aeroplane. There can only ever be a single asterisk in the search term.

If there are no wildcard characters in the search term, only words which match the search term exactly are returned.
You may assume both wildcards are never used in the same search term.

The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.

If no matching words are found, the function should return an empty list.
'''
file = open(r"words.txt","r")
words = file.readlines()
def find_words(search_term: str):
	returnList = []
	if search_term[0] == '*':
		num_chars = len(search_term) - 1
		for word in words:
			if word[-num_chars - 1:-1] == search_term[1:]:
				returnList.append(word)
#------------------------------------------------------------
	elif search_term[-1] == '*':
		num_chars = len(search_term) - 1
		for word in words:
			if word[0:num_chars] == search_term[0:2]:
				returnList.append(word)
		pass
#------------------------------------------------------------
	elif '.' in search_term:
		index = []
		chars = []
		check = -1
		for num in range(len(search_term)):
			if search_term[num] != '.':
				index.append(num)
				chars.append(search_term[num])
		for word in words:
			if len(word) - 1 == len(search_term):
				for num in range(len(index)):
					if word[index[num]] == chars[num] and check != 0:
						check = 1
					else:
						check = 0
			if check == 1:
				returnList.append(word)
			check = -1
#------------------------------------------------------------
	else:
		for word in words:
			if word == search_term + '\n':
				returnList.append(word)
#------------------------------------------------------------
	return ''.join(returnList)
	
print(find_words('pista.....'))