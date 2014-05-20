#!/usr/bin/python
import cgi
import os
import sys
from   urlparse import parse_qs, urlsplit,SplitResult,urlunsplit

                

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


        
if __name__ == '__main__':
    import unittest
    class URL_Tests(unittest.TestCase):
        """ Test class for URL utility functions """

        def test1(self):
            """ Tests on simple URL """

            url1 = 'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'

            myurl = url(url1)
            self.assertEqual(myurl.get_server(),'dl.dropboxusercontent.com')
            self.assertEqual(myurl.get_fullpath(),'/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
            self.assertEqual(myurl.get_directory(),'/u/3862332/ghs_hybrid')
            self.assertEqual(myurl.get_filename(),'3dB_Coupler_start.emp')
            self.assertEqual(myurl.get_query_param('name'),'')

        def test2(self):
            """ Tests on more complex URL """
            url2 = 'http://localhost:8008/OpenProject?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'
             
            myurl = url(url2)
            values = myurl.get_query_param('name')
            self.assertEqual(values[0],'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
            self.assertEqual(myurl.get_server(),'localhost:8008')
            self.assertEqual(myurl.get_fullpath(),'/OpenProject')
            suburl = url(values[0])
            self.assertEqual(suburl.get_server(),'dl.dropboxusercontent.com')
            self.assertEqual(suburl.get_fullpath(),'/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
            self.assertEqual(suburl.get_filename(),'3dB_Coupler_start.emp')
            self.assertEqual(suburl.get_query_param('name'),'')

        def test3(self):
            """ Test replace_filename """
            myurl = url('http://localhost/OpenProject')
            newurl = myurl.replace_filename('cgi/openproject.py')
            self.assertEqual(newurl,'http://localhost/cgi/openproject.py')

            myurl = url('http://localhost/dir1/dir2/OpenProject')
            newurl = myurl.replace_filename('openproject.py')
            self.assertEqual(newurl,'http://localhost/dir1/dir2/openproject.py')

            myurl = url('http://localhost/OpenProject?name=myproject.emp')
            newurl = myurl.replace_filename('cgi/openproject.py')
            self.assertEqual(newurl,'http://localhost/cgi/openproject.py?name=myproject.emp')

    unittest.main()