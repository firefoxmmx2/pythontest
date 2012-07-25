#!/usr/bin/python
#coding:utf8
'''
	about set
	@author ffmmx
'''

aSet={2,4,5,9,12,21,30,51,76,127,195}

print 30 in aSet
print 31 in aSet
bSet={1,2,3,5,6,8,9,12,15,17,18,21}
print aSet.union(bSet)
print aSet.intersection(bSet)
print aSet.difference(bSet)
print aSet.symmetric_difference(bSet)


