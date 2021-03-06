
import shutil
import sys
import utilities
import readmap
import math


### Fixed NI fields
Upl = 'O'
Co = '71'
Sub = '171'
PL = '00'
Proj = '000000'

def getAcctNumber(awr2ni,x):
    # Account string has the format of "0001100??, /Y"
    x = x.replace('-','')
    x = x.replace('"','')
    x = x.replace('?','')
    dept = x[0:3]
    acct = x[3:7]
    key = dept + acct
    if (not awr2ni.has_key(key)):
        ni_acct = '0'
        ni_dept = '0'
    else:
        (ni_dept,ni_acct) = awr2ni[key]


    return([dept,acct,ni_dept,ni_acct])

def readInputFile():
    consolidated = False
    awr2ni = readmap.readAccountMap(consolidated)
    print "Map file read.  ", len(awr2ni), "entries found"

    file=open(sys.argv[1])
    of = open('output.csv','w')
    ## Initialize Counters
    linecount=0
    S8=0
    S9=0
    total=0
    inCompany=0
    companyNumber=0


    for line in file.readlines():
        linecount += 1
        line = utilities.striplf(line)
        
        # if it is a blank line pass it through
        if (line == ''):
            print >> of, line
            continue
        
        # parse the line
        items = utilities.parseExcelTxtFileLine(line)
        
        # if there are not 3 items it's not an account line
        if (len(items) <> 3):
            print >> of, line
            continue
        
        # So we have an account line
        desc       = items[0]
        acctString = items[1]
        balance    = items[2]
        # if we have a total line, we're at the end of a company

        if (desc[0:5] == 'Total'):
            # for first total line print adjustment lines otherwise skip
            if (inCompany):
                inCompany = 0

            continue
            
        # if this is the line with 3 items
        if (inCompany == 0):
            inCompany = 1
            companyNumber = companyNumber+1
            S8    = 0
            total = 0
            
        # map the account line and print it out

        ### hacks here to handle inconsistency of format of 'Accum other comprehensive income' line
        if (desc[0:11]=='Accum other'):
            dept = '000'
            acct = 'na'
            ni_cc = '0'
            ni_acct = '39091'
        elif (desc[0:17]=='Retained Earnings'):
            dept = '000'
            acct = '3900'
            ni_cc = '0'
            ni_acct = '35001'
        else:
            (dept,acct,ni_cc,ni_acct) = getAcctNumber(awr2ni,acctString)

        # convert balance from string to number
        balance = utilities.excelToNumber(balance)

        #if (ni_acct[0] <> '0' and ni_acct <> '99999' and ni_acct <> '99998'):
        if (ni_acct[0] == '0'):
            print 'Unmapped account #', dept, acct,',', balance
            print line
        else:
            # debug line print Upl,Co,ni_cc,ni_acct,Sub,PL,Proj,balance,0,desc
            ### Oracle can't handle '0' in the data so print the missing D/C as empty
            if (ni_acct == '95005'):
                # need to allocate out the accounts
                if (balance[0] == '-'):
                    amt = -1 * float(balance)
                    print >> of, 'O,%s,%s,%s,%s,%s,%s,,%s,%s' % (Co,ni_cc,'61096',Sub,PL,Proj,float(amt)*.6,'Other benefits')
                    print >> of, 'O,%s,%s,%s,%s,%s,%s,,%s,%s' % (Co,ni_cc,'67095',Sub,PL,Proj,float(amt)*.4,'Misc building')
                else:
                    amt = float(balance)
                    print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,,%s' % (Co,ni_cc,'61096',Sub,PL,Proj,float(amt)*.6,'Other benefits')
                    print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,,%s' % (Co,ni_cc,'67095',Sub,PL,Proj,float(amt)*.4,'Misc building')
            else:
                if (balance[0] == '-'):
                    print >> of, 'O,%s,%s,%s,%s,%s,%s,,%s,%s' % (Co,ni_cc,ni_acct,Sub,PL,Proj,balance[1:],desc)
                else:
                    print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,,%s' % (Co,ni_cc,ni_acct,Sub,PL,Proj,balance,desc)

        ## update counters
        balance = float(balance)
        total += balance
            

    file.close()
    of.close()
    print '\nStatistics on processed file'
    print '   Number of lines: ', linecount
    print '   Sum of all output =', total
    print '   Number of companies processed = ', companyNumber
    print ''


def testReadInputFile():
    readInputFile()


if __name__ == "__main__":

    testReadInputFile()
