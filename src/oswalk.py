#!/usr/bin/env python2
#-*-coding:utf8-*-

import os

def show(arg, dirname,filenames):
	print('dirname:'+dirname)

	for f in filenames:
		if os.path.isfile(dirname+os.sep+f):
			print('------'+f)
	
if __name__ == '__main__':
	os.path.walk(os.path.expanduser('~/Downloads/H/comic') ,show,None)

