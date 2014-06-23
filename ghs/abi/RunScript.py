#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi import awrde
from abi import urltools


def main():
    urltools.html_header()
    script_name = urltools.get_parameter("name")

    if script_name:
        urltools.html_message("Running Script: %s" % script_name)
        awrde.RunScript(script_name)
    else:
        urltools.html_error("Script name is required but not supplied")

    urltools.html_footer()


if __name__ == "__main__":
    main()

