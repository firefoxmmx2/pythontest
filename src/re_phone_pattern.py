#!/usr/bin/python
# coding=utf8

# vim:ts=4
import re

def main():
	phone_pattern=re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)%')
    groups1=phone_pattern.search('work 1-(800) 555.1212 #1234').groups()
    groups2=phone_pattern.search('800-555-1212')
    groups3=phone_pattern.search('80055512121234')    
    print groups1
    print groups2
    print groups3

if __name__ == '__main__':
    main()
