#!/usr/bin/env python2
#-*-coding:utf8-*-

import Image

try:
	im = Image.open('test.jpg')
	out = im.resize((128,128)) #改变大小
	#out = im.retate(45) #旋转46度
	out = out.transpose(Image.FLIP_LEFT_RIGHT) #水平翻转
	out = out.transpose(Image.FLIP_TOP_BOTTOM) # 垂直翻转
	out = out.transpose(Image.ROTATE_90) #翻转90度
	out = out.transpose(Image.ROTATE_270) #翻转270度
	out = out.transpose(Image.ROTATE_180) #翻转 180度
	out.save('test2.jpg')
except IOError: 
	print ("No File")
