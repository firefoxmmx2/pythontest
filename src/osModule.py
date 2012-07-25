'''
Created on 2011-1-20

@author: hooxin
'''

import os

print(os.path.join('/xx/xx/ss','test.py'))
print(os.path.join('/xx/xx/xx','test.py'))

print(os.path.expanduser("~"))

print(os.path.join(os.path.expanduser("~"),'xx','dd','test.py'))

pathname='/xx/xx/xx/test.py'
print(os.path.split(pathname))

(dirname,filename)=os.path.split(pathname)
print(dirname)
print(filename)

(shortname,extension) = os.path.splitext(filename)
print(shortname)
print(extension)

os.chdir('/home/hooxin/')
import glob

print(glob.glob('*.doc'))
print(glob.glob('*.sql'))

print(os.getcwd())
metadata=os.stat('*.doc')
print(metadata.st_mtime)
import time
time.localtime(metadata.st_mtime)
time.struct_time(tm_year=2009,tm_mon=7,tm_mday=13,tm_hour=17,
				tm_min=24,tm_sec=44,tm_wday=0,tm_yday=194,tm_isdst=1)
