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
        song_id = oneSong["song_id"]
        image_url = oneSong["image_url"]
        newSong = Song(song_name=song_name, rank=rank, release_date=release_date, artist=artist, album_name=album_name,
        album_name_lower = album_name.lower(), duration=duration, song_id=song_id, image_url=image_url)
        db.session.add(newSong)
        db.session.commit()

def create_artists():
    artist = load_json('artists.json')

    for oneArtist in artist['Artists']:
        artist_name = oneArtist["artist_name"]
        artist_id = oneArtist["artist_id"]
        artist_rank = oneArtist["artist_rank"]
        artist_genre = oneArtist["artist_genre"]
        followers = oneArtist["followers"]
        popularity = oneArtist["popularity"]
        image_url = oneArtist["image_url"]

        newArtist = Artist(artist_name=artist_name, artist_rank=artist_rank, artist_genre=artist_genre,
        followers=followers, popularity=popularity, artist_id=artist_id, image_url=image_url)

        db.session.add(newArtist)
        db.session.commit()

        someSong = Song.query.filter_by(artist=artist_name).first()
        if someSong:
            newArtist.songs.append(someSong)

        someAlbum = Album.query.filter_by(artist=artist_name).first()
        if someAlbum:
            newArtist.albums.append(someAlbum)

def create_albums():
    album = load_json("albums.json")

    for oneAlbum in album["Albums"]:
        album_name = oneAlbum["album_name"]
        album_release_date = oneAlbum["album_release_date"]
        album_rank = oneAlbum["album_rank"]
        artist = oneAlbum["artist"]
        album_genre = oneAlbum["genre"]
        album_id = oneAlbum["album_id"]
        newAlbum = Album(album_name=album_name, album_rank=album_rank, album_release_date=album_release_date, artist=artist, album_genre=album_genre, album_id = album_id)

        db.session.add(newAlbum)
        db.session.commit()

        # try:
        someSong = Song.query.filter_by(album_name_lower=album_name.lower()).first()
        if someSong:
            newAlbum.songs.append(someSong)
        # except Exception:
            # continue

if __name__ == "__main__":
    create_songs()
    create_albums()
    create_artists()
