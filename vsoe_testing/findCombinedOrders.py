#!/usr/bin/env python

import shutil
import sys
import utilities

print ""

### Program Start
scriptName = sys.argv[0]
inputFileName = sys.argv[1]

print "Finding orders with both term and perpetual products"
print "   reading expenses from ",inputFileName
print ""

inputFile = open(inputFileName)

totalLines = 0
currentInvoice = ""
invoiceList = {}
itemList = list()
containsTerm = False
containsPerp = False

line = inputFile.readline() # eat header line
for line in inputFile.readlines():
	totalLines += 1
	line = utilities.striplf(line)


	fieldList = utilities.parseExcelCsv(line)
	
	try:
		(d1,invnum,date,corpid,custid,name,country,territory,item,class_code,desc,
	acct,pricelevel,qty,price1,md1,ep1,void) = fieldList
	except ValueError:
		print "failed to read file on line: ", totalLines+1
		print ""
		print "bad: ", line
		exit(1)

	if (invnum != currentInvoice):
		## this is a new invoice
		if (currentInvoice != ""):
			## store away list of parts if they contain both term and perp
			if (containsTerm and containsPerp):
				invoiceList[currentInvoice] = itemList
		## initialize for new invoice
		itemList = list()
		currentInvoice = invnum
		containsPerp = False
		containsTerm = False

	if (len(item) == 11):
		type =  item[8]
		if (type == 'T' or item == 'UPG-TERM'):
			containsTerm = True
		if (type == 'P' or item == 'UPG-PROD'):
			containsPerp = True
	else:
		type = False
	
	if (item == 'UPG-TERM'):
		containsTerm = True
		type = 'T'
	if (item == 'UPG-PROD'):
		containsPerp = True
		type = 'P'
			
	## only save item if it's term or perpetual, ignore maint and other stuff
	if (type == 'T' or type == 'P'):
		itemList.append(item)

## on last invoice need to save if needed	
if (containsTerm and containsPerp):
		invoiceList[currentInvoice] = itemList
		
inputFile.close()

for key in invoiceList.keys():
	print "Invoice Number = ", key, "contains items"
	for item in invoiceList[key]:
		print "    ", item


