# shows track info for a URN or URL
from __future__ import print_function
from __future__ import unicode_literals
import codecs
from collections import Counter

import spotipy
import sys
from spdb import TrackCache

tch = TrackCache()
tch.read()
c = Counter()

if len(sys.argv) != 4:
    print('\nUsage: python tracklist2tsv.py input output tag')
    print('    to get input, select playlist tracks in spotify and copy/paste to text file')
    print('    output file will be a tab separated file')
    exit(0)
else:
    infn = sys.argv[1]
    outfn = sys.argv[2]
    tag = sys.argv[3]


fout = codecs.open(outfn, 'w', encoding='utf8')

with open(infn) as fp:
    print('spid\tartist\talbum\tsong\ttaglist', file=fout)
    for line in fp.readlines():
        c['tracks'] += 1
        line = line.strip()
        line = line[31:]
        cached_track = tch.get_track_tuple(line)
        if cached_track:
            c['cached'] += 1
            (artist, album, song) = cached_track
        else:
            c['lookup'] += 1
            urn = 'spotify:track:{}'.format(line)
            sp = spotipy.Spotify()
            track = sp.track(urn)
            artist = track['artists'][0]['name']
            album = track['album']['name']
            song = track['name']
            tch.set_track_tuple(line, (artist, album, song))

        print('%s\t%s\t%s\t%s\tspotify:%s' % (line, artist, album, song, tag), file=fout)

tch.write()

fout.close()

print("Summary")
print("  Total Tracks: %d" % c['tracks'])
print('  Cached:       %d' % c['cached'])
print('  Looked Up:    %d' % c['lookup'])
