#!/usr/bin/python
# coding=utf8
# filename=pyqt_simple

'''
Created on 2010/07/28

@author: hooxin
'''


import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(200,200)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())
