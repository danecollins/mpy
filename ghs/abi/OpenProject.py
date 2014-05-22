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

def get_project(project_url):
        
    if (project_url.startswith('http')):
        # web file request, we'll get the project
        filename=False
        try:
            (filename,headers) = urllib.request.urlretrieve(project_url)
        except URLError as e:
            print(e.reason)
            
        # filename is the name of a temporary file.     
        # on windows, the .emp extension may not be preserved
        if not filename.endswith('.emp'):
            os.rename(filename,filename+'.emp')
            filename = filename + '.emp'
            
        # the .vin must have the same name
        vinfilename = filename.replace('.emp','.vin')
        vinurl = project_url.replace('.emp','.vin')
        try:
            (vname,vheaders) = urllib.request.urlretrieve(vinurl,vinfilename)
        except URLError as e:
            print(e.reason)
           
    else:
        # local file request
        filename = project_url

    return(filename)

def main():
    print("Content-type: text/html\n")
    print("<head><title>In OpenProject.py</title></head>")
    print("<body>")
    print("<h1>Command debug log</h1>")
    project_name = get_parameter("name")
    if project_name:
        local_name = get_project(project_name)
        print("<p>Opening project: %s</p>" % local_name)

        if os.name == 'nt':
            print("<p>On Windows, executing awrde.Open(%s)</p>" % local_name)
            import win32com.client
            awrde=win32com.client.Dispatch("MWOApp.MWOffice")
            awrde.Open(local_name)
        else:
            print("<p>On OSX so not executing awrde.Open(%s)</p>" % local_name)
    else:
        print("<h2> Error! link has no project name.</h2>")
    print("</body>")

if __name__ == "__main__":
        main()

