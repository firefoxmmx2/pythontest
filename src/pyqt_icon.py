#!/usr/bin/python
# coding=utf8
# filename=pyqt_icon
'''
Created on 2010/07/28

@author: hooxin
'''

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Icon');
		self.setWindowIcon(QtGui.QIcon('/home/hooxin/Pic/wpc1280.jpg'))
app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
