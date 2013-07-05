#!/usr/bin/env python

import shutil
import sys
import utilities



### Program Start
scriptName = sys.argv[0]
inputFileName = sys.argv[1]

print "Program to analyze revenue"


inputFile = open(inputFileName)


mwo = 0
vss = 0
xem = 0
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

	if ((item[0:3] == 'MWO' or item[0:3] == 'ANO' or item[0:3] == 'APL' or item[0:3] == 'UPG') and void == 'Normal'):
		#print "MWO product = %s" % item
		mwo = mwo + lineType*float(ep1)
	elif ((item[0:3] == 'VSS') and void == 'Normal'):
		#print "VSS product = %s" % item
		vss = vss + lineType*float(ep1)
	elif ((item[0:3] == 'XEM' or item[0:3] == 'ANA') and void == 'Normal'):
		#print "XEM product = %s" % item
		xem = xem + lineType*float(ep1)
	elif ((item[0:3] == 'HSP' or item[0:3]=='TSW' or item[0:3]=='FIL' or item[0:3]=='MOD' or item[0:3]=='NXG') and void == 'Normal'):
		#print "OEM product = %s" % item
		oem = oem + lineType*float(ep1)
	elif (item[0:3] == 'TAX' or item[0:3] == 'VAT'):
		# ignore tax entries
		tax = 1
	else:
		print "Other product = %s,  %7.0f" % (item,lineType*float(ep1))
		oth = oth + lineType*float(ep1)
	
print "MWO total = %7.0f" % mwo
print "VSS total = %7.0f" % vss
print "EM  total = %7.0f" % xem
print "OEM total = %7.0f" % oem
print "oth total = %7.0f" % oth
print "total $   = %7.0f" % (mwo+vss+xem+oem+oth)
 
inputFile.close()


