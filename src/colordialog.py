#!/usr/bin/python
#coding=utf8
#filename=colordialog.py
'''
Created on 2010/08/08

@author: hooxin
'''

import sys
from PyQt4 import QtGui,QtCore

class ColorDialog(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		
		color=QtGui.QColor(0,0,0)
		
		self.setGeometry(300,300,250,180)
		self.setWindowTitle('colorDialog')
		
		self.button=QtGui.QPushButton('Dialog',self)
		self.button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.button.move(20,20)
		
		self.connect(self.button, QtCore.SIGNAL('clicked()'),self.showDialog)
		self.setFocus()
		
		self.widget=QtGui.QWidget(self)
		self.widget.setStyleSheet('QWidget {background-color: %s}' % color.name())
		self.widget.setGeometry(130,22,100,100)
		
	def showDialog(self):
		col = QtGui.QColorDialog.getColor()
		
		if col.isValid():
			self.widget.setStyleSheet('QWidget {background-color: %s}' % col.name())
			
app = QtGui.QApplication(sys.argv)
cd = ColorDialog()
cd.show()
sys.exit(app.exec_())