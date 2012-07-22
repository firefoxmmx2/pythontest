#
# coding=utf8
'''
Created on 2010/06/29

@author: hooxin
'''

if __name__ == '__main__':
	filename = raw_input("输入文件名")
	f = open(filename,'r')
	for line in f:
		print line,
	f.close()
	