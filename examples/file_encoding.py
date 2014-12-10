from __future__ import print_function
from __future__ import unicode_literals
import sys
import codecs
import StringIO

filename = sys.argv[1]

def try_with_open(filename):
	s = try_with_codecs(filename,'std_open',use_codecs=False)
	with open('out.txt','w') as fp:
		fp.write(s)

def try_with_codecs(filename,coding,use_codecs=True):
	print("%s: " % coding,end="")
	linenumber=1
	try:
		if use_codecs:
			fp = codecs.open(filename,'r',encoding=coding)
		else:
			fp = open(filename,'r')
	except:
		print('FAILED on opening file')
		return

	out = StringIO.StringIO()

	try:
		line = fp.readline()
	except:
		print('FAILED reading first line')
		return

	while line:
		try:
			line = fp.readline()
			linenumber += 1
		except:
			print('FAILED reading line {}'.format(linenumber+1))
			return
		try:
			print(line,file=out)
		except:
			print('FAILED on writing line {}'.format(linenumber+1))
			return

	print('successful')
	return out.getvalue()

if __name__ == '__main__':
	filename = sys.argv[1]
	try_with_codecs(filename,'latin1')
	try_with_codecs(filename,'utf-8')
	try_with_codecs(filename,'ascii')
	try_with_open(filename)


# line.encode('utf-8')  encode line to utf-8
# unicode(line,'utf-8') utf-8 to unicode
