#!/usr/bin/python
#coding=utf8
#filename=fontdialog.py
'''
Created on 2010/08/09

@author: hooxin
'''

import sys
from PyQt4 import QtGui,QtCore

class FontDialog(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
#		创建水平布局
		hbox = QtGui.QHBoxLayout()
#		设置位置和高度
		self.setGeometry(300,300,250,150)
#		设置窗口名称
		self.setWindowTitle('FontDialog')
		
#		创建按钮
		button = QtGui.QPushButton('Dialog',self)
#		设置焦点模式
		button.setFocusPolicy(QtCore.Qt.NoFocus)
#		移动位置，或者设置位置
		button.move(20,20)
		
#		向水平布局添加按钮
		hbox.addWidget(button)
		
#		事件绑定
		self.connect(button, QtCore.SIGNAL('clicked()'),self.showDialog)
		
#		创建标签面板
		self.label = QtGui.QLabel('Knowledge only matters', self)
		self.label.move(130,20)
		
		hbox.addWidget(self.label,1)
#		设置本窗体布局为水平布局
		self.setLayout(hbox)
		
	def showDialog(self):
#		创建一个字体选择窗口，并且返回字体和是否信息
		font,ok = QtGui.QFontDialog.getFont()
		
		if ok:
			self.label.setFont(font)

app = QtGui.QApplication(sys.argv)
fd = FontDialog()
fd.show()
app.exec_()
		