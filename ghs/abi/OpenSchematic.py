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
    print("<head><title>In OpenSchematic.py</title></head>")
    print("<body>")
    print("<h1>Command debug log</h1>")
    schematic_name = get_parameter('name')
    close_all = get_parameter('close')
    tile = get_parameter('tile')
    if schematic_name:
        if os.name == 'nt':
            import win32com.client
            awrde=win32com.client.Dispatch("MWOApp.MWOffice")

            if (close_all == '1'):
                print("<p>Closing all windows</p>")
                for window in awrde.Windows:
                    window.close()
            print("<p>Opening schematic: %s</p>" % schematic_name)
            
            awrde.Project.Schematics(schematic_name).NewWindow()

            mwWTD_Horizontal = 1
            mwWTD_Vertical = 0
            if (tile == 'H'):
                awrde.Windows.Tile(mwWTD_Horizontal)
            elif (tile == 'V'):
                awrde.Windows.Tile(mwWTD_Vertical)
            else:
                awrde.Windows.Cascade()

    else:
        print("<h2> Error! link has no schematic name.</h2>")

    print("</body>")

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        os.environ['QUERY_STRING'] = 'name=' + sys.argv[1]

        main()
    else:
        print("Usage: OpenSchematic.py SchematicName")

