#!/usr/bin/python
import cgi
import os
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.error import URLError
from abi import urltools
from abi import awrde

#DOC name: OpenProject
#DOC title: Open a project file
#DOC desc: This command loads a new project. If a project is already loaded it will be closed. The name of the project is the URL to the project. Currently Dropbox is used to store projects due to its convenience. The .vin file is also used
#DIC args: name - URL to the project to be downloaded and opened
#DOC args: simulate - set to 1 will cause the project to be simulated after it is opened
#DOC web: http://localhost:8008/OpenProject?name=full_url_to_project.emp
#DOC wiki: OpenProject full_url_to_project.emp

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

