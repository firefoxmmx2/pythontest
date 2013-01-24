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
    xs = [9,37,70,104,138,170,202,231,261,294,324]
    ys = [0,40,87,134,180,219]
    
    for i, x in enumerate(xs):
        if i+1 >= len(xs):
            break
        for j, y in enumerate(ys):
            if j+1 >= len(ys): break
            box = (x,y,xs[i+1],ys[j+1])
            t = im.crop(box).copy()
            box = box + ((i+1) % 10,)
            result.append((normalize_32_32(t,'num_%d_%d_%d_%d_%d.bmp' % box),(i+1)%10))
#            raise Exception('test')
def normalize_32_32(im,filename):
    '''切割图片'''
    #  需要居中化,并且拓展为32x32像素的图片
    width,height = im.size
    black_point = [(x,y) for x in range(width) \
                    for y in range(height) \
                    if im.getpixel((x,y)) == BLACK]
    x_points,y_points = zip(*black_point)
    min_x,min_y = min(x_points),min(y_points)
    max_x,max_y = max(x_points),max(y_points)
    box = (min_x-1,min_y-1,max_x+1,max_y+1)
    im = im.crop(box)
    im = im.resize((32,32),Image.ANTIALIAS)
    
#    im.show()
    im.save(filename)
    return im
if __name__ == '__main__':
    im = Image.open('3.gif')
    im = conver_to_bw(im)
    split(im)