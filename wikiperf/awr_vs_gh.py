import urllib2,base64
import time

def get_wiki_page(path,host):
    req = urllib2.Request(path)
    try:
        if (host=='AWR'):
            base64string = base64.encodestring('dcollins:Ak6nc6uu5')
            req.add_header("Authorization", "Basic %s" % base64string) 
        else:
            base64string = base64.encodestring('dane:Ak6nc6uu5')
            req.add_header("Authorization", "Basic %s" % base64string)

        x=urllib2.urlopen(req)
        y=x.read()
        z=len(y)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
    return(z)


URLS = [
    ['Focus group home page',
     'http://gh.awr.com/display/TEST/Focus+Groups',
     'https://wiki.awrcorp.com/display/focusgroups/Home' ],
    ['Boolean Engine page',
     'http://gh.awr.com/display/TEST/Boost+Boolean+Engine',
     'https://wiki.awrcorp.com/display/focusgroups/Boost+Boolean+Engine'],
    ['Editorial Calendar',
     'http://gh.awr.com/display/TEST/Advertisement+Editorial+Calendar+2014',
     'https://wiki.awrcorp.com/display/marketing/Advertisement+Editorial+Calendar+2014']
      ]

for url in URLS:
    desc = url[0]
    GH = url[1]
    AWR = url[2]
    t0=time.time()
    x=get_wiki_page(AWR,'AWR')
    t1=time.time()
    AWR_time = t1-t0

    t0 = time.time()
    x-get_wiki_page(GH,'GH')
    t1=time.time()
    GH_time = t1-t0

    print desc
    print '  AWR time = ', round(AWR_time,1)
    print '  GH  time = ', round(GH_time,1)
    print '  ratio = ', round(AWR_time/GH_time,1)
    print


