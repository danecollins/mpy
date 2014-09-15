#!/usr/bin/python
import cgi
import os
import sys
from   urllib.parse import parse_qs, urlsplit,SplitResult,urlunsplit
from   urllib.error import URLError
import urllib.request

class url(object):
    def __init__(self,path):
        self.parsed = urlsplit(path)
        
    def get_server(self):
        """ Returns the host:port part of the url """
        return(self.parsed.netloc)
    
    def get_fullpath(self):
        """ Returns the full path of the url with server and args removed """
        return(self.parsed.path)
        
    def get_filename(self):
        """ Returns the end file name of the path only """
        fullpath = self.parsed.path
        return(os.path.basename(fullpath))
        
    def get_directory(self):
        """ Returns the full path minus the file name """
        fullpath = self.parsed.path
        # there is an inconsistency in os.path in that the path does not contain
        # training / unless the path is / which makes it unpredictible so we'll 
        # have the root be empty string instead
        dir = os.path.dirname(fullpath)
        if (dir == '/'):
            dir = ''
        return(dir)
        
    def get_query_param(self,param_name):
        """ Returns the value of the named parameter or empty string if it's missing """
        params = self.parsed.query
        values = parse_qs(params)
        if (param_name in values):
                return(values[param_name])
        else:
                return('')

    def replace_filename(self,newfilename):
        """ Returns a new URL with the filename replaced by newfilename """
        newfullpath = self.get_directory() + '/' + newfilename
        newurl = SplitResult(self.parsed[0],self.parsed[1],newfullpath,self.parsed[3],self.parsed[4])
        return urlunsplit(newurl)

def get_command_list():
    return([
        'LoadProject',
        'LoadSchematic',
        'OpenSchematic',
        'LoadSystemDiagram',
        'OpenSystemDiagram',
        'Simulate',
        'RunScript',
        'OpenUserFolder',
        'TileVertical',
        'TileHorizontal',
        'CloseWindows',
        'OpenEM',
        'OpenGraph',
        'OpenProject'
                    ])

def convert_command_to_URL(path):
    """ Checks whether url is a command and fixes it """
    # Commands are somewhat in the form of URL's in that they need to be valid enough
    # that the command gets to the AWAC but past that we can change the rest into anything
    # we want.
    #
    # The current command syntax is:
    #     http://localhost:port/COMMAND?arguments
    #
    # which we process in the following way:
    #     1) command is converted to abi/COMMAND.py

    # Define the commands we'll fix up
    command_list = get_command_list()
    # split up the url
    command_url = url(path)

    # we need to lowercase the command so we don't run into case issues
    command = command_url.get_filename()
    if (command in command_list):
        newcommand = "abi/" + command + '.py'

        # add args back in
        newurl = command_url.replace_filename(newcommand)
        return(newurl)
    else:
        # not a command, do nothing
        return(False)

def get_parameter(name):

    # form being executed from web server
    form = cgi.FieldStorage()
    if (name in form and form[name].value != ""):
        url = form[name].value

        # BUG/FEATURE
        # the CGI mechanism collapses multiple / to a single / (which would normally be on)
        # but it makes http:// into http:/ which is not legal.  This adds the / back in.
        if (url.startswith('https:') and not url.startswith('https://')):
            url = url.replace('https:/','https://')
        if (url.startswith('http:') and not url.startswith('http://')):
            url = url.replace('http:/','http://')   
        return(url)
    else:
        return False


def get_file(file_url, filetype):
    "downloads a file to a temp directory and returns the name. can be emp, sch or sys"
    file_extension = '.' + filetype
    if (file_url.startswith('http')):
        # web file request, we'll get the project
        filename=False
        try:
            (filename,headers) = urllib.request.urlretrieve(file_url)
        except URLError as e:
            print(e.reason)
            
        if not filename:
            return False
            
        # filename is the name of a temporary file.     
        # on windows, the .emp extension may not be preserved
        if not filename.endswith(file_extension):
            os.rename(filename,filename+file_extension)
            filename = filename + file_extension
            
        # the .vin must have the same name
        ## just not sure we want to do this anymore
        #vinfilename = filename.replace('.emp','.vin')
        #vinurl = project_url.replace('.emp','.vin')
        #try:
        #    (vname,vheaders) = urllib.request.urlretrieve(vinurl,vinfilename)
        #except URLError as e:
        #    print(e.reason)
        return(filename)
    else:
        # local file request
        return(file_url)

### These functions manage consistent formatting for the html log window
### this output is checked for in tests so any edits here will require
### changing the tests

def html_header():
    print("Content-type: text/html\n")
    print("<head><title>In ABI Command</title></head>")
    print("<body>")
    print("<h1>Command debug log</h1>")

def html_footer():
    print("</body>")

def html_message(message):
    print("<p>%s</p>" % message)

def html_error(message):
    print("<p><font color=red>%s</font></p>" % message)

def html_test(message):
    print("EMULATING %s" % message)

# def html_test(message):
    
#     #dt = datetime.datetime.now()
#     #fp.write(dt.strftime('%y-%m-%d %H:%M:%S '))
#     print('<p>TESTMODE: %s</p>' % message)

