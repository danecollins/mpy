
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

def getAcctNumber(map,x):
    x = x.replace('-','')
    x = x.replace('"','')
    x = x.replace('?','')
    dept = x[0:3]
    acct = x[3:7]
    key = dept + acct
    if (not map.has_key(key)):
        ni_acct = '0000'
        ni_dept = '0000'
    else:
        (ni_dept,ni_acct) = map[key]
        
    
    return([dept,acct,ni_dept,ni_acct])
    
def readInputFile():
    USConsolidated = True
    map = readmap.readAccountMap(USConsolidated)
    print "Map file read.  ", len(map), "entries found"
    
    file=open(sys.argv[1])
    of = open('output.csv','w')
    ## Initialize Counters
    linecount=0
    skipNextLines=0
    S8=0
    S9=0
    assets=0
    liabilities=0
    expenses=0
    total=0
    xx=0
    
    ### because of possible issues with newline types, test line count
    ### before processing
    allLines = file.readlines()
    print sys.argv[1]," contains ",len(allLines)," lines"
    for line in allLines:
        linecount += 1

        ### line contains desc, acct string, balance
        ### second argument is the delimiter (comma or tab)
        items = utilities.parseExcelTxtFileLine(line,',')
        if (len(items) <> 3):
            print '**** Wrong number of items on the following line ****'
            print 'There are',len(items),'instead of 3 items'
            print line

        if (items[0] <> ''):

            desc = items[0]
            acctString = items[1]
            balance = items[2]
            ### hacks here to handle inconsistency of format of 'Accum other comprehensive income' line
            if (desc[0:11]=='Accum other'):
                dept = '000'
                acct = 'na'
                ni_cc = '0000'
                ni_acct = '39091'
                skipNextLines=0 # no longer need to skip lines
            elif (desc[0:17]=='Retained Earnings'):
                dept = '000'
                acct = '3900'
                ni_cc = '0000'
                ni_acct = '35001'
            elif (desc[0:5]=='Total'):
                break
            else:
                (dept,acct,ni_cc,ni_acct) = getAcctNumber(map,acctString)

            balance = utilities.excelToNumber(balance)
            
            if (ni_acct[0] <> '0' and ni_acct <> '99999' and ni_acct <> '99998'):
                #print Upl,Co,ni_cc,ni_acct,Sub,PL,Proj,balance,0,desc


                ### Oracle can't handle '0' in the data so print the missing D/C as empty
                if (ni_acct == '95005'):
                    # need to allocate out the accounts
                    if (balance[0] == '-'):
                        amt = -1 * float(balance)
                        print >> of, 'O,%s,%s,%s,%s,%s,%s,,%s,%s' % (Co,ni_cc,'61096',Sub,PL,Proj,round(float(amt)*.6,2),'Other benefits')
                        print >> of, 'O,%s,%s,%s,%s,%s,%s,,%s,%s' % (Co,ni_cc,'67095',Sub,PL,Proj,round(float(amt)*.4,2),'Misc building')
                    else:
                        amt = float(balance)
                        print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,,%s' % (Co,ni_cc,'61096',Sub,PL,Proj,round(float(amt)*.6,2),'Other benefits')
                        print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,,%s' % (Co,ni_cc,'67095',Sub,PL,Proj,round(float(amt)*.4,2),'Misc building')
                else:
                    if (balance[0] == '-'):
                        print >> of, 'O,%s,%s,%s,%s,%s,%s,,%s,%s' % (Co,ni_cc,ni_acct,Sub,PL,Proj,balance[1:],desc)
                    else:
                        print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,,%s' % (Co,ni_cc,ni_acct,Sub,PL,Proj,balance,desc)
                
                ## now update counters
                balance = round(float(balance),2)
                total += balance
            else:
                balance = round(float(balance),2)
                if (ni_acct == '99999'):
                    S9 += balance
                elif (ni_acct == '99998'):
                    S8 += balance
                else:
                    print 'Unmapped account #', dept, acct,',', balance
        else:
            break
          
    ### somehow even though balance is rounded total still gets off track so need to round here
    total = round(total,2)
    
    if (S8 < 0):
        print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,0,%s' % (Co,'9095','90999','171','0','0',abs(S8),'Other expenses')
    else:
        print >> of, 'O,%s,%s,%s,%s,%s,%s,0,%s,%s' % (Co,'9095','90999','171','0','0',abs(S8),'Other expenses')
    total = round(total - S8,2)
    if (total < 0):
        print >> of, 'O,%s,%s,%s,%s,%s,%s,%s,0,%s' % (Co,'0000','10001','171','0','0',abs(total),'Petty Cash')
    else:
        print >> of, 'O,%s,%s,%s,%s,%s,%s,0,%s,%s' % (Co,'0000','10001','171','0','0',abs(total),'Petty Cash')
    file.close()
    of.close()
    print '\nStatistics on processed file'
    print '   Number of lines: ', linecount
    print '   Sum of all output =', total
    print '   Sum of all 99998 =', round(S8,2)
    print '   Sum of all 99999 =', round(S9,2)
    print ''


def testReadInputFile():
    readInputFile()
        

if __name__ == "__main__":
          
    testReadInputFile()