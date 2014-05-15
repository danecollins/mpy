#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()
import sys

def convert_command_to_URL(path):
	# Commands are somewhat in the form of URL's in that they need to be valid enough
	# that the command gets to the AWAC but past that we can change the rest into anything
	# we want.
	#
	# The current command syntax is:
	#     http://localhost:port/COMMAND?arguments
	#
	# which we process in the following way:
	#     1) command is converted to cgi/COMMAND.py
    # 
    # note, if the command already starts with /cgy it is left unmodified
    #       so that testing can be done with full URL's

	# split off arguments if they exist
	args = False
	if '?' in path:
		(url, args) = path.split('?')
	else:
		url = path

    # we need to lowercase the URL so we don't run into case issues
    url = url.lowercase()
	url = "/cgi/" + url
	url = url + '.py'

    # add args back in
	if (args):
		url = url + '?' + args

	return(url)


class RedirectHandler(CGIHTTPServer.CGIHTTPRequestHandler):
	cgi_directories = ['/cgi']

	def do_HEAD(s):
		original_path = s.path
		print >> original_stdout, type(original_path)
		print >> original_stdout, "-- in do_HEAD with path: " + original_path

		if (original_path.lowercase().startswith('/cgi')):
			print >> original_stdout, "-- Path already has /cgi, executing"
			CGIHTTPServer.CGIHTTPRequestHandler.do_GET(s)
		else:
			newpath = convert_command_to_URL(original_path)
			print original_stdout, "-- modified path to: " + newpath
			s.send_response(301)
			s.send_header("Location",newpath)
			s.end_headers()

	def do_GET(s):
		s.do_HEAD()



print "hello there"
original_stdout = sys.stdout
server = BaseHTTPServer.HTTPServer
##  handler = 
server_address = ("", 8008)
## handler.cgi_directories = ['/cgi']
 
httpd = server(server_address, RedirectHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.socket.close()

