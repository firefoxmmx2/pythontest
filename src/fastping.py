#!/usr/bin/env python2
# -*- coding:utf-8 -*-

'''
Created on 2012-6-11

'''

import sys, subprocess
from threading import Thread
from Queue import Queue

class CreateThread(Thread):
	def __init__(self,func,args,name=''):
		super(CreateThread,self).__init__()
		self.__name=name
		self.__func = func
		self.__args = args
	
	def run(self):
		apply(self.__func,self.__args)
	
	
class FPing(object):
	def __init__(self,network,tnum):
		self.network = network
		self.tnum = tnum
		
	def ip_process(self,network):
		start = network.split('-')[0].split('.')[3]
		end = network.split('-')[1]
		ip = network.split('-')[0].split('.')[:3]
		ip_3 = '.'.join(ip)
		return (start,end,ip_3)
	
	def check_grama(self,network):
		check = network.find('-')
		if check == -1:
			self.usage()
			sys.exit(1)
	def usage(self):
		print('''
		Usage: python fping.py ip-num example:
		python fping.py 192.168.1.1-255
		''')
		
	def ping_scanf(self,num,iq,oq):
		while True:
			try:
				ip = iq.get()
				print('[*]Thread %s: Pinging %s' % (num,ip))
				ret = subprocess.call('ping -c 1 -w 3 %s' % ip,shell=True,stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)
				if ret == 0:
					print('[*]%s: is alive.' % ip)
					oq.put(ip)
				else:
					print('[*]%s: did not responed' % ip)
				iq.task_done()
			except Exception:
				print('Threading Exception!')
				sys.exit(1)
				
	def active(self):
		worker_num = self.tnum
		in_q = Queue()
		out_q = Queue()
		start,end,ip3 = self.ip_process(self.network)
		
		for ip1 in xrange(int(start),int(end)+1):
			ip = ip3 + '.' +str(ip1)
			in_q.put(ip)
			
		for i in xrange(worker_num):
			worker = CreateThread(self.ping_scanf,(i,in_q,out_q),self.ping_scanf.__name__)
			worker.setDaemon(True)
			worker.start()
			
		print('[*]Main Thread Waiting...')
		in_q.join()
		out_q.join()
		print ('[*]Done!')
if __name__ == '__main__':
	thread_worker_num = 10
	fping = FPing(sys.argv[1],thread_worker_num)
	if len(sys.argv) !=2 :
		fping.usage()
		sys.exit(1)
	fping.active()
