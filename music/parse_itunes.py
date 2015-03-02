from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict

import xml.etree.ElementTree as ET

tree = ET.parse('library.xml')
root = tree.getroot()

## loop through all tracks
tracks = root[0][15]

artists = defaultdict(list)

musictypes = ['Purchased AAC audio file', 'MPEG audio file','Matched AAC audio file','AAC audio file',
              'Apple Lossless audio file','AIFF audio file']

for trackindex in range(0,len(tracks),2):
	trackid     = tracks[trackindex]
	trackfields = tracks[trackindex+1]

	track={}
	for fieldindex in range(0,len(trackfields)):
		if (trackfields[fieldindex].text == 'Name'):
			track['name'] = trackfields[fieldindex+1].text

		if (trackfields[fieldindex].text == 'Artist'):
			track['artist'] = trackfields[fieldindex+1].text

		if (trackfields[fieldindex].text == 'Play Count'):
			track['count'] = trackfields[fieldindex+1].text

		if (trackfields[fieldindex].text == 'Genre'):
			track['genre'] = trackfields[fieldindex+1].text

		if (trackfields[fieldindex].text == 'Rating'):
			track['rating'] = trackfields[fieldindex+1].text

		if (trackfields[fieldindex].text == 'Kind'):
			track['kind'] = trackfields[fieldindex+1].text


	if track['kind'] in musictypes:
		if 'artist' in track:
			artists[track['artist']].append(track)


print('tracks,plays,avgrating,ratingsum,artist')
for artist in artists:
	tracks = artists[artist]
	rating = 0
	count = 0
	playcount = 0
	for track in tracks:
		count += 1
		if 'rating' in track:
			rating += int(track['rating'])
		if 'count' in track:
			playcount += int(track['count'])


	#print('tracks: %2d, plays: %4d, avgrating: %3.1f\t%s' % (count, playcount, round(float(rating/20)/count,1),artist))
	print('%2d,%4d,%3.1f,%d,%s' % (count, playcount, rating/20,round(float(rating/20)/count,1),artist))





