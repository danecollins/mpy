from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter,namedtuple

import os
import shutil
import datetime
import socket
import time
import sys

def generate_test_files(count,source_pattern='test_file{}.bin'):
    source_files = []
    for i in range(count):
        fn = source_pattern.format(i)
        with open(fn,'wb') as fp:
            fp.write(bytearray(os.urandom(1000000)))
        source_files.append(fn)
    return source_files

def get_destinations():
    destination_list = []
    # destinations are named tuples of destination path and printable label name
    dest = namedtuple('Destination',['path','name'])

    # first add paths for argo boxes
    for d in ['lou','cam','els']:
        path = "\\\\us-{}-argo\\awr\\Share\\Users\\dane\\{}".format(d,d)
        name = 'ARGO-{}'.format(d)
        destination_list.append( dest._make([path,name]))

    # next add the additional destinations
    destination_list.append( dest._make(['\\\\ts1a\\dane\\tmp','TS1A']) )
    destination_list.append( dest._make(['\\\\web1a\\confluence_html\\tmp','wiki host']) )
    return destination_list


def run_test(source_files, destinations):  
    c = Counter()
    for source in source_files:
        for d in destinations:
            print('%s to %s' % (source,d.path))

            start = datetime.datetime.now()
            shutil.copy2(source, d.path)
            end = datetime.datetime.now()
            delta = end-start
            elapsed = delta.seconds + float(delta.microseconds)/1000000.
            c[d.name] += elapsed
            os.remove(d.path + '\\' + source) ## full filename for remove

    # convert from total seconds to MBps
    for site in destinations:
        c[site.name] = round( 5.0/c[site.name], 2)
    return c

if __name__ == '__main__':
    if len(sys.argv) > 1:
        interval = float(sys.argv[1]) * 60
    else:
        interval = False

    sources = generate_test_files(5)
    destinations = get_destinations()
    host = socket.gethostname()
    while True:
        log_time = datetime.datetime.now().strftime('%m-%d %H:%M')
        log_string  = "%s\t%-8s\t" % (log_time,host)
        head_string = "# time     \thost    \t"
        print(log_string)
        times = run_test(sources,destinations)
        for d in destinations:
            log_string  += '%4.2f\t' % times[d.name]
            head_string += '%s\t' % d.name

        print(head_string)
        print(log_string)
        with open('\\\\us-cam-argo\\awr\\share\\users\\dane\\netcopy\\log_of_times.txt','a') as fp:
            print(log_string,file=fp)
        if interval:
            print("Sleeping %f seconds" % interval)
            time.sleep(interval)
        else:
            break



### Source |            Destination            |
### -------|-----------------------------------|
###        |  CO       |    CAM    |    ELS    |
###  CO    | 1.97 MBps | 0.16 MBps | 0.17 MBps |
###  CAM   | 1.63 MBps | 4.37 MBps | 2.08 MBps |
###  ELS   | 0.20 MBps | 2.65 MBps | 6.68 MBps |
