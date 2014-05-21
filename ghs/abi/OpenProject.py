#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError


def get_parameter(name):
    if len(sys.argv) > 1:
        # form being executed from command line for testing
        return sys.argv[1]
    else:
        # form being executed from web server
        form = cgi.FieldStorage()
        if (name in form and form[name].value != ""):
            url = form[name].value
            print('-- in get_parameter with url of: ' + url, file=fp)

            # BUG/FEATURE
            # the CGI mechanism collapses multiple / to a single / (which would normally be on)
            # but it makes http:// into http:/ which is not legal.  This adds the / back in.
            if (url.startswith('https:') and not url.startswith('https://')):
                url = url.replace('https:/','https://')
            if (url.startswith('http:') and not url.startswith('http://')):
                url = url.replace('http:/','http://')   
            print('-- returning with url of: ' + url, file=fp)
            return(url)
        else:
            return False

def get_project(project_url):
    try:
        fp
    except:
        fp = sys.stdout
        
    if (project_url.startswith('http')):
        # web file request, we'll get the project
        print('----- getting: ' + project_url,file=fp)
        filename=False
        print(type(project_url),file=fp)
        try:
            (filename,headers) = urllib.request.urlretrieve(project_url)
        except URLError as e:
            print(e.reason,file=fp)
            
        print('----- received file: ' + filename, file=fp)
        # filename is the name of a temporary file.
        
        # on windows, the .emp extension may not be preserved
        if not filename.endswith('.emp'):
            os.rename(filename,filename+'.emp')
            filename = filename + '.emp'
            print('----- renamed file to: ' + filename,file=fp)
            
        # the .vin must have the same name
        vinfilename = filename.replace('.emp','.vin')
        vinurl = project_url.replace('.emp','.vin')
        print('----- getting: ' + vinurl,file=fp)
        print('----- and storing as: ' + vinfilename,file=fp)
        try:
            (vname,vheaders) = urllib.request.urlretrieve(vinurl,vinfilename)
        except URLError as e:
            print(e.reason,file=fp)
           
        print('----- received file: ' + vinfilename,file=fp)
    else:
        # local file request
        filename = project_url
        print('----- local file request: ' + filename,file=fp)
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
    with open('c:\\src\\work_scripts\\ghs\\OP.log','w') as fp: 
        main()

