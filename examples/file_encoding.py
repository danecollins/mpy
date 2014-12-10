from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
import codecs
import StringIO

filename = sys.argv[1]

def binarydiff(f1,f2):
	with open(f1,'rb') as fp:
		a = fp.read()
	with open(f2,'rb') as fp:
		b = fp.read()
	return a == b

def try_with_codecs(filename,coding):
	print("%s: " % coding,end="")
	linenumber=1
	try:
		if coding != 'open':
			fp = codecs.open(filename,'r',encoding=coding)
			fout = codecs.open(filename+coding,'w',encoding=coding)
		else:
			fp = open(filename,'r')
			fout = open(filename+'open','w')
	except:
		print('FAILED on opening file')
		return

	try:
		line = fp.readline()
	except:
		print('FAILED reading first line')
		return
	fout.write(line)

	while line:
		try:
			line = fp.readline()
			linenumber += 1
		except:
			print('FAILED reading line {}'.format(linenumber+1))
			return
		try:
			fout.write(line)
		except:
			print('FAILED on writing line {}'.format(linenumber+1))
			return

	print('successful')
	fp.close()
	fout.close()
	if not binarydiff(filename,filename+coding):
		print("DIFF FAILED")
	os.remove(filename+coding)
	return 

if __name__ == '__main__':
	filename = sys.argv[1]
	try_with_codecs(filename,'latin1')
	try_with_codecs(filename,'utf-8')
	try_with_codecs(filename,'ascii')
	try_with_codecs(filename,'open')


# line.encode('utf-8')  encode line to utf-8
# unicode(line,'utf-8') utf-8 to unicode
