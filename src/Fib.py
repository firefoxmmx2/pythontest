#!/usr/bin/python
#coding:utf8

'''
Created on 2011-1-22

@author: hooxin
'''
class Fib:
	'''a generator'''
	def __init__(self,max):
		self.max=max
	
	def __iter__(self):
		self.a=0
		self.b=1
		return self
	
	def __next__(self):
		fib=self.a
		if fib > self.max:
			raise StopIteration
		self.a,self.b=self.b,self.a+self.b
		return fib
	
if __name__ =="__main__":
	fib=Fib(1000)
	print(fib.__class__)
	print(fib)
	print(fib.__doc__)
	
	for n in fib:
		print( n,end=' ')
	
	