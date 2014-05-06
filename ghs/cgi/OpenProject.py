#!/usr/bin/python
import cgi
import os

if os.name == 'nt':
	bin_path = '/src/work_scripts/ghs/bin/'
else:
	bin_path='/Users/dane/work_scripts/ghs/bin/'


def main():
	print "Content-type: text/html\n"
	print "In OpenProject.py"
	form = cgi.FieldStorage()
	if form.has_key("name") and form["name"].value != "":
		print "<h1>I will open project named:", form["name"].value,"</h1>"

		command = bin_path + 'open_project.py ' + form["name"].value
		print "executing command: " + command

		os.system(command)
	else:
		print "<h1> Error! link has no project name.</h1>"

main()
