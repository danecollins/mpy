#!/usr/bin/python
import cgi
import os
import sys
from abi import awrde
from abi import urltools

#DOC name: TileHorizontal
#DOC title: Tile open windows horizontally
#DOC desc: Tiles the open windows horizontally
#DOC web: http://localhost:8008/TileHorizontal
#DOC wiki: TileHorizontal

def main():
    urltools.html_header()
    awrde.TileWindowsHorizontal()
    urltools.html_footer()

if __name__ == "__main__":
    main()

