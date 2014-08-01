#!/usr/bin/python
import cgi
import os
import sys
from abi import urltools
from abi import awrde

#DOC name: OpenUserFolder
#DOC title: Open the contents of a User Folder
#DOC desc: This command closes all open windows, opens all the contents of folder and then perform a tile command.
#DOC args: name* - name of the folder to be opened
#DOC web: http://localhost:8008/OpenUserFolder?name=AmpFolder
#DOC wiki: OpenUserFolder AmpFolder

def main():
    urltools.html_header()
    folder_name = urltools.get_parameter('name')

    if folder_name:
        awrde.OpenUserFolder(folder_name)

    else:
        urltools.html_error('You must specify the name parameter with the OpenUserFolder command')
        urltools.html_error('use OpenUserFolder?name=<folder_name>')

    urltools.html_footer()


if __name__ == "__main__":
    main()

