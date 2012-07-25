#!/usr/bin/env python2
#-*-coding:utf8-*-

import re
import urllib2
from bs4 import BeautifulSoup

def readPage(url):
	page = urllib2.urlopen(url).read()
	pageContent = BeautifulSoup(page)
	if pageContent.find('pre'):
		preHandleCode = pageContent.find('pre').next
		print(preHandleCode)
	else:
		print('No Code')

www  = urllib2.urlopen('http://www.oschina.net/code/list/y/python?show=time&p=7')
msg = www.read()
find = r'(http://www.oschina.net/code/snippet_\d+_\d+)'
ak = re.findall(find,msg)

if ak is not None:
	for i in ak:
		print(i)
		readPage(i)