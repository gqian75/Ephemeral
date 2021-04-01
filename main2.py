#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/create_db.py
# Fares Fraij
# ---------------------------

import json
from models import app, db, Song

# ------------
# load_json
# ------------
def load_json(filename):
    """
    return a python dict jsn
    filename a json file
    """
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


# ------------
# create_songs
# ------------
def create_songs():
    song = load_json('songs.json')

    for oneSong in song['Songs']:
        song_name = oneSong["song_name"]
        rank = oneSong["rank"]
        artist = oneSong["artist"]
        release_date = oneSong["release_date"]
		
        newSong = Song(song_name = song_name, rank=rank, release_date=release_date, artist=artist)
        
        db.session.add(newSong)
        # commit the session to my DB.
        db.session.commit()

# ------------
# create_books
# ------------
def create_books():
    """
    populate book table
    """
    book = load_json('books.json')

    for oneBook in book['Books']:
        title = oneBook['title']
        id = oneBook['id']
		
        newBook = Book(title = title, id = id)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
	
create_songs()
