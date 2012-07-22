'''
Created on 2011-1-19

@author: hooxin
'''

import re
from BaseHTMLProcessor import BaseHTMLprocessor

class Dialectizer(BaseHTMLprocessor):
	subs=()
	
	def reset(self):
		self.verbatim=0
		BaseHTMLprocessor.reset(self)
	
	def start_pre(self,attrs):
		self.unknown_starttag(self, attrs)
	
	def end_pre(self):
		self.unknown_endtag('pre')
		self.verbatim-=1
	
	def handle_data(self,text):
		self.pieces.append(self.verbatim and text or self.process(text))
	
	def process(self,text):
		for formPattern,toPattern in self.subs:
			text=re.sub(formPattern , toPattern, text)
		return text
	
class ChefDialectizer(Dialectizer):
	subs = ((r'a([nu])', r'u\1'),
            (r'A([nu])', r'U\1'),
            (r'a\B', r'e'),
            (r'A\B', r'E'),
            (r'en\b', r'ee'),
            (r'\Bew', r'oo'),
            (r'\Be\b', r'e-a'),
            (r'\be', r'i'),
            (r'\bE', r'I'),
            (r'\Bf', r'ff'),
            (r'\Bir', r'ur'),
            (r'(\w*?)i(\w*?)$', r'\1ee\2'),
            (r'\bow', r'oo'),
            (r'\bo', r'oo'),
            (r'\bO', r'Oo'),
            (r'the', r'zee'),
            (r'The', r'Zee'),
            (r'th\b', r't'),
            (r'\Btion', r'shun'),
            (r'\Bu', r'oo'),
            (r'\BU', r'Oo'),
            (r'v', r'f'),
            (r'V', r'F'),
            (r'w', r'w'),
            (r'W', r'W'),
            (r'([a-z])[.]', r'\1.  Bork Bork Bork!'))
class OldDialectizer(Dialectizer):
	subs = ((r'i([bcdfghjklmnpqrstvwxyz])e\b', r'y\1'),
            (r'i([bcdfghjklmnpqrstvwxyz])e', r'y\1\1e'),
            (r'ick\b', r'yk'),
            (r'ia([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
            (r'e[ea]([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
            (r'([bcdfghjklmnpqrstvwxyz])y', r'\1ee'),
            (r'([bcdfghjklmnpqrstvwxyz])er', r'\1re'),
            (r'([aeiou])re\b', r'\1r'),
            (r'ia([bcdfghjklmnpqrstvwxyz])', r'i\1e'),
            (r'tion\b', r'cioun'),
            (r'ion\b', r'ioun'),
            (r'aid', r'ayde'),
            (r'ai', r'ey'),
            (r'ay\b', r'y'),
            (r'ay', r'ey'),
            (r'ant', r'aunt'),
            (r'ea', r'ee'),
            (r'oa', r'oo'),
            (r'ue', r'e'),
            (r'oe', r'o'),
            (r'ou', r'ow'),
            (r'ow', r'ou'),
            (r'\bhe', r'hi'),
            (r've\b', r'veth'),
            (r'se\b', r'e'),
            (r"'s\b", r'es'),
            (r'ic\b', r'ick'),
            (r'ics\b', r'icc'),
            (r'ical\b', r'ick'),
            (r'tle\b', r'til'),
            (r'll\b', r'l'),
            (r'ould\b', r'olde'),
            (r'own\b', r'oune'),
            (r'un\b', r'onne'),
            (r'rry\b', r'rye'),
            (r'est\b', r'este'),
            (r'pt\b', r'pte'),
            (r'th\b', r'the'),
            (r'ch\b', r'che'),
            (r'ss\b', r'sse'),
            (r'([wybdp])\b', r'\1e'),
            (r'([rnt])\b', r'\1\1e'),
            (r'from', r'fro'),
            (r'when', r'whan'))
def translate(url,dialectName='chef'):
	import urllib
	sock=urllib.urlopen(url)
	htmlSource=sock.read()
	sock.close()
	parserName='%sDialectizer'%dialectName.capitalize()
	parserClass=globals()[parserName]
	parser = parserClass()
	parser.feed(htmlSource)
	parser.close()
	return parser.output()

def test(url):
	for dialect in ('chef','fudd','olde'):
		outfile='%s.html'% dialect
		fsock=open(outfile,'wb')
		fsock.write(translate(url, dialect))
		fsock.close()
		import webbrowser
		webbrowser.open_new(outfile)
	
if __name__ =="__main__":
	test('http://diveintopython.org/odbchelper_list.html')