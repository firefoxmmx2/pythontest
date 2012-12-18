#!/usr/bin/env python2
#- * - coding:utf8 - * -
'''
Created on 2012-12-11

'''

import Image,ImageDraw,ImageFont
import random
import math,string

class RandomChar():
    '''随机生成汉字'''
    @staticmethod
    def unicode():
        val = random.randint(0x4e00,0x9fbf)
        return unichr(val)
    
    @staticmethod
    def gb2312():
        head = random.randint(0xb0,0xcf)
        body = random.randint(0xa,0xf)
        tail = random.randint(0,0xf)
        val = (head << 8) | (body << 4) | tail
        s = '%x' % val
        return s.decode('hex').decode('gb2312')
    
class ImageChar():
    def __init__(self,fontColor=(0,0,0),
                 size=(100,40),
                 fontPath='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc',
                 bgColor=(255,255,255,),
                 fontSize=20):
        self.size = size
        self.fontPath = fontPath
        self.bgColor = bgColor
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = ImageFont.truetype(self.fontPath, self.fontSize)
        self.image = Image.new('RGB', self.size, self.bgColor)
        
    def rotate(self):
        self.image.rotate(random.randint(0,30),expand=0)
        
    def drawText(self,pos,txt,fill):
        draw  = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font,fill=fill)
        del draw
    def randRBG(self):
        return (random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255))
    def randPoint(self):
        (width,height) = self.size
        return (random.randint(0,width),random.randint(0,height))
    def randLine(self,num):
        draw = ImageDraw.Draw(self.image)
        for i in range(0,num):
            draw.line((self.randPoint(),self.randPoint()),
                      self.randRBG())
        del draw
        
    def randChinese(self,num):
        gap = 5
        start = 0 
        for i in range(0,num):
            x = start + self.fontSize * i + random.randint(0,gap) + gap * i
            self.drawText((x,random.randint(-5,5)), RandomChar().gb2312(), self.randRBG())
            self.rotate()
        self.randLine(18)
        
    def save(self,path):
        self.image.save(path)
        
if __name__ == '__main__':
    ic = ImageChar(fontColor=(100,211,90),size=(100,40))
    ic.randChinese(4)
    ic.save("1.jpeg")