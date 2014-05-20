#!/usr/bin/env python
 
import cgi


print("""Content-type: text/html
<html>
<head>
<title>Test URL Encoding</title>
</head>
<body>""")
  
form = cgi.FieldStorage()
 
val1 = form.getvalue('one')
val2 = form.getvalue('two')
 
print("""
the arguments passed in were
<ul>
<li>%s</li>
<li>%s</li>
</ul>
</body></html>""" % (val1, val2) )

