#!/usr/bin/python
#coding=utf8
#filename=menubar.py
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
		self.setWindowTitle('menubar')
		exit=QtGui.QAction(QtGui.QIcon(u'/home/hooxin/Pic/术士.jpg'),'exit',self)
		exit.setShortcut('Ctrl+Q')
		exit.setStatusTip('exit application')
		self.connect(exit, QtCore.SIGNAL('triggerd()'),QtCore.SLOT('close()'))
		
		self.statusBar()
		menubar=self.menuBar()
		sss=menubar.addMenu('&File')
		sss.addAction(exit)
		
app=QtGui.QApplication(sys.argv)
main=MainWindow()
main.show()
sys.exit(app.exec_())