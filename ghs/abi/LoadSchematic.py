#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi import urltools
from abi import awrde

#DOC name: LoadSchematic
#DOC title: Import a schematic file
#DOC desc: This command imports a schematic (.sch) file into a project. The name of the schematic is the URL to the .sch file. Currently Dropbox is used to store projects due to its convenience but they can also be attached to the wiki.
#DOC args: name - URL to the schematic to be downloaded and imported
#DOC web: http://localhost:8008/LoadSchematic?name=http://dl.dropbox.com/123456/amp.sch
#DOC wiki: LoadSchematic http://dl.dropbox.com/123456/amp.sch

def main():
    urltools.html_header()
    file_name = urltools.get_parameter("name")
    if file_name:
        local_name = urltools.get_file(file_name,'sch')
        urltools.html_message("Opening schematic: %s" % local_name)
        awrde.LoadSchematic(local_name)
    else:
        urltools.html_error("Link has no schematic name.")

    urltools.html_footer()

if __name__ == "__main__":
    main()

