from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter
from collections import namedtuple
import os, time
import shutil
import sys

#####################################################################
##
## publish.py - utility to push new files to their dest
##            - something you would use make for if it existed on windows
##
## Usage: publish.py [-s]
##            - copy files as dictated in Publish.txt
##            - -s(imulate) option causes it to just print what would happen
## 
## Notes: A Publish.txt must exist in the directory in which it is run
##        Publish.txt has the directives of what files to copy.
##
## Publish.txt syntax: 
##             file_a->fileb - copy file_a to file_b if it is newer
##                           - destination is replaced if older
##             file_a->dir/  - if last character of dir is / then it's a dir
##                             and destination becomes dir/file_a    
##         
#####################################################################

did_something = False
if '-s' in sys.argv:
	print('=== Running in simulation mode, will not copy files. ===')
	execute = False
else:
	execute = True

verbose_mode = True if '-v' in sys.argv else False

if not os.path.exists('Publish.txt'):
	print('No Publish.txt, nothing to do.')
	exit(0)

try:
	with open('Publish.txt') as fp:
		files = list()
		cp = namedtuple('CopyPairs',['frompath','topath'])
		for line in fp:
			line = line.strip()
			if line != '':
				(frompath,topath)= line.split('->')
				frompath = frompath.strip()
				topath   = topath.strip()
				if os.path.exists(topath):
					if os.path.isdir(topath):
						# destination is a directory so create filename
						topath = topath + '\\' + frompath
					files.append(cp._make([frompath,topath]))
				else:
					print('Destination directory %s does not exist! Skipping...' % topath)
except:
	print('Error parsing Publish.txt file')
	print("Unexpected error:", sys.exc_info()[0])
	exit(1)

if verbose_mode:
	for x in files:
		print('Work to be done:')
		print('   From: ',x.frompath)
		print('   To:   ',x.topath)
		print()


for file in files:

	if not os.path.exists(file.frompath):
		print('Source file: %s does not exist! Skipping...' % file.frompath)
		continue

	try:
		source_time = os.path.getmtime(file.frompath)
	except:
		print('Could not get the modified time of: %s!' % file.frompath)
		print('Error is:', sys.exc_info()[0])
		print('Exiting...')
		exit(1)

	if os.path.exists(file.topath):
		try:
			dest_time   = os.path.getmtime(file.topath)
		except:
			print('Could not get the modified time of: %s!' % file.frompath)
			print('Error is:', sys.exc_info()[0])
			print('Exiting...')
			exit(1)
	else:
		dest_time = 0

	if (source_time > dest_time):
		did_something = True
		if execute:
			shutil.copyfile(file.frompath,file.topath)
		print('copying %s to %s' % (file.frompath,file.topath))

if not did_something:
	print('Nothing to be done.')



