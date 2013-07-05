import shutil
import sys
import utilities


### Fixed NI fields
# Accounts that need to be mapped
# 


   
def split_accounts():
   
    file=open('output_split.csv')
    of = open('output_simple.csv','w')
    ## Initialize Counters
    linecount=0
    print "\n --- splitting out the account ---\n"
    
    for line in file.readlines():
        line = line.rstrip('\n')
        (f1,f2,dept,acct,f5,f6,f7,amt1,amt2,description) = line.split(',')
        if (amt1 == ''):
            amt = '-' + amt2
        if (amt2 == ''):
            amt = amt1

        linecount += 1
        print >> of, "%s,%s,%s,%s" % (dept, acct, amt,description)          
    file.close()
    of.close()

        
split_accounts()