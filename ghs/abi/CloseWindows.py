#!/usr/bin/python
import cgi
import os
import sys
from abi import awrde
from abi import urltools


def main():
	urltools.html_header()
	awrde.CloseWindows()
	urltools.html_footer()

if __name__ == "__main__":
    main()

