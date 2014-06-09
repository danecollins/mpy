#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi import urltools
from abi import awrde


def main():
    urltools.html_header()
    project_name = urltools.get_parameter("name")
    sim_after = urltools.get_parameter("simulate")
    if project_name:
        local_name = urltools.get_project(project_name)
        urltools.html_message("Opening project: %s" % local_name)
        awrde.OpenProject(local_name)
        if (sim_after):
            awrde.Simulate()
    else:
        urltools.html_error("Link has no project name.")

    urltools.html_footer()

if __name__ == "__main__":
    main()

