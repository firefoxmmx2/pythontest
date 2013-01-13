#!/usr/bin/env python2
# -*- coding:utf8 -*-

'''
识别手写的数字
'''

import  Image

WHITE = 255
BLACK = 0

def conver_to_bw(im):
    im = im.convert("L")
#    im.save('sample_L.bmp')
#    im.show()
    im = im.point(lambda x:WHITE if x>196 else BLACK)
    im = im.convert('1')
#    im.save('sample_1.bmp')
#    im.show()
    return im

def split(im):
    assert im.mode == '1'
    result = []
    w,h = im.size
    data = im.load()
    xs = [0,23,57,77,106,135,159,179,205,228,w]
    ys = [0,22,60,97,150,h]
    
    for i, x in enumerate(xs):
        if i+1 >= len(xs):
            break
        for j, y in enumerate(ys):
            if j+1 >= len(ys): break
            box = (x,y,xs[i+1],ys[j+1])
            t = im.crop(box).copy()
            box = box + ((i+1) % 10,)
            result.append((normalize_32_32(t,'num_%d_%d_%d_%d_%d.bmp' % box),(i+1)%10))
           
def normalize_32_32(im,filename):
    '''切割图片'''
    im.resize((32,32))
#    im.show()
    im.save(filename)
    return im
if __name__ == '__main__':
    im = Image.open('3.gif')
    im = conver_to_bw(im)
    print(split(im))