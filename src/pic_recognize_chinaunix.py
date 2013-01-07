#!/usr/bin/env python
#- * - coding:utf8 - * -

'''
Created on 2013-1-7
'''

import Image

def img2four(image):
    left = 0
    upper = 0
    right = 10
    lower = 10
    
    c = 4
    while c:
        box = (left, upper,right,lower)
        im = Image.open(image)
        region = im.crop(box)
        region.convert('L').save("crop_"+str(4-c)+".bmp")
        left = left+10
        right = right + 10
        c = c-1

def printPixel(image):
    img = Image.open(image )
    for y in range(0,10):
        for x in range(0,10):
            print img.getpixel((x,y))
        print

def cross(color):
    if color != 238:
        return True
    else:
        return False
def recognize(image):
    '''通过每个字体都有不同的颜色,在使用灰度滤镜的时候,都应该有不同的灰度,通过灰色来判断具体是那个数字'''
    bgcolor = 238
    img = Image.open(image)
    
    p = img.getpixel((1,8)) #取得像素点的颜色
    if cross(p):
        return 7
    
    p = img.getpixel((0,0))
    if cross(p):
        return 5
    
    p = img.getpixel((2,1))
    if cross(p):
        return 1 
    
    p = img.getpixel((3,1))
    if cross(p):
        return 4
    
    p = img.getpixel((1,1))
    if cross(p):
        return 6 # not 1 , must be 6
    
    p = img.getpixel((1,7))
    if cross(p):
        return 2
    
    p = img.getpixel((2,5))
    if cross(p):
        return 9
    
    p = img.getpixel((5,4))
    if cross(p):
        return 0 # not 9 , must be 0
    
    p = img.getpixel((1,4))
    if cross(p):
        return 8
    else:
        return 3
    
def getcode(image):
    img2four(image)
    n0 = recognize('crop_0.bmp')
    n1 = recognize('crop_1.bmp')
    n2 = recognize('crop_2.bmp')
    n3 = recognize('crop_3.bmp')
    
    import os
    
    if os.path.exists('crop_0.bmp'):
        os.remove('crop_0.bmp')
    
    if os.path.exists('crop_1.bmp'):
        os.remove('crop_1.bmp')
        
    if os.path.exists('crop_2.bmp'):
        os.remove('crop_2.bmp')
    
    if os.path.exists('crop_3.bmp'):
        os.remove('crop_3.bmp')
        
    return str(n0) + str(n1) + str(n2) + str(n3)

    

if __name__ == '__main__':
    print getcode('1.bmp')