import os, time
import shutil

## TODO: figure out the right way to handle
## file paths that work on osx and windows

files = ["time_test.txt" , "fubar.txt"]
source_dir = '.\\'
dest_dir = '\\\\ts1a\\dane\\push_files\\'

for file in files:
	source_path = source_dir + file
	dest_path   = dest_dir   + file
	print "comparing ", source_path, "with", dest_path

	source_time = os.path.getmtime(source_path)
	try:
		dest_time   = os.path.getmtime(dest_path)
	except WindowsError:
		dest_time   = 0
	
	if (source_time > dest_time):
	 	shutil.copyfile(source_path,dest_path)
	 	print "copied ", file


