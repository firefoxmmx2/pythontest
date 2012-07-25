'''
Created on 2011-1-22

@author: hooxin
'''
import os
class LazyRules:
	rulesFilename=os.path.join(os.path.expanduser('~'), '臨時文本.txt')
	
	def __init__(self):
		self.patternFile=open(self.rulesFilename,encoding='utf8')
		self.cache=[]
		
	def __iter__(self):
		self.cacheIndex=0
		return self
	
	def __next__(self):
		self.cacheIndex+=1
		
		if len(self.cache) >= self.cacheIndex:
			return self.cache[self.cacheIndex-1]
		
		if self.patternFile.closed:
			raise StopIteration

		line=self.patternFile.readline()
		if not line:
			self.patternFile.close()
			raise StopIteration
				
		pattern,search,replace=line.split(None,3)
		
		funcs=build_match_and_apply_functions(pattern,search,replace)
		self.cache.append(funcs)
		return funcs
	
rules=LazyRules()