#!/usr/bin/python
import cgi
import os
import sys
from abi import urltools
from abi import awrde


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

