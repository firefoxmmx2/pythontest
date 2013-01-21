#!/usr/bin/env python2
#- * - coding:utf8 - * -

'''
Created on 2012-12-21

python 基于PIL的 图片识别
'''

import Image, ImageEnhance,ImageFilter

image_name = '1.jpeg'

#去干扰点
im = Image.open(image_name)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im =enhancer.enhance(2)
im = im.convert('L')
im = im.convert('1')
im.show()

s=12 #起始切割点 x
t=2 #起始切割点 y
w=10 #切割宽+y
h=15 #切割长+x


im_new=[]
for i in range(4):#验证码切割
    im1=im.crop((s+w*i+i*2,t,s+w*(i+1)+i*2,h))
    im_new.append(im1)
    

xsize,ysize = im_new[0].size
gd=[]
for i in range(ysize):
    tmp=[]
    for j in range(xsize):
        if(im_new[0].getpixel((j,i))==255):
            tmp.append(1)
        else:
            tmp.append(0)
    gd.append(tmp)

#看效果

if __name__=='__main__':
    for i in range(ysize):
        print gd[i]    