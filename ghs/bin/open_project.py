#!/usr/bin/python

import os
import sys

project_name = sys.argv[1]

if os.name == 'nt':
	import win32com.client
	awrde=win32com.client.Dispatch("MWOApp.MWOffice")
	awrde.Open(project_name)
else:
	file=open('gh_commands.log','a')
	print >> file, 'MWO.open(%s)' % (project_name)
	file.close()

	
