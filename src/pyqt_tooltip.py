#!/usr/bin/python
# coding=utf8
# filename=pyqt_tooltip.py
'''
Created on 2010/07/29

@author: hooxin
'''

import sys
from PyQt4 import QtGui

class Tooltip(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Tooltip')
		
		self.setToolTip('This is <B>QWidget</B> widget')
		QtGui.QToolTip.setFont(QtGui.QFont('OldEnghlish',10))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())