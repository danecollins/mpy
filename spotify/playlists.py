# shows a user's playlists (need to be authenticated via oauth)

import sys
import os
import spotipy
import spotipy.util as util

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])


if __name__ == '__main__':
    username = '128323673'

    #token = util.prompt_for_user_token(username)
    token = 'http://vividamps.com/about?code=AQAnal29EWVeEUlFh-6oOp6JOppxqc4z0PKZ9Lxr2o5k2hR9YCClRj1UA_WhWbhe3SHZ6s2paOBVJdbmwHUwum_C0BehZNNH5DwuqRBplJFvYpORpnlCEvDy5wusDPUKcZh6vMOnFV6DEuNaBbh8drjrQtgn5e920clyxoL4qtTdaAQpe_QYDbHMOawFJYSs'


    if token:
        top = 100
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print
                print playlist['name']
                print '  total tracks', playlist['tracks']['total']
                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                print tracks
                exit(0)
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print "Can't get token for", username
