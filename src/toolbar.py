#!/usr/bin/python
#coding=utf8
#filename=toolbar.py

'''
Created on 2010/07/29

@author: hooxin
'''
import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		self.resize(250,150)
		self.setWindowTitle('toolbar')
		self.exit = QtGui.QAction(QtGui.QIcon(u'/home/hooxin/Pic/术士.jpg'),'exit',self)
		self.exit.setShortcut('Ctrl+Q')
		self.connect(self.exit, QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))
		
		self.toolbar = self.addToolBar('exit')
		self.toolbar.addAction(self.exit)
		

app=QtGui.QApplication(sys.argv)
main=MainWindow()
main.show()
sys.exit(app.exec_())