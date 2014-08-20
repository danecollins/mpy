#!/usr/bin/python
import cgi
import os
import sys
from abi import awrde
from abi import urltools

#DOC name: TileVertical
#DOC title: Tile open windows vertically
#DOC desc: Tiles the open windows vertically
#DOC web: http://localhost:8008/TileVertical
#DOC wiki: TileVertical

def main():
    urltools.html_header()
    awrde.TileWindowsVertical()
    urltools.html_footer()

if __name__ == "__main__":
    main()

