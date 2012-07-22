#coding:utf8
'''
用于测试python在for循环方面的执行性能,通过运行的时间差来比较。
Created on 2011-7-10

@author: hooxin
'''
import datetime
import os

def python_for_performance():
	before_time = datetime.datetime.now()
	for i in xrange(1000000000):
		str("11")
	after_time = datetime.datetime.now()
	
	print('python_for_performance use times : {0}'.format((after_time-before_time).microseconds//1000))
	
	
if __name__ == "__main__":
	python_for_performance()
