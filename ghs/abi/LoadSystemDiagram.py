#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi import urltools
from abi import awrde

#DOC name: LoadSystemDiagram
#DOC title: Import a system diagram diagram file
#DOC desc: This command imports a system diagram (.sys) file into a project. The name of the system diagram is the URL to the .sys file. Currently Dropbox is used to store projects due to its convenience but they can also be attached to the wiki.
#DOC args: name - URL to the system diagram to be downloaded and imported
#DOC web: http://localhost:8008/LoadSystemDiagram?name=http://dl.dropbox.com/123456/amp.sys
#DOC wiki: LoadSystemDiagram http://dl.dropbox.com/123456/amp.sys

def main():
    urltools.html_header()
    file_name = urltools.get_parameter("name")
    if file_name:
        imported_name = os.path.basename(file_name).strip('.sys')
        local_name = urltools.get_file(file_name,'sys')
        urltools.html_message("Opening system diagram: %s" % local_name)
        awrde.LoadSystemDiagram(local_name, imported_name)
    else:
        urltools.html_error("Link has no system diagram name.")

    urltools.html_footer()

if __name__ == "__main__":
    main()

