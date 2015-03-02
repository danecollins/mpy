from __future__ import print_function
from __future__ import unicode_literals

import pickle


class Track:
    '''
    Attributes:
        name
        genre       string
        rating      int
        grouping    string
        owned       bool
        spotify     bool
        tags        set
    '''
    def __init__(self):
        self.name = 'unset'
        self.genre = 'unset'
        self.rating = -1
        self.grouping = 'unset'
        self.owned = False
        self.spotify = False
        self.tags = set()

    @classmethod
    def create_with_name(cls, name):
        self = cls()
        self.name = name
        return self

    @classmethod
    def create_with_attrib(cls, name, genre, rating, grouping):
        self = cls()
        self.name = name
        self.genre = genre
        self.rating = rating
        self.grouping = grouping
        return self

    def add_tag(self, tag_or_tags):
        if isinstance(tag_or_tags, list):
            for x in tag_or_tags:
                self.tags.add(x)
        else:
            self.tags.add(tag_or_tags)


class Album:
    '''
    Attributes:
        name    string
        tracks  list of Track
        nickname short name (computed property)

    '''

    def __init__(self, name):
        self.name = name
        self.nick = False
        self.tracks = list()

    def track_count(self):
        return len(self.tracks)

    def add_track(self, track):
        self.tracks.append(track)
        return self.track_count()

    def set_nickname(self, n):
        self.nick = n

    def get_nickname(self):
        return (self.nick or self.name)

    nickname = property(get_nickname, set_nickname)

    def __str__(self):
        return "Album('%s', tracks=%d)" % (self.name, self.track_count())

    def __repr__(self):
        return "Album('%s', tracks=%d)" % (self.name, self.track_count())


class Artist:
    '''
    Attributes:
        name        string
        albums      list of Album
        nickname    short name (computed)
        active      bool
        seen_live   set(date strings)
        want_to_see bool


    '''
    def __init__(self, name):
        self.name = name
        self.nick = False
        self.albums = list()

    def add_album(self, album):
        self.albums.append(album)

    def __str__(self):
        return "Atist('%s', albums=%d)" % (self.name, len(self.albums))

    def __repr__(self):
        return "Atist('%s', albums=%d)" % (self.name, len(self.albums))

class MusicDB:
    '''
    Attributes:
        artists      list of artists

    Methods:
        load_from_file(filename='music.db')
        write_to_file(filename='music.db')
    '''
    db = list()

    def add_artist(self, artist):
        self.db.append(artist)

    @classmethod
    def load_from_file(cls, filename='music.db'):
        self = cls()
        with open(filename, 'rb') as fp:
            self.db = pickle.load(fp)
        return self

    def write_to_file(self, filename='music.db'):
        with open(filename, 'wb') as fp:
            pickle.dump(self.db, fp)
