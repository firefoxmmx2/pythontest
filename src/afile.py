#
#coding:utf8
'''
Created on 2011-2-3

@author: hooxin
'''

if __name__=="__main__":
	afile=open('/home/hooxin/Work/filetest.txt',mode="r")
	try:
		print(afile.read())
	except IOError as e:
		print(e)
	finally:
		afile.close()
	
