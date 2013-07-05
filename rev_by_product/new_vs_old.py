#!/usr/bin/env python

import shutil
import sys
import utilities



### Program Start
scriptName = sys.argv[0]
inputFileName = sys.argv[1]

print "Program to analyze revenue"


inputFile = open(inputFileName)


old = 0
new = 0
maint = 0
xem = 0
ana = 0
fil = 0
oem = 0
oth = 0
totalLines=0


parts = {}

line = inputFile.readline() # eat header line
for line in inputFile.readlines():
	totalLines += 1
	line = utilities.striplf(line)
	fieldList = utilities.parseExcelCsv(line)
	# if parsing crashes uncomment this
	#print line
	(d1,invnum,date,corpid,custid,name,country,territory,item,class_code,desc,
	acct,pricelevel,qty,price1,md1,ep1,void) = fieldList
	price = float( str(price1).replace(',','',2))
	md = float( str(md1).replace(',','',2))
	ep = float( str(ep1).replace(',','',2))

	
	qty = int(qty) # convert to integer

### returns need to be negative
	if (d1 == "Invoice"):
		lineType = 1
	elif (d1 == "Return"):
		lineType = -1
	else:
		print "Unknown type %s" % d1

	if (len(item)>8 and item[8] == 'M' and void == 'Normal'):
		#print "Maintenance = %s, %s" % (item,territory)
		maint = maint + lineType*float(ep1)
	else:
		if ((item[0:3] == 'MWO' or item[0:3] == 'APL' or item[0:3] == 'UPG' or item[0:3] == 'VSS' or item[0:3] == 'ANO') and void == 'Normal'):
			#print "MWO product = %s" % item
			old = old + lineType*float(ep1)
		elif ((item[0:3] == 'ACE' or item[0:3]=='TSW' or item[0:3]=='MOD' or item[0:3]=='NXG' or item[0:3]=='PTD' or item[0:3]=='WIQ' or item[0:3]=='ACS') and void == 'Normal'):
			print "new product = %s" % item
			new =new + lineType*float(ep1)
		elif ((item[0:3] == 'XEM') and void == 'Normal'):
			#print "new product = %s" % item
			xem =xem + lineType*float(ep1)
		elif ((item[0:3] == 'ANA' ) and void == 'Normal'):
			#print "new product = %s" % item
			ana =ana + lineType*float(ep1)
		elif ((item[0:3]=='FIL') and void == 'Normal'):
			print "new product = %s" % item
			fil =fil + lineType*float(ep1)
		elif (item[0:3] == 'TAX' or item[0:3] == 'VAT'):
			# ignore tax entries
			tax = 1
		else:
			#print "Other product = %s,  %7.0f" % (item,lineType*float(ep1))
			oth = oth + lineType*float(ep1)
	

inputFile.close()

print "OLD total = %7.0f" % old
print "NEW total = %7.0f" % new
print "XEM total = %7.0f" % xem
print "ANA total = %7.0f" % ana
print "FIL total = %7.0f" % fil
print "MNT total = %7.0f" % maint
