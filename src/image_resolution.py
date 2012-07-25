#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import os, sys, Image

rootDir = '~/Pic'
targetDir = '../test_pic'

def encodeChinese(msg):
    _type = sys.getfilesystemencoding()
    return msg.decode('UTF-8').encode(_type)

errFile = open('errFile.log','w')

def judgeSize(im):
    #判断图片分辨率，如果最大边长超过了1024返回false，否则true
    sizeOne = im.size[0]
    sizeTwo = im.size[1]
    
    if sizeOne > sizeTwo:
        _max = sizeOne
        _min = sizeTwo
    else:
        _max = sizeTwo
        _min = sizeOne
    if max > 1024:
        return False
    else:
        return True
    
def returnSize(im):
    #返回图片大小，返回两个值，第一个返回值最大
    _max,_min = im.size
    if _max > _min:
        return _max,_min
    else:
        return _min,_max

def changeSize(im,_max,_min):
    value = _max / 1024
    print 'value = %s' % value
    _min = _min/value
    newimg = im.resize((1024,min),Image.ANTIALIAS)
    return newimg

def main():
    for parent,dirnames,filenames in os.walk(os.path.expanduser(rootDir)):
        for filename in filenames:
            fName = filename
            filename = parent + os.sep + filename
            fPostfix = os.path.splitext(filename)[1]
            try:
                img = Image.open(filename)
            except:
                print filename
                print encodeChinese('打开这个文件出错')
                continue
            print filename
            print fPostfix
            if fPostfix != '.jpg' and fPostfix != '.png' and fPostfix != '.JPG' \
                and fPostfix != '.PNG':
                errFile.write(str(filename) + '\n')
                errFile.write(encodeChinese('上面这个文件不是图片，请检查...')+'\n')
                errFile.write('\n')
            else:
                print 'judgeSize()'
                if judgeSize(img) == False:
                    print 'judgeSize == False'
                    _max,_min = returnSize(img)
                    newimg = changeSize(img,  _max,_min)
                    newimg.save(targetDir + os.sep + fName)
                    print str(targetDir + os.sep + fName)
                    print encodeChinese('保存完毕')
    print encodeChinese("处理完毕")
    errFile.close()
    
main()