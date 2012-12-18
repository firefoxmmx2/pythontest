'''
Created on 2012-6-14

@author: hooxin
'''
import time,urllib,hashlib
import urllib2
import re
from cookielib import CookieJar,LWPCookieJar
from urllib2 import HTTPCookieProcessor

def current_timestamp():
    return int(time.time()*1000)
def encypt_password(password):
    if not re.match(r'^[0-9a-f]{32}$', password):
        password = md5(md5(password))
    return password
def urlencode(u):
    def unif8(u):
        if type(u) == unicode:
            u = u.encode('utf8')
        return u
    return urllib.urlencode([(unif8(k), unif8(v)) for k,v in u.items()])

def urlopen(opener,url,**args):
    if 'data' in args and type(args['data']) == dict:
        args['data'] = urlencode(args['data'])
    return opener.open(urllib2.Request(check_url),**args)
def md5(string):
    return hashlib.md5(string).hexdigest().lower()

cachetime = current_timestamp()
username = 'firefoxmmx'
password = 'missdark'
realPasswd = ''

check_url = 'http://login.xunlei.com/check?u=%s&cachetime=%d' % (username, cachetime)
cookie = CookieJar()
opener = urllib2.build_opener(HTTPCookieProcessor(cookie))
loginPage = urlopen(opener,check_url).read()
verityCode = cookie._cookies['.xunlei.com']['/']['check_result'].value[2:].upper()
print(verityCode)
realPasswd = encypt_password(password)
realPasswd = md5(realPasswd+verityCode) 
check_url = 'http://login.xunlei.com/sec2login/'

checkLogin = urlopen(opener,check_url,data={'u':username,'p':realPasswd,'verifycode': verityCode})
loginPage = checkLogin.read()
cookie
print loginPage