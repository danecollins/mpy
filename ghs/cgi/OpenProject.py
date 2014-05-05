#!/usr/bin/python
import cgi
import os

bin_path='/Users/dane/work_scripts/ghs/bin/'

def main():
	print "Content-type: text/html\n"
	form = cgi.FieldStorage()
	if form.has_key("name") and form["name"].value != "":
		print "<h1>I will open project named:", form["name"].value,"</h1>"

		os.system(bin_path + 'open_project.py ' + form["name"].value)
	else:
		print "<h1> Error! link has no project name.</h1>"

main()
