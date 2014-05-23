#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError


def get_parameter(name):

    # form being executed from web server
    form = cgi.FieldStorage()
    if (name in form and form[name].value != ""):
        url = form[name].value

        # BUG/FEATURE
        # the CGI mechanism collapses multiple / to a single / (which would normally be on)
        # but it makes http:// into http:/ which is not legal.  This adds the / back in.
        if (url.startswith('https:') and not url.startswith('https://')):
            url = url.replace('https:/','https://')
        if (url.startswith('http:') and not url.startswith('http://')):
            url = url.replace('http:/','http://')   
        return(url)
    else:
        return False

def main():
    print("Content-type: text/html\n")
    print("<head><title>In RunScript.py</title></head>")
    print("<body>")
    print("<h1>Command debug log</h1>")
    script_name = get_parameter('name')

    if script_name:
        if os.name == 'nt':
            import win32com.client
            awrde=win32com.client.Dispatch("MWOApp.MWOffice")

            print("<p>Running Script: %s</p>" % script_name)
            awrde.Project.ProjectScripts.Item(script_name).Routines.Item("Main").Run()

    else:
        print("<h2> Error! link has no script name.</h2>")

    print("</body>")

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        os.environ['QUERY_STRING'] = 'name=' + sys.argv[1]

        main()
    else:
        print("Usage: RunScript.py SchematicName")

