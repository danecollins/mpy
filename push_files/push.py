import os, time

## TODO: figure out the right way to handle
## file paths that work on osx and windows

files = ["time_test.txt"]
source_dir = '.\\'
dest_dir = '\\\\ts1a\\dane\\revrec\\'

for file in files:
	source_path = source_dir + file
	dest_path   = dest_dir   + file
	print "comparing ", source_path, "with", dest_path
	#
	# source_time = os.path.getmtime(source_path)
	# dest_time   = os.path.getmtime(dest_path)
	
	# if (source_time > dest_time):
	# 	os.path.copy(source_path,dest_path)
	# 	print "copied ", file


