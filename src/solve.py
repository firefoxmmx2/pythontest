'''
Created on 2011-1-23

@author: hooxin
'''

import re
import itertools

def solve(puzzle):
	words=re.findall('[A-Z]+', puzzle.upper())
	uniqueCharacters=set(''.join(words))
	assert len(uniqueCharacters) <= 10,'Too many letters'
	firstLetters={word[0] for word in words}
	n=len(firstLetters)
	sortedCharecters=''.join(firstLetters)+\
			  ''.join(uniqueCharacters-firstLetters)
	characters=tuple(ord(c) for c in sortedCharaters)
	digits=tuple(ord(c) for c in '0123456789')
	zero=digits[0]
	for guess in itertools.permutations(digits,len(characters)):
		if zero not in guess[:n]:
			equation=puzzle.translation(dict(zip(characters,guess)))
			if eval(equation):
				return equation

if __name__=='__main__':
	import sys
	for puzzle in sys.argv[1:]:
		print(puzzle)
		solution=solve(puzzle)
		if solution:
			print(solution)

