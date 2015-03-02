from __future__ import print_function
from __future__ import unicode_literals

import unittest
from musiclib import Album, Artist, Track


class TestTrack(unittest.TestCase):
    def test_track_init(self):
        x = Track()
        self.assertEqual(x.name, 'unset')

    def test_track_init_with_name(self):
        x = Track.create_with_name('track 1')
        self.assertEqual(x.name, 'track 1')

    def test_track_init_with_attrib(self):
        x = Track.create_with_attrib('Track 1', 'Blues', 60, 'Skating')
        self.assertEqual(x.name, 'Track 1')
        self.assertEqual(x.genre, 'Blues')
        self.assertEqual(x.rating, 60)
        self.assertEqual(x.grouping, 'Skating')

    def test_track_add_tag(self):
        x = Track.create_with_name('track 1')
        x.add_tag('not_owned')
        self.assertEqual(x.tags, set(['not_owned']))
        x.add_tag(['a', 'b', 'c'])
        self.assertEqual(x.tags, set(['not_owned', 'a', 'b', 'c']))


class TestAlbum(unittest.TestCase):

    def test_album_init(self):
        x = Album('Album Name')
        self.assertEqual(x.name, 'Album Name')
        self.assertTrue(isinstance(x.tracks, list))

    def test_album_add_track(self):
        x = Album('album name')
        t1 = Track.create_with_name('track 1')
        x.add_track(t1)
        print(x)
        self.assertEqual(x.track_count(), 1)
        t2 = Track.create_with_name('track 2')
        x.add_track(t2)
        self.assertEqual(x.track_count(), 2)


if __name__ == '__main__':
    unittest.main()
