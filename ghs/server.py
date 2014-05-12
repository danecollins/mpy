#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()
import sys

def fixURL(path):
	# remove arguments if they exist
	args = False
	if (path.find('?') <> -1):
		(url, args) = path.split('?')

	# does command start with cgi
	if not (url[0:3] == "/cgi"):
		url = "/cgi/" + url

	# does command end in .py
	if not (url[-3:] == '.py'):
		url = url + '.py'

	if (args):
		url = url + '?' + args

	return(url)


class RedirectHandler(CGIHTTPServer.CGIHTTPRequestHandler):
	cgi_directories = ['/cgi']

	def do_HEAD(s):
		original_path = s.path
		print >> original_stdout, type(original_path)
		print >> original_stdout, "-- in do_HEAD with path: " + original_path

		if (original_path.find('.py') <> -1):
			print >> original_stdout, "-- Path already has .py, executing"
			CGIHTTPServer.CGIHTTPRequestHandler.do_GET(s)
		else:
			newpath = fixURL(original_path)
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

