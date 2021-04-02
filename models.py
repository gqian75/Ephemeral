#!/usr/bin/env python3

# ---------------------------
# models.py
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://postgres:zxcvb@localhost:5432/songdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

link = db.Table('link',
    db.Column('song_rank',db.Integer,db.ForeignKey('song.rank')),
    db.Column('artist_rank',db.Integer,db.ForeignKey('artist.artist_rank'))
    )

class Song(db.Model):
    """
    Song class has 6 attrbiutes 
    song_name, rank, release_date, duration, artist, album
    """
    __tablename__ = 'song'

    rank = db.Column(db.Integer, primary_key=True)
	
    song_name = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(80), nullable=False)
    album_name = db.Column(db.String(80), nullable=False)
    album_name_lower = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.Integer,nullable=True)

    album_rank = db.Column(db.Integer, db.ForeignKey('album.album_rank'))

class Artist(db.Model):
    """
    Artist class has 4 attrbiutes 
    artist_name, artist_rank, artist_genre, followers
    """
    __tablename__ = 'artist'

    artist_rank = db.Column(db.Integer, primary_key=True)

    artist_name = db.Column(db.String(80), nullable=False)
    artist_genre = db.Column(db.String(120), nullable=False)
    followers = db.Column(db.Integer,nullable=False)

class Album(db.Model):
    """
    Album class has 4 attrbiutes 
    album_name, album_rank, album_release_date, artist
    """
    __tablename__ = 'album'

    album_rank = db.Column(db.Integer, primary_key=True)

    album_name = db.Column(db.String(80), nullable=False)
    album_release_date = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)

    songs = db.relationship('Song', backref = 'album')

db.drop_all()
db.create_all()