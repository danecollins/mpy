#!/usr/bin/python
import cgi
import os
import sys
from abi import urltools
from abi import awrde

#DOC name: OpenGraph
#DOC title: Open a graph
#DOC desc: This command opens a graph. 
#DOC args: name* - name of the graph to be opened
#DOC args: close - a value of 0 does nothing, a value of 1 causes all existing windows to be closed
#DOC args: tile - a value of 'H' causes a horizontal tiling to be done, a value of 'V' causes a vertical tiling and a value of 'N' disables the tiling
#DOC web: http://localhost:8008/OpenGraph?name=S21;close=1;tile=H
#DOC wiki: OpenGraph S21

def main():
    urltools.html_header()
    name = urltools.get_parameter('name')
    close_all = urltools.get_parameter('close')
    tile = urltools.get_parameter('tile')

    if name:
    
        if (close_all):
            awrde.CloseWindows()
        awrde.OpenGraph(name)

        if (tile == 'H'):
            awrde.TileWindowsHorizontal()
        elif (tile == 'V'):
            awrde.TileWindowsVertical()
        else:
            awrde.CascadeWindows()

    else:
        urltools.html_error('You must specify the name parameter with the OpenEM command')
        urltools.html_error('use OpenGraph?name=<graph_name>')

    urltools.html_footer()


if __name__ == "__main__":
    main()

