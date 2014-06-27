Introduction
------------
The web interface into AWRDE is implemented through a local web server, the 
AWR web application controller or AWAC for short, running on the same machine
as AWRDE. This server (currently implemented in python) receives URL's and
uses them to execute CGI scripts (also currently implemented in python) which
connect to AWRDE through COM to execute actions.


Dependencies
------------
* Python 3.4+
** https://www.python.org/download/releases/2.7
* Python Win32 Extensions
** http://sourceforge.net/projects/pywin32/files/
* py.test

Local development setup
-----------------------
* PYTHONPATH must include the ghs directory

Configuration
-------------

### Confluence Configuration
* Admin->Custom HTML
** Define execcmd() based on confluence/custom_html.txt
* Admin->User Macros
** Add macro for awrcommand based on confluence/mwocmd.txt


Deploy
------
A script is provided to create a deployable version of the system

### On Linux
1. cd to the ghs directory
2. bin/copyto.sh <directory>

### On Windows
1. cd to ghs directory
2. bin\copyto.bat <directory>

where <directory> is an existing destination directory





