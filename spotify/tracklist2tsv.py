# shows track info for a URN or URL
from __future__ import print_function
from __future__ import unicode_literals
import codecs

import spotipy
import sys


if len(sys.argv) != 4:
    print('\nUsage: python tracklist2tsv.py input output tag')
    exit(0)
else:
    infn = sys.argv[1]
    outfn = sys.argv[2]
    tag = sys.argv[3]


fout = codecs.open(outfn, 'w', encoding='utf8')

with open(infn) as fp:
    print('spid\tartist\talbum\tsong\ttaglist', file=fout)
    for line in fp.readlines():
        line = line.strip()
        line = line[31:]
        urn = 'spotify:track:{}'.format(line)
        sp = spotipy.Spotify()
        track = sp.track(urn)
        print('%s\t%s\t%s\t%s\tspotify:%s' % (line,
                                              track['artists'][0]['name'],
                                              track['album']['name'],
                                              track['name'],
                                              tag), file=fout)
fout.close
