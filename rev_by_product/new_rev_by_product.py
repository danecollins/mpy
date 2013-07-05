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
ano = 0
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

	if (len(item)>8 and item[8] == 'M' and void == 'Normal'):
		print "Maintenance = %s, %s" % (item,territory)
		mwo = mwo + lineType*float(ep1)
	else:
		print "Other product = %s,  %7.0f" % (item,lineType*float(ep1))
		oth = oth + lineType*float(ep1)
	

inputFile.close()


