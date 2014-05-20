#!/usr/bin/python
import cgi
import os
import sys
from   cgi.urltools import url, convert_command_to_URL
from   urllib.parse import parse_qs, urlsplit,SplitResult,urlunsplit



def test_init_simpleURL():
    url1 = 'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'

    myurl = url(url1)
    assert(myurl.get_server(),'dl.dropboxusercontent.com')
    assert(myurl.get_fullpath(),'/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    assert(myurl.get_directory(),'/u/3862332/ghs_hybrid')
    assert(myurl.get_filename(),'3dB_Coupler_start.emp')
    assert(myurl.get_query_param('name'),'')

def test_init_complexURL():
    url2 = 'http://localhost:8008/OpenProject?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'
     
    myurl = url(url2)
    values = myurl.get_query_param('name')
    assert(values[0],'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    assert(myurl.get_server(),'localhost:8008')
    assert(myurl.get_fullpath(),'/OpenProject')
    suburl = url(values[0])
    assert(suburl.get_server(),'dl.dropboxusercontent.com')
    assert(suburl.get_fullpath(),'/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    assert(suburl.get_filename(),'3dB_Coupler_start.emp')
    assert(suburl.get_query_param('name'),'')

def test_replace_filename():
    myurl = url('http://localhost/OpenProject')
    newurl = myurl.replace_filename('cgi/openproject.py')
    assert(newurl,'http://localhost/cgi/openproject.py')

    myurl = url('http://localhost/dir1/dir2/OpenProject')
    newurl = myurl.replace_filename('openproject.py')
    assert(newurl,'http://localhost/dir1/dir2/openproject.py')

    myurl = url('http://localhost/OpenProject?name=myproject.emp')
    newurl = myurl.replace_filename('cgi/openproject.py')
    assert(newurl,'http://localhost/cgi/openproject.py?name=myproject.emp')

def test_convert_command_to_URL():
    assert(convert_command_to_URL('http://localhost/OpenProject'), \
                                  'http://localhost/cgi/OpenProject.py')
    assert(convert_command_to_URL('http://localhost/OpenProject?name=3dB.emp'), \
                                  'http://localhost/cgi/OpenProject.py?name=3dB.emp')
    assert(convert_command_to_URL( \
    'http://localhost:8008/OpenProject?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'), \
    'http://localhost:8008/cgi/OpenProject.py?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')