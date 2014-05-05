#!/usr/local/bin/python
import cgi

def main():
	print "Content-type: text/html\n"
	form = cgi.FieldStorage()
	if form.has_key("firstname") and form["firstname"].value != "":
		print "<h1>Hello", form["firstname"].value,"</h1>"
	else:
		print "<h1> Error! Please enter first name.</h1>"

main()
