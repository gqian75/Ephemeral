#!/usr/bin/env python3

# ---------------------------
# models.py
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://postgres:zxcvb@localhost:5432/songdb')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://postgres:jake@localhost:5432/songdb')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://zuvviiky:gUj52EfnqxD2UeVkSPQ7kDeiAQOwMcu6@queenie.db.elephantsql.com:5432/zuvviiky')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)


link = db.Table('link',
    db.Column('song_rank',db.Integer,db.ForeignKey('song.rank')),
    db.Column('artist_rank',db.Integer,db.ForeignKey('artist.artist_rank'))
    )

class Song(db.Model):
    """
    Song class has 7 attrbiutes
    song_name, rank, release_date, duration, artist, album, image_url
    """
    __tablename__ = 'song'

    rank = db.Column(db.Integer, primary_key=True)

    song_name = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(80), nullable=False)
    album_name = db.Column(db.String(80), nullable=False)
    album_name_lower = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.String(80),nullable=True)
    song_id = db.Column(db.String([]),nullable=False)

    #durationms = db.Column(db.Integer,nullable=True)

    album_rank = db.Column(db.Integer, db.ForeignKey('album.album_rank'))
    # artists = db.relationship('Artist', backref = 'song', uselist = False)
    image_url = db.Column(db.String(80),nullable=True)

class Artist(db.Model):
    """
    Artist class has 5 attrbiutes
    artist_name, artist_rank, artist_genre, followers, image_url
    """
    __tablename__ = 'artist'

    artist_rank = db.Column(db.Integer, primary_key=True)

    artist_name = db.Column(db.String(80), nullable=False)
    artist_genre = db.Column(db.String([]), nullable=False)
    followers = db.Column(db.Integer,nullable=False)
    popularity = db.Column(db.Integer)
    artist_id = db.Column(db.String([]),nullable=False)
    songs = db.relationship('Song',secondary = 'link', backref = 'compose')
    albums = db.relationship('Album', backref = 'release')
    # song_rank = db.Column(db.Integer, db.ForeignKey('song.rank'))
    image_url = db.Column(db.String(80), nullable=False)

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
    album_genre = db.Column(db.String([]))
    album_id = db.Column(db.String([]),nullable=False)
    songs = db.relationship('Song', backref = 'album')

    artist_rank = db.Column(db.Integer, db.ForeignKey('artist.artist_rank'))


# db.drop_all()
# db.create_all()
