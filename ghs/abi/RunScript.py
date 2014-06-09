#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi import awrde


def main():
    bi.urltools.html_header()
    script_name = abi.urltools.get_parameter("name")

    if script_name:
        abi.urltools.html_message("Running Script: %s" % script_name)
        abi.awrde.RunScript(script_name)
    else:
        abi.urltools.html_error("Script name is required but not supplied")

    abi.urltools.html_footer()


if __name__ == "__main__":
    main()

