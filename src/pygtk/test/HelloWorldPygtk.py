
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="hooxin"
__date__ ="$2010-12-9 23:53:24$"
import pygtk
import gtk

class HelloWorld:
    def hello(self,widget,data=None):
        print 'Hello World'
    def deleteEvent(self,widget,event,data=None):
        print 'delete event occurred'
        return False
    def destroy(self,widget,data=None):
        gtk.main_quit()
    def __int__(self):
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('deleteEvent',self.deleteEvent)
        self.window.connect('destroy',self.destroy)
        self.window.set_border_width(10)
        self.button = gtk.Button('Hello World')
        self.button.connect('clicked', self.hello,None)
        self.button.connect_object('clicked'.gtk.Widget.destroy,self.window)
        self.window.add(self.button)
        self.button.show()
        self.window.show( )

    def main(self):
        gtk.main()
if __name__ == "__main__":
    hello=HelloWorld(  )
    hello.main()
