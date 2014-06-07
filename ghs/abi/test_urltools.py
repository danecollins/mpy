#!/usr/bin/python
import cgi
import os
import sys
import hashlib
from   io import StringIO
from   abi.urltools import url, convert_command_to_URL, get_parameter, get_project
from   abi.urltools import html_header,html_footer,html_message,html_error
from   abi.awrde import set_test_mode
from   urllib.parse import parse_qs, urlsplit,SplitResult,urlunsplit
from   unittest.mock import patch


def test_init_simpleURL():
    url1 = 'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'

    myurl = url(url1)
    assert(myurl.get_server() == 'dl.dropboxusercontent.com')
    assert(myurl.get_fullpath() == '/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    assert(myurl.get_directory() == '/u/3862332/ghs_hybrid')
    assert(myurl.get_filename() == '3dB_Coupler_start.emp')
    assert(myurl.get_query_param('name') == '')

def test_init_complexURL():
    url2 = 'http://localhost:8008/OpenProject?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp'
     
    myurl = url(url2)
    values = myurl.get_query_param('name')
    assert(values[0] == 'https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    assert(myurl.get_server() == 'localhost:8008')
    assert(myurl.get_fullpath() == '/OpenProject')
    suburl = url(values[0])
    assert(suburl.get_server() == 'dl.dropboxusercontent.com')
    assert(suburl.get_fullpath() == '/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')
    assert(suburl.get_filename() == '3dB_Coupler_start.emp')
    assert(suburl.get_query_param('name') == '')

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
    assert(convert_command_to_URL('http://localhost/OpenProject') ==  \
                                  'http://localhost/abi/OpenProject.py')
    assert(convert_command_to_URL('http://localhost/OpenProject?name=3dB.emp') ==  \
                                  'http://localhost/abi/OpenProject.py?name=3dB.emp')
    assert(convert_command_to_URL( \
    'http://localhost:8008/OpenProject?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp') ==  \
    'http://localhost:8008/abi/OpenProject.py?name=https://dl.dropboxusercontent.com/u/3862332/ghs_hybrid/3dB_Coupler_start.emp')

def test_get_parameter_simple():
    # simple arguments
    os.environ['QUERY_STRING'] = 'arg1=foo&arg2=bar'
    assert(get_parameter('arg1') == 'foo')
    assert(get_parameter('arg2') == 'bar')
    # missing parameter gets returned as empty string
    assert(get_parameter('arg3'),'')

def test_get_parameter_urlfix():
    # multiple / fixing
    os.environ['QUERY_STRING'] = 'name=http://localhost:8008/OpenProject'
    assert(get_parameter('name') == 'http://localhost:8008/OpenProject')
    os.environ['QUERY_STRING'] = 'name=https://localhost:8008/OpenProject'
    assert(get_parameter('name') == 'https://localhost:8008/OpenProject')


def test_get_project():
    # this is the link to AM.emp in dropbox
    os.environ['QUERY_STRING'] ='name=https://dl.dropboxusercontent.com/u/3862332/ghs_testing/AM.emp'
    url = get_parameter('name')
    print(url)
    filename = get_project(url)

    # make sure we got the file
    assert(filename)

    md = hashlib.sha1()
    size = 0

    with open(filename,'rb') as fp:
        bytes = fp.read()

    for byte in bytes:
        size = size + 1
        md.update(str(byte).encode('utf-8'))
    
    hexval = md.hexdigest()

    emp_size = 11572
    emp_digest = 'c5829547ad87d5acf80994c8cafe7f4c4e6e6198'

    assert(size == emp_size)
    assert(hexval == emp_digest)

    filename = filename.replace('.emp','.vin')
    
    # make sure file was downloaded
    assert(filename)

    with open(filename,'rb') as fp:
        bytes = fp.read()

    size=0
    for byte in bytes:
        size = size + 1
        md.update(str(byte).encode('utf-8'))
    
    hexval = md.hexdigest()

    vin_size = 1116
    vin_digest = 'ff3a5e92bbde3f46f4bfaf457b07ae5105361bd3'

    assert(size == vin_size)
    assert(hexval == vin_digest)


### test the html section of functions
###
### for this we will be re-directing stdout to capture the output
set_test_mode(True)

def test_html_header():
    expected = \
"""Content-type: text/html

<head><title>In Simulate.py</title></head>
<body>
<h1>Command debug log</h1>
""".strip()
    with patch('sys.stdout',new=StringIO()) as fake_out:
        html_header()
        value = fake_out.getvalue().strip()

    #print(value)
    assert(value == expected)


def test_html_footer():
    # output is .strip() so don't add newline
    expected = '</body>'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        html_footer()
        value = fake_out.getvalue().strip()

    assert(value == expected)

def test_html_message():
    
    # output is .strip() so don't add newline
    expected = '<p>hello</p>'
    with patch('sys.stdout',new=StringIO()) as fake_out:
        html_message("hello")
        value = fake_out.getvalue().strip()

    assert(value == expected)

def test_html_error():
    # output is .strip() so don't add newline
    expected = '<p><font color=red>hello</font></p>'

    with patch('sys.stdout',new=StringIO()) as fake_out:
        html_error("hello")
        value = fake_out.getvalue().strip()

    print(value)
    assert(value == expected)

