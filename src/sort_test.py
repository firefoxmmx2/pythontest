#!/usr/bin/env python2
#- * - coding:utf8 - * -
'''
Created on 2013-1-24

'''
from abc import ABCMeta, abstractmethod

class BaseSort(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def sort(self,array):
		pass
	def less(self,v,w): #return boolean
		return v < w
	def exch(self,array,i,j): 
		array[i],array[j] = array[j],array[i]
	def show(self,array):
		for i in array:
			print(i,)
		print()
	def isSorted(self,array): #return boolean
		for i in range(1,len(array)):
			if self.less(array[i],array[i-1]) : return False
		return True
	
class Selection(BaseSort):
	'''选择排序'''
	def sort(self,array):
		n = len(array)
		for i in range(n):
			min = i
			for j in range(i+1,n):
				if self.less(array[j], array[min]): min = j;
			self.exch(array,i,min)

class Insertion(BaseSort):
	'''插入排序'''
	def sort(self, array):
		n = len(array)
		for i in range(1,n):
			for j in range(i,0,-1):
				if not self.less(array[j], array[j-1]):
					break
				self.exch(array, j, j-1)
				
class Shell(BaseSort): #希尔排序
	'''希尔排序'''
	def sort(self,array):
		n = len(array)
		h = 1
		while h < n/3 : h = 3*h + 1 #1,4,13,40,121,364,1093
		while h >= 1:
			#将数组变成有序的
			for i in range(h,n):
				#将a[i]插入到a[i-h],a[i-2*h],a[i-3*h]...之中
				for j in range(i,0,-h):
					if j >=h and self.less(array[j],array[j-h]):
						self.exch(array,j,j-h)
					else:
						break
			h = h/3

class Merge(BaseSort):
	'''归并排序'''
	def merge(self,array,lo,mid,hi):
		#将array[lo..mid]和array[mid+1..hi] 归并
		i = lo
		j = mid+1
		print "range(lo,hi+1) = ",range(lo,hi+1)
		for k in range(lo,hi+1):
			self.aux[k] = array[k]

		for k in range(lo,hi+1):
			if i > mid: 
				array[k] = self.aux[j]
				j += 1	
			elif j > hi:
				array[k] = self.aux[i]
				i += 1	
			elif self.less(self.aux[j],self.aux[i]):
				array[k] = self.aux[j]
				j += 1	
			else:
				array[k] = self.aux[i]
				i += 1	
	def sort(self,array):
		self.aux = [None for i in range(10)]
		self._sort(array,0,len(array)-1)
	def _sort(self,array,lo,hi):
		if hi <= lo: return
		mid = lo+(hi-lo)/2
		self._sort(array,lo,mid)
		self._sort(array,mid+1,hi)
		
		self.merge(array,lo,mid,hi)
	
if __name__ == '__main__':
	selection1 = Selection()
	array = [s for s in 'helloworld']
	selection1.sort(array)
	print(array)
	array = [s for s in 'helloworld']
	insertion1 = Insertion()
	insertion1.sort(array)
	print(array)
	array = [s for s in 'SHELLSORTEXAMPLE']
	shell1 = Shell()
	shell1.sort(array)
	print(array)
	array = [s for s in 'MERGESORTEXAMPLE']
	merge = Merge()
	merge.sort(array)
	print(array)


