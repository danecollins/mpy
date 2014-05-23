#!/usr/bin/python
import cgi
import os
import sys
from   urllib.parse import parse_qs, urlsplit,SplitResult,urlunsplit

     

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
    command_list = ['OpenProject','OpenSchematic','OpenGraph','Simulate','RunScript']
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
