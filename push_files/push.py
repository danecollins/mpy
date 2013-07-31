import os, time
import shutil
import sys


### read configuration from file
file = open(sys.argv[1])
for line in file.readlines():
	line = line.rstrip('\n')
	(keyword,data) = line.split('=')
	
	if (keyword == 'FROM'):
		source_dir = data
	elif (keyword == 'TO'):
		dest_dir = data
	elif (keyword == 'FILES'):
		files = data.split(':')
	else:
		print "unknown keyword:", keyword
		
try:
	source_dir
	dest_dir
	files
except NameError:
	print "The config file did not set all the variables"

for file in files:
	source_path = source_dir + file
	dest_path   = dest_dir   + file
	print "comparing ", file

	source_time = os.path.getmtime(source_path)
	try:
		dest_time   = os.path.getmtime(dest_path)
	except WindowsError:
		dest_time   = 0
	
	if (source_time > dest_time):
	 	shutil.copyfile(source_path,dest_path)
	 	print "copied ", file


