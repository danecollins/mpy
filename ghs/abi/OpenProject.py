#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
import abi.urltools
import abi.awrde


def main():
    abi.urltools.html_header()
    project_name = abi.urltools.get_parameter("name")
    sim_after = abi.urltools.get_parameter("simulate")
    if project_name:
        local_name = abi.urltools.get_project(project_name)
        abi.urltools.html_message("Opening project: %s" % local_name)
        abi.awrde.OpenProject(local_name)
        if (sim_after):
            abi.awrde.Simulate()
    else:
        abi.urltools.html_error("Link has no project name.")

if __name__ == "__main__":
    main()

