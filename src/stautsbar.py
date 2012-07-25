#!/usr/bin/python
#coding=utf8
'''
Created on 2010/07/29

@author: hooxin
'''

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(250,150)
		self.setWindowTitle('statusbar')
		statusBar = self.statusBar()
		statusBar.showMessage('Ready')
		
app=QtGui.QApplication(sys.argv)
main=MainWindow()
main.show()
sys.exit(app.exec_())