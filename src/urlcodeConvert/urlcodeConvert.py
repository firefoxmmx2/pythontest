'''
Created on 2010-11-21

@author: hooxin
'''
import urllib2
if __name__ == '__main__':
	urlpath = 'ed2k:%2F%2F%7Cfile%7C%E3%80%8A%E6%B5%B7%E6%9C%88%E5%A7%AC%E3%80%8B%28kuragehime%29%5B%E6%9D%B1%E6%9D%91%E3%82%A2%E3%82%AD%E3%82%B3%5D.%5B%E7%AC%AC%E4%B8%80%E5%8D%B701%E8%A9%B1%5D.rar%7C33842415%7C609913185e722b61aca7ff7ebcb9c2ca%7Ch=vnwj2a5gbmqfvbgo7jjqj7qab7tmd27x%7C/'
	newUrlPath = urllib2.unquote(urlpath)
	print newUrlPath