#!/usr/bin/env python3

# ---------------------------
# create_db.py
# ---------------------------

import json
from models import app, db, Song, Artist, Album

def load_json(filename):
    """
    return a python dict jsn
    filename a json file
    """
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_songs():
    song = load_json('songs.json')

    for oneSong in song['Songs']:
        song_name = oneSong["song_name"]
        rank = oneSong["rank"]
        artist = oneSong["artist"]
        release_date = oneSong["release_date"]
        album_name = oneSong["album"]
        duration = oneSong["duration"]
        newSong = Song(song_name=song_name, rank=rank, release_date=release_date, artist=artist, album_name=album_name, album_name_lower = album_name.lower(), duration=duration)
        db.session.add(newSong)
        db.session.commit()

def create_artists():
    artist = load_json('artists.json')

    for oneArtist in artist['Artists']:
        artist_name = oneArtist["artist_name"]
        artist_rank = oneArtist["artist_rank"]
        artist_genre = oneArtist["artist_genre"]
        followers = oneArtist["followers"]
		
        newArtist = Artist(artist_name=artist_name, artist_rank=artist_rank, artist_genre=artist_genre, followers=followers)
        
        db.session.add(newArtist)
        db.session.commit()

def create_albums():
    album = load_json("albums.json")

    for oneAlbum in album["Albums"]:
        album_name = oneAlbum["album_name"]
        album_release_date = oneAlbum["album_release_date"]
        album_rank = oneAlbum["album_rank"]
        artist = oneAlbum["artist"]

        newAlbum = Album(album_name=album_name, album_rank=album_rank, album_release_date=album_release_date, artist=artist)
        
        db.session.add(newAlbum)
        db.session.commit()

        try:
            someSong = Song.query.filter_by(album_name=album_name.lower()).first()
            if someSong:
                newAlbum.songs.append(someSong)
        except Exception:
            continue

create_songs()
create_artists()
create_albums()
