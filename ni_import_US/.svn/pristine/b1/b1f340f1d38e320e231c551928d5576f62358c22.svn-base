#!/usr/bin/env python

def striplf(s):
    return (s.rstrip('\n'))

def excelToNumber(s):
    ## check to see if token is negative number but formatted with parens
    if ( s[0] == '(' ):
        s = '-' + s[1:len(s)-1]

    s = s.replace(',','')
    
    ## need to round numbers to 2 digits
    tmp = float(s)
    s = '%.2f' % tmp
    return(s)

def parseExcelTxtFileLine(s):
    fields = []
    s = s.rstrip("\n")
    while (len(s)>0):
        if (s[0] == '"'):
            ## if token is quoted find next quote
            tmp = s.find('"',1)
            token=s[1:tmp]
            tmp=tmp+1  ## skip tab also
        else:
            ## if token is not quoted, find next tab
            tmp = s.find('\t')
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
        ## if all we have is a tab then last field is empty
        if (s == '\t'):
            ###BUG - so should be able to do this but does not work -return(fields.append(''))
            fields.append(' ')
            return(fields)
        else:
            s = s[1:] ## strip off tab

    return(fields)

### test parse function
def testParseExcelTxt():
    s1 = 'Cash - Operating	"0001100??, /Y"	"7,929,871.10"	"5,072,492.28"'
    print "test 1 -", s1
    for item in parseExcelTxtFileLine(s1):
        print item

    s2 = 'this	"a,string	with,tabs"	line3	line4'
    print "test 2 -", s2
    for item in parseExcelTxtFileLine(s2):
        print item

    s3 = 'this	"a	string	with	tabs"	(3.22)	line4	'
    print "test 3 -", s3
    for item in parseExcelTxtFileLine(s3):
        print excelToNumber(item)

if __name__ == "__main__":
    testParseExcelTxt()
