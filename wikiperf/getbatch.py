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
        return(z)
    except urllib2.HTTPError as e:
        print e.code
        #print e.read()



URLS = [
    ['batch.js', 'https://wiki.awrcorp.com/s/d41d8cd98f00b204e9800998ecf8427e/en_GB-1988229788/4733/f235dd088df5682b0560ab6fc66ed22c9124c0be.49/44/_/download/superbatch/js/batch.js']
       ]

for url in URLS:
    desc = url[0]
    AWR = url[1]
    t0=time.time()
    content_size = get_wiki_page(AWR,'AWR')
    t1=time.time()
    AWR_time = t1-t0

    print desc
    print '  AWR time = ', round(AWR_time,1)
    print '  content size = ', content_size

    print


