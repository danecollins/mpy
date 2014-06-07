#!/usr/bin/python
import cgi
import os
import sys
import urltools
import awrde


def main():
    urltools.html_header()
    schematic_name = urltools.get_parameter('name')
    close_all = urltools.get_parameter('close')
    tile = urltools.get_parameter('tile')

    if schematic_name:
    
        if (close_all):
            awrde.CloseAllWindows()
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

