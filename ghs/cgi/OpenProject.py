#!/usr/bin/python
import cgi
import os
import sys
import urllib
import urltools


def get_parameter(name):
	if sys.argv[1]:
		# form being executed from command line for testing
		return sys.argv[1]
	else:
		# form being executed from web server
		form = cgi-FieldStorage()
		if (form.has_key(name) and form[name].value != ""):
			return(form[name].value)
		else:
			return False

def get_project(project_url):
	if (http in project_url):
		# web file request, we'll get the project
		(filename,headers) = urllib.urlretrieve(project_url)
		# filename is the name of a temporary file. 
		# the .vin must have the same name
		vinfilename = filename.replace('.emp','.vin')
		vinurl = project_url.replace('.emp','.vin')
		urllib.urlretrieve(vinurl,vinfilename)
	else:
		# local file request
		filename = project_url
	return(filename)

def main():
	print "Content-type: text/html\n"
	print "<head><title>In OpenProject.py</title></head>"
	print "<body>"
	print "<h1>Command debug log</h1>"
	project_name = get_parameter("name")
	if project_name:
		local_name = get_project(project_name)
		print "<p>Opening project: %s</p>" % project_name

		if os.name == 'nt':
			print "<p>On Windows, executing awrde.Open(%s)</p>" % project_name
			import win32com.client
			awrde=win32com.client.Dispatch("MWOApp.MWOffice")
			awrde.Open(project_name)
		else:
			print "<p>On OSX so not executing awrde.Open(%s)</p>" % project_name
	else:
		print "<h2> Error! link has no project name.</h2>"
	print "</body>"

main()


	
