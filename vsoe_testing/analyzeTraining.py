#!/usr/bin/env python

import shutil
import sys
import utilities



### Program Start
scriptName = sys.argv[0]
inputFileName = sys.argv[1]

print "Program to analyze training orders"
print "   reading expenses from ",inputFileName
print ""
print "List of training items failing 15% test..."
print "---------------------------------------------------------------------------"

inputFile = open(inputFileName)
outputFileName = 'Failing_training.txt'

outputFile = open(outputFileName,'w')

totalLines = 0
maintLines = 0
maintProducts = 0
nonMaintLines = 0
withMarkdown = 0
failed=0
lastInvoice = ''

parts = {}

line = inputFile.readline() # eat header line
for line in inputFile.readlines():
	totalLines += 1
	line = utilities.striplf(line)
	fieldList = utilities.parseExcelCsv(line)
	(d1,invnum,date,corpid,custid,name,country,territory,item,class_code,desc,
	acct,pricelevel,qty,price,md,ep,void) = fieldList
	
	qty = int(qty) # convert to integer
	
	#only process maintenance orders
	if ( len(invnum) > 5 and (invnum[4] == 'S' or invnum[4] == 's') and void == 'Normal' and 
		not (item=='ADMIN FEE' or item=='BACK-MAIN' or item=='HWK-200' or item=='TAX')):
		if (parts.has_key(item)):
			parts[item] += qty
		else:
			parts[item] = qty
			
		maintLines += 1
		maintProducts += qty
		if (float(md) > 0.01):
			withMarkdown += qty
			percentage = round(float(md) / float(price)*100,1)
			if (percentage >= 15):
				lineNumber = int(totalLines)+1
				print 'item %4s failed with %5.1f%%, qty=%2d, item=%11s, invoice=%s' % (lineNumber,percentage,qty, item,invnum)
				failed += qty
				if (lastInvoice <> invnum):
					print >> outputFile, "====== %s - %s ======" % (date,name)
					print >> outputFile, "  * invoice number = %s" % (invnum)
					lastInvoice = invnum
				
				print >> outputFile, "  * %s (%d seat(s))" % (item,qty)
				print >> outputFile, "  * list price = %s, discount = %s (%5.1f%%)" % (price,md,percentage)
				print >> outputFile, "  * **enter explanation here**\n"
				
			
			if (percentage > 10 and percentage < 15):
				print 'item %4s passed with %5.1f%%, qty=%2d, item=%11s, invoice=%s' % (lineNumber,percentage,qty,item,invnum)
				
	else:
		nonMaintLines += 1    	
 
inputFile.close()
outputFile.close()

print "\nOverall Statistics"
print "---------------------------------------------------------------------------"
print "Number of Item Lines      = ",totalLines
print "Number of Training Lines     = ",maintLines
print "Number of Training Products  = ",maintProducts," (maintenance lines times quantity)"
print "Training Products with Discount   = ",withMarkdown, " (product quantity having a discount)"
print "Training Products with >15% Discount = ",failed, " (products that have big discounts)"
if (float(maintProducts)>0.01):
	print "Percentage of line items that failed 15% discount test = ", round(float(failed)/float(maintProducts)*100.0,2)

print "\nSample Size Statistics"
print "---------------------------------------------------------------------------"
for key in parts.keys():
	print key," = ",parts[key]

