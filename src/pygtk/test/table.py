#coding:utf8
'''
Created on 2010-12-12

@author: hooxin
'''
import gtk

class Table:
	def callback(self,widget,event,data=None):
		print 'Hello again - %s was pressed' % data
	
	def delete_event(self,widget,event,data=None):
		gtk.main_quit()
		return False
	
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		
		self.window.set_title('Table')
		self.window.connect('delete_event',self.delete_event)
		self.window.set_border_width(20)
		#创建一个2X2表格
		table=gtk.Table(3,2,True)
		button=gtk.Button('button 1')
		button.connect('clicked',self.callback,'button 1')
		self.window.add(table)
		#放置一个button在cell 1 row 1
		table.attach(button,1,2,0,1)
		button.show()
		
		button=gtk.Button('button 2')
		button.connect('clicked',self.callback,'button 2')
		button.show()
		table.attach(button,0,1,0,1)
		
		button=gtk.Button('quit')
		button.connect('clicked',lambda w: gtk.main_quit())
		#放置一个按钮在CELL 0
		table.attach(button,0,2,1,2)
		button.show()
		table.show()
		self.window.show()
		
def main():
	gtk.main()
	return 0

if __name__=='__main__':
	Table()
	main()