#!/usr/bin/env python

def striplf(s):
    return (s.rstrip('\n'))

def readExistingAccountMap():
    file=open('coa_map.csv')
    accountMap={}
    line = file.readline() ## eat first line
    for line in file.readlines():
        line = striplf(line)
        (expenseType,natAcctNum) = line.split(',')
        ### ran into a problem initially because there was white space
        ### around the keys so strip these fields to be safe
        expenseType=(expenseType.lstrip()).rstrip()
        natAcctNum=(natAcctNum.lstrip()).rstrip()
        accountMap[expenseType] = natAcctNum
    file.close()
    return(accountMap)

def parseExcelCsv(s):
    fields = []
    while (s):
        if (len(s)>0 and s[0] == '"'):
            ## if token is quoted find next quote
            tmp = s.find('"',1)
            token=s[1:tmp]
            tmp=tmp+1  ## skip comma also
        else:
            ## if token is not quoted, find next comma
            tmp = s.find(',')
            if (tmp == -1):
                ## this is the last token
                token = s
                s = ''
            else:
                token=s[0:tmp]
        ## need to remove current token
        ##  TODO: note if this is the last token tmp is -1 and s is set so this is redundant
        s = s[tmp:]
        fields.append(token)
        ## if we are out of string then return
        if (len(s)==0):
            return(fields)
        ## if all we have is a comma then last field is empty
        if (s == ','):
            ###BUG - so should be able to do this but does not work -return(fields.append(''))
            fields.append(' ')
            return(fields)
        else:
            s = s[1:] ## strip off comma

### test parse function
def testParseExcelCsv():
    s1 = 'this,is,a,test'
    print "test 1 -", s1
    for item in parseExcelCsv(s1):
        print item
        
    s2 = 'this,"a,string,with,commas",line3,line4'
    print "test 2 -", s2
    for item in parseExcelCsv(s2):
        print item
        
    s3 = 'this,"a,string,with,commas",line3,line4,'
    print "test 3 -", s3
    for item in parseExcelCsv(s3):
        print item
        
            
#testParseExcelCsv()