from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter
from collections import namedtuple
import os, time
import shutil
import sys
import re

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


def get_file_list(input_file='Publish.txt'):
	if not os.path.exists(input_file):
		print('No Publish.txt, nothing to do.')
		exit(0)

	try:
		with open(input_file) as fp:
			files = list()
			cp = namedtuple('CopyPairs',['frompath','topath','tofile'])
			for line in fp:
				line = line.strip()
				if line != '':
					(frompath,topath)= re.split(r'\s*->\s*', line)
					### topath can be a directory or a full filename
					### determine which by seeing if the last component
					### has a dot in it which makes it a file
					###
					### NOTE: if file has no . this won't work!
					###
					pathelements = re.split(r'\\',topath)
					if '.' not in pathelements[-1]:
						pathelements.append(frompath)

					topath = os.sep.join(pathelements[:-1])
					tofile = os.sep.join(pathelements)

					files.append(cp._make([frompath,topath,tofile]))
	except:
		print('Error parsing Publish.txt file')
		print("Unexpected error:", sys.exc_info()[0])
		return(None)
	return(files)


def copy_files(files,execute,verbose_mode):
	global did_something

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

		if not os.path.isdir(file.topath):
			print('Destination directory %s does not exist!' % file.topath)
			print('Exiting...')
			exit(1)

		if os.path.exists(file.tofile):
			try:
				dest_time   = os.path.getmtime(file.tofile)
			except:
				print('Could not get the modified time of: %s!' % file.tofile)
				print('Error is:', sys.exc_info()[0])
				print('Exiting...')
				exit(1)
		else:
			dest_time = 0

		if (source_time > dest_time):
			did_something = True
			if execute:
				shutil.copyfile(file.frompath,file.tofile)
			print('copying %s to %s' % (file.frompath,file.tofile))
		else:
			if verbose_mode:
				print('destination file %s is up to date' % file.tofile)

if __name__ == '__main__':
	did_something = False
	if '-s' in sys.argv:
		print('=== Running in simulation mode, will not copy files. ===')
		execute = False
	else:
		execute = True

	verbose_mode = True if '-v' in sys.argv else False

	files = get_file_list()
	copy_files(files,execute,verbose_mode)

	if not did_something:
		print('Nothing to be done.')



