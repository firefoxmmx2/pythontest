#!/usr/bin/python
'''
 htmlQuo.py
 @author ffmmx
 
'''

from BaseHTMLProcessor import BaseHTMLProcessor
if __name__=='__main__':
    htmlSource='''
    <html>
     <head>
     <title>Test page</title>
     </head>
     <body>
     <ul>
     <li><a href=index.html>Home</a></li>
     <li><a href=toc.html>Table of contents</a></li>
     <li><a href=history.html>Revision history</a></li>
     </body>
     </html>
    '''
    parser=BaseHTMLProcessor()
    print parser.feed(htmlSource)

