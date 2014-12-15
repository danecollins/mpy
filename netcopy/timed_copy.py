from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter

import os
import shutil
import datetime
import socket

def get_files(source_pattern):
    for i in range(5):
        with open('test_file{}.bin'.format(i),'wb') as fp:
            fp.write(bytearray(os.urandom(1000000)))

def run_test(source_pattern):
    

    basedir = '\\\\us-{}-argo\\awr\\Share\\Users\\dane\\{}\\{}'
    destinations = ['lou','cam','els']

    c = Counter()
    for i in range(5):
        print(i)
        source_file = source_pattern.format(i)
        for d in destinations:
            destfile = basedir.format(d,d,source_file)
            print('%s to %s' % (source_file,destfile))
            start = datetime.datetime.now()
            shutil.copy2(source_file, destfile)
            end = datetime.datetime.now()
            delta = end-start
            elapsed = delta.seconds + float(delta.microseconds)/1000000.
            c[d] += elapsed
            os.remove(destfile)
    return c

    print('Copied 5 1Mb files to each server in:')
    for d in destinations:
        print( "  {}: {} S ({} MBps)".format(d,round(c[d],2),round(5/c[d],2)))

if __name__ == '__main__':
    source_pattern = 'test_file{}.bin'
    host = socket.gethostname()
    log_string = "{}\t{}\t".format(datetime.datetime.now(),host)
    times = run_tests(source_pattern)
    log_string+= '%4.2f MBps\t%4.2f MBps\t%4.2Mbps'.format(
        times['cam'],times['els'],times['lou'])
    print(log_string)
    with open('\\us-cam-argo\awr\share\users\dane\netcopy\log_of_times.txt','a') as fp:
        print(log_string,file=fp)
            



### Source |            Destination            |
### -------|-----------------------------------|
###        |  CO       |    CAM    |    ELS    |
###  CO    | 1.97 MBps | 0.16 MBps | 0.17 MBps |
###  CAM   | 1.63 MBps | 4.37 MBps | 2.08 MBps |
###  ELS   | 0.20 MBps | 2.65 MBps | 6.68 MBps |
