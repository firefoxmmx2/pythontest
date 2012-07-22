'''
Created on 2010-12-10

@author: hooxin
'''
import gtk

class HelloWorld:
	def hello(self,widget,data=None):
		print 'Hello World'
	def deleteEvent(self,wiget,event,data=None):
		print 'delete event occured'
		return False
	def destroy(self,widget,data=None):
		gtk.main_quit()
		pass
	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect('delete_event',self.deleteEvent)
		self.window.connect('destroy',self.destroy)
		self.window.set_border_width(10)
		self.button=gtk.Button('Hello World')
		self.button.connect('clicked',self.hello,None)
		self.button.connect_object('clicked',gtk.Widget.destroy,self.window)
		self.window.add(self.button)
		self.button.show()
		self.window.show()
		self.main()
		pass
	def main(self):
		gtk.main()
if __name__ == '__main__':
	hello=HelloWorld()
	pass