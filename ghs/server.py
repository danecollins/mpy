#!/usr/bin/env python
 
import http.server
import http.server
import cgitb; cgitb.enable()
import sys
import abi.urltools
import os

debug=True
os.environ["PYTHONPATH"] = os.getcwd()
print("Setting PYTHONPATH to: " + os.getcwd())

def dprint(string):
    if (debug):
        print(string, file=original_stdout)


class RedirectHandler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/abi']

    def do_HEAD(s):
        original_path = s.path
        dprint('-- original path: ' + original_path)

        newpath = abi.urltools.convert_command_to_URL(original_path)
        if not newpath:
            dprint('-- path not modified')
            http.server.CGIHTTPRequestHandler.do_GET(s)
        else:
            dprint("-- modified path to: " + newpath)
            s.send_response(301)
            s.send_header("Location",newpath)
            s.end_headers()

    def do_GET(s):
        s.do_HEAD()



print("Sarting Server")
original_stdout = sys.stdout
server = http.server.HTTPServer
##  handler = 
server_address = ("", 8008)
 
httpd = server(server_address, RedirectHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.socket.close()

