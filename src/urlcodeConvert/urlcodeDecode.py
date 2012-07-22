#!/usr/bin/python2
# coding=utf8
# filename=urlcodeDecode
'''
Created on 2010-11-21

@author: hooxin
'''
import urllib2
import sys

if __name__ == '__main__':
	print urllib2.unquote(sys.argv[1])
