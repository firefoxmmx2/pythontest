#!/usr/bin/env python2
# -*- coding:utf-8 -*-
'''
Created on 2012-6-8

@author: hooxin
'''

import sys, smtplib, socket
from getpass import getpass
from smtplib import SMTPHeloError

if len(sys.argv) < 4:
    print('[*]usage: %s server fromaddr toaddr ' % sys.argv[0])
    sys.exit(1)
    
server = sys.argv[1]
fromaddr = sys.argv[2]
toaddr = sys.argv[3]

message = '''
TO: %s
From: %s
Subject: Test Message from smtp_mail.py
Hello, This a simple smtp mail example
''' % (','.join(toaddr), fromaddr)

def get_size():
    '''获得服务器允许发送邮件的大小'''
    
    try:
        s = smtplib.SMTP(server)
        code = s.ehlo()[0]
        usesesmtp = 1
        if not (200 <= code <= 299):
            usesesmtp = 0
            code = s.helo()[0]
            if not (200 <= code <= 299):
                raise SMTPHeloError(code)
            
        if usesesmtp and s.has_extn('size'):
            print('最大消息大小是',s.esmtp_features['size'])
            if len(message) > int(s.esmtp_features['size']):
                print('消息太长;退出...')
                sys.exit(2)
        s.starttls()        
        s.sendmail(fromaddr,toaddr,message)
    except(socket.gaierror,socket.errno,socket.herror,smtplib.SMTPException),e:
        print('***你的消息可能还没有被发送')
        print(e)
        sys.exit(1)
        
    else:
        print('***消息已经成功的发送到%d' % len(toaddr))
        
def ssl_tls():
    '''使用SSL安全套件层和TLS安全传输层进行邮件传输，确保密码在传输过程中的安全'''
    try:
        s = smtplib.SMTP(server)
        code = s.ehlo()[0]
        usesesmtp = 1
        if not (200 <= code <= 299):
            usesesmtp = 0
            code = s.helo()[0]
            if not (200 <= code <= 299):
                raise SMTPHeloError(code)
            
        if usesesmtp and s.has_extn('starttls'):
            print('验证 TLS.......')
            s.starttls()
            code=s.ehlo()[0]
            if not (200 <= code <= 299):
                print('在开始tls之后不能ehlo')
                sys.exit(5)
                
            print('使用TLS连接...')
            
        else:
            print ('服务器 不支持TLS;尝试正常的连接方式')
            
        s.sendmail(fromaddr, toaddr,message)
    except(socket.gaierror,socket.errno,socket.herror,smtplib.SMTPException),e:
        print('***消息可能没有被发送！')
        print(e)
        
    else:
        print '***消息成功的发送到%d' % len(toaddr)
        
        
    
def auth_login():
    '''当发送邮件时，服务器需要验证，则输入用户名密码，可以发送邮件'''
    username = 'firefoxmmx'
    password = 'missdark_gmail'
    try:
        s = smtplib.SMTP(server)
        s.starttls()
        code = s.ehlo()[0]
        usesesmtp = 1
        
        if not (200 <= code <= 299):
            usesesmtp = 0
            code = s.helo()[0]
            if not (200 <= code <= 299):
                raise SMTPHeloError(code)
        if usesesmtp and s.has_extn('auth'):
            print('使用用户验证连接...')
            try:
                s.login(username,password)
            except smtplib.SMTPException,e:
                print('验证失败:',e)
                sys.exit(1)
                
        else:
            print('服务器不支持用户验证;使用正常连接方式')
        
        
        s.sendmail(fromaddr, toaddr,message)
        
    except(socket.gaierror,socket.error,socket.herror,smtplib.SMTPException),e:
        print('***消息可能没有被发送！')
        print(e)
        sys.exit(1)
    else:
        print '***消息成功的发送到%d' % len(toaddr)
        
        
if __name__ == '__main__':
#    get_size()
#    ssl_tls()
    auth_login()
        