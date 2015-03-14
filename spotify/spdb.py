from __future__ import print_function
from __future__ import unicode_literals
import json


class TrackCache:
    def __init__(self, file='./spdb.json'):
        self.db = {}
        self.__filename__ = file

    def read(self):
        with open(self.__filename__) as f:
            self.db = json.loads(f.read())

    def write(self):
        with open(self.__filename__, 'w') as f:
            f.write(json.dumps(self.db, indent=2))

    def get_track_tuple(self, key):
        return self.db.get(key)

    def set_track_tuple(self, key, track_tuple):
        self.db[key] = track_tuple
