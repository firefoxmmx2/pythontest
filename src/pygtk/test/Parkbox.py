#coding:utf8
'''
Created on 2010-12-12

@author: hooxin
'''
import gtk
import sys
import string
import pygtk


def make_box(homogeneous,spacing,expand,fill,padding):
	'''
		park_start的属性意义
		需要加入的容器，容器间距，是否伸展，是否填充，容器内间距
	'''
	box=gtk.HBox(homogeneous,spacing)
	
	button=gtk.Button('box.pack')
	box.pack_start(button,expand,fill,padding)
	button.show()
	
	button=gtk.Button('(button,')
	box.pack_start(button,expand,fill,padding)
	button.show()
	
	if expand == True:
		button=gtk.Button('True,')
	else:
		button=gtk.Button('False,')
	box.pack_start(button,expand,fill,padding)
	button.show()
	
	padstr='%d)' % padding
	
	button=gtk.Button(padstr)
	box.pack_start(button,expand,fill,padding)
	button.show()
	return box
	
class PackBox1:
	
	def deleteEvent(self,widget,event,data=None) :
		gtk.main_quit()
		return False
	def __init__(self,which):
		
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect('delete_event',self.deleteEvent)
		self.window.set_border_width(10)
		
		box1=gtk.VBox(False,0)
		
		if which == 1:
			label=gtk.Label('HBox(False,0)')
			label.set_alignment(0,0)
			box1.pack_start(label,False,False,0)
			label.show()
			box2=make_box(False,0,False,False,0)
			box1.pack_start(box2,False,False,0)
			box2.show()
			
			separator=gtk.HSeparator()
			box1.pack_start(separator,False,True,5)
			separator.show()
			
			label=gtk.Label('HBox(True,0)')
			label.set_alignment(0,0)
			box1.pack_start(label,False,False,0)
			label.show()
			
		elif which == 2:
			label=gtk.Label('HBox(False,10)')
			label.set_alignment(0,0)
			box1.pack_start(box2,False,False,0)
			box1.show()
			
			box2=make_box(False, 10, True, True, 0)
			box1.pack_start(box2,False,False,0)
			box2.show()
			
		elif which==3:
			box2=make_box(False, 0, False, False, 0)
			label=gtk.Label('end')
			box2.pack_end(label,False,False,0)
			label.show()
			
			box1.pack_start(box2,False,False,0)
			box2.show()
			separator=gtk.HSeparator()
			
			box1.pack_start(separator,False,True,5)
			separator.show();
			
		quitbox=gtk.HBox(False,0)
		button=gtk.Button('quit')
		button.connect('clicked',lambda w:gtk.main_quit())
		quitbox.pack_start(button,True,False,0)
		box1.pack_start(quitbox,False,False,0)
		
		
		self.window.add(box1)
		
		button.show()
		quitbox.show()
		box1.show()
		
		self.window.show()
		
def main():
	gtk.main()
	return 0
		
if __name__=='__main__':
		if len(sys.argv)!=2:
			sys.stderr.write('usage:Packbox.py num, where num is 1,2 or 3.\n')
			sys.exit(1)
		PackBox1(string.atoi(sys.argv[1]))
		main()