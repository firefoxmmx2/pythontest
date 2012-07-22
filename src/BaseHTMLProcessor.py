#!/usr/bin/python
# coding=utf8

# vim:ts=4
from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLprocessor(SGMLParser):
	def reset(self):
		self.pieces=[]
		SGMLParser.reset(self)

	def unknown_starttag(self,tag,attrs):
		strattrs=''.join([' %s="%s"' % (key,value) for key,value in attrs])
		self.pieces.append('<%(tag)s%(strattrs)>' % locals())

	def unknown_endtag(self,tag):
		self.pieces.append("</%(tag)>" % locals())

	def handle_charref(self,ref):
		self.pieces.append("$#%(ref)s;" % locals())

	def handle_entityref(self,ref):
		self.pieces.append('&%(ref)s' % locals())
		if htmlentitydefs.entitydefs.has_key(ref):
			self.pieces.append(";")

	def handler_data(self,text):
		self.pieces.append(text)

	def handler_comment(self,text):
		self.pieces.append('<!--%(text)s-->'% locals())
	def handler_pi(self,text):
		self.pieces.append('<?%(text)s>'% locals())
	def handler_decl(self,text):
		self.pieces.append('<!%(text)s>'% locals())
	def output(self):
		return ''.join(self.pieces)

