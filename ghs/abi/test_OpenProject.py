import cgi
import os
import hashlib
import sys
from abi.OpenProject import get_parameter, get_project

def test_get_parameter_simple():
	# simple arguments
	os.environ['QUERY_STRING'] = 'arg1=foo&arg2=bar'
	assert(get_parameter('arg1'),'foo')
	assert(get_parameter('arg2'),'bar')
	# missing parameter gets returned as empty string
	assert(get_parameter('arg3'),'')

def test_get_parameter_urlfix():
	# multiple / fixing
	os.environ['QUERY_STRING'] = 'name=http://localhost:8008/OpenProject'
	assert(get_parameter('name'),'http://localhost:8008/OpenProject')
	os.environ['QUERY_STRING'] = 'name=https://localhost:8008/OpenProject'
	assert(get_parameter('name'),'https://localhost:8008/OpenProject')


def test_get_project():
	# this is the link to AM.emp in dropbox
	os.environ['QUERY_STRING'] ='name=https://dl.dropboxusercontent.com/u/3862332/ghs_testing/AM.emp'
	url = get_parameter('name')
	print(url)
	filename = get_project(url)
	md = hashlib.sha1()
	size = 0

	with open(filename,'rb') as fp:
		bytes = fp.read()

	for byte in bytes:
		size = size + 1
		md.update(str(byte).encode('utf-8'))
	
	hexval = md.hexdigest()

	return(size,hexval)
	(size,digest) = get_file_md5(filename)

	emp_size = 11572
	emp_digest = 'c5829547ad87d5acf80994c8cafe7f4c4e6e6198'

	assert(size,emp_size)
	assert(digest,emp_digest)

	filename = filename.replace('.emp','.vin')
	with open(filename,'rb') as fp:
		bytes = fp.read()

	for byte in bytes:
		size = size + 1
		md.update(str(byte).encode('utf-8'))
	
	hexval = md.hexdigest()

	return(size,hexval)
	(size,digest) = get_file_md5(filename)

	emp_size = 1116
	emp_digest = 'ff3a5e92bbde3f46f4bfaf457b07ae5105361bd3'
	
