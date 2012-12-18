#!/usr/bin/env python2
# -*- coding:utf-8 -*-

'''
Created on 2012-6-8

@author: hooxin
'''

def fib(num,a=0,b=1):
    fb = []  
    if b<num:
        fb.append(b)
        fb.extend(fib(num,b,a+b))
    return fb
print fib(100)