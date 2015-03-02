from __future__ import print_function
from collections import defaultdict
import codecs

# name (String)
# artist (String)
# album_artist (String)
# composer = None (String)
# album = None (String)
# genre = None (String)
# kind = None (String)
# size = None (Integer)
# total_time = None (Integer)
# track_number = None (Integer)
# track_count = None (Integer)
# disc_number = None (Integer)
# disc_count = None (Integer)
# year = None (Integer)
# date_modified = None (Time)
# date_added = None (Time)
# bit_rate = None (Integer)
# sample_rate = None (Integer)
# comments = None (String)
# rating = None (Integer)
# album_rating = None (Integer)
# play_count = None (Integer)
# location = None (String)
# compilation = None (Boolean)
# grouping = None (String)
# lastplayed = None (Time)
# length = None (Integer)

from pyItunes import *

artists = defaultdict(set)
artist_names = set()
artist_names_lc = set()
l = Library('/Users/dane/Music/iTunes/iTunes Music Library.xml')
for trackid, s in l.songs.items():
    if s.genre not in ['Rock', 'Pop', 'Country','Blues', 'Mellow']:
        print('skipping: %s - %s' % (s.name, s.genre))
        continue

    if s.album:
        artists[s.artist].add(s.album)
    if s.artist:
        lcartist = s.artist.lower().replace(' ','')
        if lcartist not in artist_names_lc:
            artist_names.add(s.artist)
            artist_names_lc.add(lcartist)
        else:
            if s.artist not in artist_names:
                print('check %s' % s.artist)

for artist in artists:
    a = artists[artist]
    num = len(a)
    lc = set()
    for album_name in a:
        mod = album_name.lower().replace(' ','')
        if mod in lc:
            print('Artist: %s\t%s' % (artist,  mod))
        else:
            lc.add(mod)



with codecs.open('albums.txt', 'w', encoding='latin1') as fp:
    for artist in artists:
        for album in artists[artist]:
            print('%s\t%s' % (artist, album), file=fp)