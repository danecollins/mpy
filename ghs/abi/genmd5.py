import cgi
import os
import sys
import hashlib
from abi.LoadProject import get_parameter, get_project


def get_file_md5(file):
	md = hashlib.sha1()
	size = 0

	with open(file,'rb') as fp:
		bytes = fp.read()

	for byte in bytes:
		size = size + 1
		md.update(str(byte).encode('utf-8'))
	
	hexval = md.hexdigest()

	return(size,hexval)

if __name__ == "__main__":
	print(len(sys.argv))
	print(sys.argv)
	if (len(sys.argv) < 2 ):
		print('Usage: test_LoadProject.py <file>')
	else:
		(size,digest) = get_file_md5(sys.argv[1])

		print("File Size = " + str(size))
		print("File Digest = '" + digest + "'")
