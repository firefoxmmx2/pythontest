#coding:utf8
'''
Created on 2010-12-19

@author: hooxin
'''

import gtk

class CheckButton:
	def callback(self,widget,data=None):
		print ('%s was toggle %s ' % \
		(data,("off","on")[widget.get_active()]))
		
	def delete_event(self,widget,data=None):
		gtk.main_quit()
		return False
	
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL);
		self.window.set_title('check button')
		self.window.connect('delete_event',self.delete_event)
		self.window.set_border_width(20)
		
		vbox=gtk.VBox(True,2)
		self.window.add(vbox)
		
		button=gtk.CheckButton('check button 1')
		button.connect('toggled',self.callback,'check button 1')
		button.show()
		vbox.pack_start(button,True,True,2)
		
		button=gtk.CheckButton('check button 2')
		button.connect('toggled',self.callback,'check button 2')
		button.show()
		vbox.pack_start(button,True,True,2)
		vbox.show()
		self.window.show()
		
def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	CheckButton()
	main()
