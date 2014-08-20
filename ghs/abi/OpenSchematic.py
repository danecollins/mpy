#!/usr/bin/python
import cgi
import os
import sys
from abi import urltools
from abi import awrde

#DOC name: OpenSchematic
#DOC title: Open a schematic
#DOC desc: This command loads a new project. If a project is already loaded it will be closed. The name of the project is the URL to the project. Currently Dropbox is used to store projects due to its convenience. The .vin file is also used
#DOC args: name* - name of the schematic to be opened
#DOC args: close - a value of 0 does nothing, a value of 1 causes all existing windows to be closed
#DOC args: tile - a value of 'H' causes a horizontal tiling to be done, a value of 'V' causes a vertical tiling and a value of 'N' disables the tiling
#DOC web: http://localhost:8008/OpenSchematic?name=ResonatorSchematic;close=1;tile=H
#DOC wiki: OpenSchematic ResonatorSchematic

def main():
    urltools.html_header()
    schematic_name = urltools.get_parameter('name')
    close_all = urltools.get_parameter('close')
    tile = urltools.get_parameter('tile')

    if schematic_name:
    
        if (close_all):
            awrde.CloseWindows()
        awrde.OpenSchematic(schematic_name)

        if (tile == 'H'):
            awrde.TileWindowsHorizontal()
        elif (tile == 'V'):
            awrde.TileWindowsVertical()
        else:
            awrde.CascadeWindows()

    else:
        urltools.html_error('You must specify the name parameter with the OpenSchematic command')
        urltools.html_error('use OpenSchematic?name=<schematic_name>')

    urltools.html_footer()


if __name__ == "__main__":
    main()

