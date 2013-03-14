#!/usr/bin/env python2
#coding:utf8
# Filename: pacmaker.py
from optparse import OptionParser
import base64
import os
import pycurl
import curl

'''
用于生成一个自动代理的脚本,使用autoproxy规则
'''


port = 80
protol = 'HTTP'
host = 'localhost'

avail_protol = ('HTTP', 'SOCKS4', 'SOCKS5',)
output = os.path.realpath('.') + os.path.sep + 'pacmaked.pac'
autoproxy_gfwlist = "http://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt"
gfwlist_file = None
#useProxy=False
#proxy = ('SOCKS5','127.0.0.1',7070) 

def make_pac():
    
    gfwlist = None
    if gfwlist_file:
        with open(gfwlist_file, 'r') as gfwfile:
            gfwlist = gfwfile.read()
            gfwlist = base64.b64decode(gfwlist).decode()
    else:
#        proxyHandler = ProxyHandler({protol:host+':'+port}) #只提供HTTP方式的代理，这里不受用改为CURL方式 
#        proxyAuth = ProxyBasicAuthHandler()
#        curl果然强大。
        c = curl.Curl()
        c.set_option(pycurl.PROXY,host)
        c.set_option(pycurl.PROXYPORT,port)
        if protol == 'HTTP':
            curlProxyType = pycurl.PROXYTYPE_HTTP
        elif protol == 'SOCKS5':
            curlProxyType=pycurl.PROXYTYPE_SOCKS5
        elif protol == 'SOCKS4':
            curlProxyType=pycurl.PROXYTYPE_SOCKS4
          
        c.set_option(pycurl.PROXYTYPE,curlProxyType)
        res = c.get(autoproxy_gfwlist,{})
        gfwlist = res
        gfwlist = base64.b64decode(gfwlist).decode()

    # print(gfwlist)
    pac_content = '''
    function regExpMatch(url, pattern) {
	    try { return new RegExp(pattern).test(url); } catch(ex) { return false; }
    }

    function FindProxyForURL(url, host) {
        %s
        return "DIRECT";
    }
    '''
    pac_part = []

    
    for line in (i for i in gfwlist.split('\n') if i.find("!") != 0 
            and i.find('[') != 0 and len(i) >= 3):
        return_str = 'return "{protol} {host}:{port}; DIRECT"; \n'.format(
                protol=protol,
                host=host,
                port=port
                )
        # print(line)
        if line.find('@@') == 0:
            return_str = 'return "DIRECT"; \n'
            line = line[2:]
        if line.find('||') == 0:
            line = line[2:]
            match_str = line.replace('.', r'\\.')
            match_str = match_str.replace('/', r'\\/')

            if_str = r'     if(regExpMatch(url,"^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?{match}"))'.format(match=match_str)
        else:
            if_str = r'     if(shExpMatch(url, "http://*' + line + '*"))'

        pac_part.append(if_str + ' ' + return_str)

    # print(''.join(pac_part))
    # print(pac_content % (''.join(pac_part)))
    pac_content = pac_content % (''.join(pac_part))
    with open(output, 'w') as outfile:
        outfile.write(pac_content)

if __name__ == '__main__':
    usage = 'usage: %prog [option]'
    parser = OptionParser(usage=usage)
    
    parser.add_option('-o', '--output', help='output file', dest='output', default=output)
    parser.add_option('-H', '--host', help='hostname or ip of proxy', dest='host', default=host)
    parser.add_option('-p', '--port', help='port of proxy', dest='port', default=port)
    parser.add_option('-t', '--type', help='type of proxy', dest='protol', default=protol)
    parser.add_option('-i', '--input', help="autoproxy input file", dest='input')
    (options, args) = parser.parse_args()
    
    print(options)
    
    if options.protol.upper() not in avail_protol:
        raise Exception('it\'s not support proxy protol.')
    
    protol = options.protol.upper()
    port = int(options.port)
    host = options.host
    output = options.output
    gfwlist_file = options.input

    make_pac()
