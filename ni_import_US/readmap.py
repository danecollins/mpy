
import shutil
import sys
import utilities

department = {}
department['0'] = '0000'
department['300'] = '0000'
department['400'] = '1090'
department['500'] = '4010'
department['600'] = '6010'
department['700'] = '2010'
department['800'] = '9095'

# consolidated is a boolean which is true if we're running a consolidated
# account list which means columns 3 and 4 are the ni accounts.  If we're
# running the subs then the ni accounts are in columns 5 and 6
def readAccountMap(consolidated):
    file=open('account_map.txt')
    accountMap={}
    lineNumber = 0
    line = file.readline() ## eat first line
    for line in file.readlines():
        ## second argument is the delimiter
        items = utilities.parseExcelTxtFileLine(line,'\t')
        lineNumber = lineNumber + 1
        # all lines must have 6 columns
        if (len(items) <> 7):
            print 'line #', lineNumber, ' does not have the right number of columns. s/b 6 but is ',len(items)
            print line
            
        if (items):
            awr_dept = items[0]
            if (awr_dept == '0'):
                awr_dept = '000'
            awr_acct = items[1]
            if (consolidated):
                ni_cc    = items[2]
                ni_acct  = items[3]
            else:
                ni_cc    = items[4]
                ni_acct  = items[5]               

            if (awr_acct <> ''):
                key = awr_dept + awr_acct
                if (ni_acct == ''):
                    # if the ni_acct is missing then set it to 0
                    ni_acct = '00000'
                if (accountMap.has_key(key)):
                    if (accountMap[key] <> ni_acct):
                        print 'overriding account',key,'from',accountMap[key],'to',ni_acct
                accountMap[key] = (ni_cc,ni_acct)

    file.close()
    return(accountMap)

def testReadMap():
    map = readAccountMap(True)
    print 'map contains', len(map), 'items'
    print 'test 1 - map account 1500 shoud produce 15040 = ', map['1500']

if __name__ == "__main__":
    testReadMap()
