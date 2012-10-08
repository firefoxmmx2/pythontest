import math
import Image
import ImageDraw

class DrawFun():
    width = 512
    height = 512

    min = -10
    max = 10
    
    step = 1

    unit = 1
    canvas = None
    draw = None

    ctrx = 0
    ctry = 0

    def __init__(self,width,height,min,max,step,unit):
        self.width = width
        self.height = height
        self.min = min
        self.max = max
        self.step = step
        self.unit = unit
        
        self.canvas = Image.new("RGB",[self.width,self.height],(255,255,255))

        self.draw = ImageDraw.Draw(self.canvas)

        self.ctrx = math.floor(self.width/2)
        self.ctry = math.floor(self.height/2)

        self.draw.line([(0,self.ctry),(self.width,self.ctry)],fill=(0,0,0))
        self.draw.line([(self.ctrx,0),(self.ctrx,self.height)],fill=(0,0,0))

        viewx = int(math.floor(self.width/self.unit + 1)/2)
        viewy = int(math.floor(self.height/self.unit + 1)/2)

        for x in range(1,viewx+1):
            offsetx = x * self.unit
            self.draw.line([(self.ctrx+offsetx,0),(self.ctrx+offsetx,self.height)],fill=(200,200,200))
            self.draw.line([(self.ctrx-offsetx,0),(self.ctrx-offsetx,self.height)],fill=(200,200,200))
        for y in range(1,viewy+1):
            offsety = y*self.unit
            self.draw.line([(0,self.ctry+offsety),(self.width,self.ctry+offsety)], fill=(200,200,200))
            self.draw.line([(0,self.ctry-offsety),(self.width,self.ctry-offsety)], fill=(200,200,200))

    def paint(self,fun,color):
        aryPoint = []

        min = int(math.floor(self.min/self.step))
        max = int(math.floor(self.max/self.step))

        for i in range(min,max):
            x = i*self.step
            y = fun(x)

            x = x*self.unit
            y = y*self.unit

            curX = self.ctrx + x
            curY = self.ctry - y

            aryPoint.append((curX,curY))

        self.draw.point(aryPoint,fill=color)


    def show(self):
        self.canvas.show()
    def saveToJPG(self,path):
        self.canvas.save(path,"JPEG")
    def saveToPNG(self,path):
        self.canvas.save(path,"PNG")

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)


if __name__ == '__main__':
    
    drawfun = DrawFun(512,512,-10,10,0.0001,50)


    drawfun.paint(sin,(255,0,0))
    drawfun.paint(cos,(0,255,0))
    drawfun.paint(tan,(0,0,255))

    drawfun.show()

    
    drawfun.saveToPNG("demo.png")
