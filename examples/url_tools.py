#!/usr/bin/python
import cgi
import os
import sys
import urllib
from urlparse import parse_qs, urlparse

def runtest(test,a,b):
    if not (a == b):
        print "Test Failure: " + str(test)
        print "    %s <> %s" % (a,b)
        print 
        

class url(object):
  def __init__(self,path):
    self.parsed = urlparse(path)
    
  def get_server(self):
    return(self.parsed.netloc)
  
  def get_fullpath(self):
    return(self.parsed.path)
    
  def get_filename(self):
    fullpath = self.parsed.path
    return(os.path.basename(fullpath))
    
  def get_directory(self):
    fullpath = self.parsed.path
    return(os.path.dirname(fullpath))
    
  def get_query_param(self,param_name):
    params = self.parsed.query
    values = parse_qs(params)
    if (param_name in values):
        return(values[param_name])
    else:
        return('')
    
    

if __name__ == '__main__':
    
    url1 = 'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'
    
    print "Tests on simple URL"
    myurl = url(url1)
    runtest(1,myurl.get_server(),'dl.dropboxusercontent.com')
    runtest(2,myurl.get_fullpath(),'/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    runtest(3,myurl.get_filename(),'3dB_Coupler_start.emp')
    runtest(4,myurl.get_query_param('name'),'')
    
    url2 = 'http://localhost:8008/OpenProject?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'
    print "Tests on more complex URL"
    myurl = url(url2)
    values = myurl.get_query_param('name')
    runtest(5,values[0],'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    runtest(6,myurl.get_server(),'localhost:8008')
    runtest(7,myurl.get_fullpath(),'/OpenProject')
    suburl = url(values[0])
    runtest(8,suburl.get_server(),'dl.dropboxusercontent.com')
    runtest(9,suburl.get_fullpath(),'/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    runtest(10,suburl.get_filename(),'3dB_Coupler_start.emp')
    runtest(11,suburl.get_query_param('name'),'')