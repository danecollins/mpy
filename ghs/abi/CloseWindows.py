#!/usr/bin/python
import cgi
import os
import sys
from abi import awrde
from abi import urltools

#DOC name: CloseWindows
#DOC title: Closes all windows
#DOC desc: Closes all the currently open windows
#DOC web: http://localhost:8008/CloseWindows
#DOC wiki: CloseWindows

def main():
	urltools.html_header()
	awrde.CloseWindows()
	urltools.html_footer()

if __name__ == "__main__":
    main()

