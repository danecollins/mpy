#!/usr/bin/env python
 
import cgi, os, time, sys, shutil, subprocess
import time

def get_networks():
	output = subprocess.check_output(["iwlist", "wlan0", "scanning"])

	secured = []
	unsecured = []
	ssid = ''

	for line in output.split('\n'):
		line = line.rstrip('\n\r')

		if (line.find('Cell') <> -1 and line.find('Address') <> -1):
			# new access point
			if (ssid <> ''):
				# remove the quotes from the name if they exist
				ssid = ssid.replace('"','')
				if (encrypted == 1):
					secured.append(ssid)
				else:
					unsecured.append(ssid)
			ssid = ''
			encrypted = -1
		if (line.find('ESSID:') <> -1):
			(tag,ssid) = line.split(':')

		if (line.find('Encryption key') <> -1):
			(tag,encryption) = line.split(':')
			if (encryption == 'on'):
				encrypted = 1
			else:
				encrypted = 0

	## now store last one
	if (ssid <> ''):
		# remove the quotes from the name if they exist
		ssid = ssid.replace('"','')
		if (encrypted == 1):
			secured.append(ssid)
		else:
			unsecured.append(ssid)

	return([secured,unsecured])

def connect_to_network(network_name,password):
	shutil.copyfile('/etc/network/interfaces','/tmp/interfaces.bak')
	fp = open('./sedfile','w')
	print >> fp, 's/wpa-ssid.*/wpa-ssid "' + network_name + '"/'
	print >> fp, 's/wpa-psk.*/wpa-psk "' + password + '"/'
	fp.close()
	os.system('sed -f sedfile < /tmp/interfaces.bak > /etc/network/interfaces')
	os.system('restart_wlan0')
	os.system('cd /home/ubuntu/bbserv;wlan_setup.py')

form = cgi.FieldStorage()
 
net = form.getvalue('network')
passwd = form.getvalue('password')

(secured,unsecured) = get_networks()


### basic error checking
if ((net in secured) and (passwd is None)):
	errormsg = "You are connecting to a secured network and must specify a password."
	nextpage = "../index.html"
elif (net is None):
	errormsg = "You must select one of the networks."
	nextpage = "../index.html"
elif (net not in secured) and (net not in unsecured):
	errormsg = "Could not find net in secured or unsecured network lists (%s) (%s)" % (secured, unsecured)
	nextpage = "../index.html"
else:
	errormsg = False
	nextpage = "../index.html"

connect_to_network(net,passwd)


print """<html>
<head>
<title>GardenValet Network Setup</title>
</head>

<body>
 <script language="javascript" type="text/javascript">
     <!--
     window.setTimeout('window.location="%s"; ',3000);
     // -->
 </script>
<p>
<h1>GardenValet Network Setup</h1>
<p>
""" % (nextpage)


if (errormsg):
	print '<font color="red">%s</font>' % errormsg
else:
	print "You will be connecting to network", net

print "<p>If you are not redirected automatically, follow the <a href='%s'>this link</a><p>" % (nextpage)


print "\n</body>\n</html>\n"


