#!/usr/bin/python
import cgi
import os
import sys
from abi import urltools
from abi import awrde

#DOC name: OpenSystemDiagram
#DOC title: Open a system diagram
#DOC desc: This command opens a system diagram in a new window. It has options to close all open windows as well as tile or cascade the windows.
#DOC args: name* - name of the system diagram to be opened
#DOC args: close - a value of 0 does nothing, a value of 1 causes all existing windows to be closed
#DOC args: tile - a value of 'H' causes a horizontal tiling to be done, a value of 'V' causes a vertical tiling and a value of 'N' disables the tiling
#DOC web: http://localhost:8008/OpenSystemDiagram?name=Tranceiver;close=1;tile=H
#DOC wiki: OpenSystemDiagram Tranceiver

def main():
    urltools.html_header()
    name = urltools.get_parameter('name')
    close_all = urltools.get_parameter('close')
    tile = urltools.get_parameter('tile')

    if name:
        if (close_all):
            awrde.CloseWindows()
        awrde.OpenSystemDiagram(name)

        if (tile == 'H'):
            awrde.TileWindowsHorizontal()
        elif (tile == 'V'):
            awrde.TileWindowsVertical()
        else:
            awrde.CascadeWindows()

    else:
        urltools.html_error('You must specify the name parameter with the OpenSystemDiagram command')
        urltools.html_error('use OpenSystemDiagram?name=<schematic_name>')

    urltools.html_footer()


if __name__ == "__main__":
    main()

