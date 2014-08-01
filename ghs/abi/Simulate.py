#!/usr/bin/python
import cgi
import os
import sys
from abi import awrde
from abi import urltools

#DOC name: Simulate
#DOC title: Simulate the project
#DOC desc: Simulates the project file
#DOC web: http://localhost:8008/Simulate
#DOC wiki: Simulate

def main():
	urltools.html_header()
	awrde.Simulate()
	urltools.html_footer()

if __name__ == "__main__":
    main()

