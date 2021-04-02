#!/usr/bin/env python3

# ---------------------------
# test.py
# ---------------------------

import os
import sys
import unittest
from models import db, Song, Artist, Album

# -----------
# DBTestCases
# -----------
class DBTestCases(unittest.TestCase):

    def test_song_1(self):
        song = Song(song_name="ABC", rank=187, release_date="2021-01-01", artist="def", \
            album_name="A1", album_name_lower = "A1".lower(), duration=1000)
        db.session.add(song)
        db.session.commit()

        res = db.session.query(Song).filter_by(rank = 187).one()
        self.assertEqual(str(res.rank), '187')

        db.session.query(Song).filter_by(rank = 187).delete()
        db.session.commit()

    def test_song_2(self):
        song = Song(song_name="ABC", rank=187, release_date="2021-01-01", artist="def", \
            album_name="A1", album_name_lower = "A1".lower(), duration=1000)
        db.session.add(song)
        db.session.commit()

        res = db.session.query(Song).filter_by(song_name = "ABC").one()
        self.assertNotEqual(str(res.artist), 'DEF')

        db.session.query(Song).filter_by(rank = 187).delete()
        db.session.commit()

    def test_song_3(self):
        song = Song(song_name="ABC", rank=187, release_date="2021-01-01", artist="def", \
            album_name="A1", album_name_lower = "A1".lower(), duration=1000)
        song2 = Song(song_name="ABC", rank=200, release_date="2021-01-01", artist="def", \
            album_name="A1", album_name_lower = "A1".lower(), duration=2000)
        db.session.add(song)
        db.session.add(song2)
        db.session.commit()

        res = db.session.query(Song).filter_by(song_name="ABC").all()
        self.assertNotEqual(str(len(res)), '1')

        db.session.query(Song).filter_by(rank = 187).delete()
        db.session.query(Song).filter_by(rank = 200).delete()
        db.session.commit()

    def test_album_1(self):
        album = Album(album_name="A1", album_rank=150, album_release_date="2021-01-01", artist="def")
        db.session.add(album)
        db.session.commit()

        res = db.session.query(Album).filter_by(album_rank = 150).one()
        self.assertNotEqual(str(res.album_rank), 150)

        db.session.query(Album).filter_by(album_rank = 150).delete()
        db.session.commit()

    def test_album_2(self):
        album = Album(album_name="A1", album_rank=150, album_release_date="2021-01-01", artist="def")
        db.session.add(album)
        db.session.commit()

        res = db.session.query(Album).filter_by(artist = "def").one()
        self.assertEqual(str(res.album_rank), '150')

        db.session.query(Album).filter_by(album_rank = 150).delete()
        db.session.commit()

    def test_album_3(self):
        album = Album(album_name="A1", album_rank=150, album_release_date="2021-01-01", artist="def")
        album2 = Album(album_name="A2", album_rank=151, album_release_date="2021-01-01", artist="ghi")
        db.session.add(album)
        db.session.add(album2)
        db.session.commit()

        res = db.session.query(Album).filter_by(album_release_date = "2021-01-01").all()
        self.assertEqual(str(len(res)), '2')

        db.session.query(Album).filter_by(album_rank = 150).delete()
        db.session.query(Album).filter_by(album_rank = 151).delete()
        db.session.commit()

    def test_artist_1(self):
        artist = Artist(artist_name="def", artist_rank=200, artist_genre=["genre"], followers=500, popularity=180)
        db.session.add(artist)
        db.session.commit()

        res = db.session.query(Artist).filter_by(artist_rank = 200).one()
        self.assertEqual(str(res.artist_rank), '200')

        db.session.query(Artist).filter_by(artist_rank = 200).delete()
        db.session.commit()

    def test_artist_2(self):
        artist = Artist(artist_name="def", artist_rank=200, artist_genre=["pop", "rock", "hip-hop"], followers=500, popularity=180)
        db.session.add(artist)
        db.session.commit()

        res = db.session.query(Artist).filter_by(artist_rank = 200).one()
        self.assertIn("rock", res.artist_genre)

        db.session.query(Artist).filter_by(artist_rank = 200).delete()
        db.session.commit()

    def test_artist_3(self):
        artist = Artist(artist_name="def", artist_rank=200, artist_genre=["pop"], followers=500, popularity=180)
        artist2 = Artist(artist_name="DEF", artist_rank=201, artist_genre=["rock"], followers=500, popularity=180)
        db.session.add(artist)
        db.session.add(artist2)
        db.session.commit()

        res = db.session.query(Artist).filter_by(artist_name = 'def').one()
        self.assertEqual(str(res.artist_rank), '200')

        db.session.query(Artist).filter_by(artist_rank = 200).delete()
        db.session.query(Artist).filter_by(artist_rank = 201).delete()
        db.session.commit()

if __name__ == '__main__':
    unittest.main()