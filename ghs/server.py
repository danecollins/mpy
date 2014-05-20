#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()
import sys
import urltools

def convert_command_to_URL(path):
    """ Checks whether url is a command and fixes it """
    # Commands are somewhat in the form of URL's in that they need to be valid enough
    # that the command gets to the AWAC but past that we can change the rest into anything
    # we want.
    #
    # The current command syntax is:
    #     http://localhost:port/COMMAND?arguments
    #
    # which we process in the following way:
    #     1) command is converted to cgi/COMMAND.py

    # Define the commands we'll fix up
    command_list = ['OpenProject','OpenSchematic','OpenGraph']
    # split up the url
    command_url = urltools.url(path)

    # we need to lowercase the command so we don't run into case issues
    command = command_url.get_filename()
    if (command in command_list):
        newcommand = "cgi/" + command + '.py'

        # add args back in
        newurl = command_url.replace_filename(newcommand)
        return(newurl)
    else:
        # not a command, do nothing
        return(False)

class RedirectHandler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi']

    def do_HEAD(s):
        original_path = s.path

        newpath = convert_command_to_URL(original_path)
        if not newpath:
            CGIHTTPServer.CGIHTTPRequestHandler.do_GET(s)
        else:
            print original_stdout, "-- modified path to: " + newpath
            s.send_response(301)
            s.send_header("Location",newpath)
            s.end_headers()

    def do_GET(s):
        s.do_HEAD()



print "Sarting Server"
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

