from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter
 
import sys
import re
import codecs

fn = sys.argv[1]

fp = open(fn)
fout = open('out.txt','w')

linenumber=0
line = fp.readline()
linenumber += 1
while line:
    fields = re.split('[", |]',line)
    for f in fields:
        try:
            x=f.encode('ascii', 'ignore')
            if (x != f):
                print(f,'-',x)
        except:
            print(f,file=fout)
            print(f)
    line = fp.readline()
    linenumber += 1
#    if linenumber > 50: break

fp.close()
fout.close()