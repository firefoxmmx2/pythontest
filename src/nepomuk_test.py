#!/usr/bin/env python2
# coding:utf8
# filename:nepomuk_test.py
# descption:a example for nepomuk


import sys
from PyQt4 import QtCore
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyKDE4.nepomuk import Nepomuk


dummy_file = open('fummy.txt','w')
dummy_file.write('测试\n')
dummy_file.close()

result = Nepomuk.ResourceManager.instance().init()
if result != 0:
    sys.exit(result)

file_info = QtCore.QFileInfo("fummy.txt")
absolute_path = file_info.absoluteFilePath()
resource = Nepomuk.Resource(kdecore.KUrl(absolute_path))

tagText = "tagtest"
tag = Nepomuk.Tag(tagText)
tag.setLabel(tagText)

resource.addTag(tag) # add tag
resource.setDescription("This is an example comment.") # set description
resource.setRating(4); # set rating

print "resource.exists() == ",resource.exists()
print "resource.isVaid() == ",resource.isValid()
print "resource.identifiers().length == ", len(resource.identifiers())
print "resource.type() == ",resource.type()
print "resource.types() == ",resource.types()
print "resource.resourceUri() == ",resource.resourceUri()
print "resource.resourceType () == ",resource.resourceType() 
print "resource.identifierUri() == ",resource.identifierUri()
