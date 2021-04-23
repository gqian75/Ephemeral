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
link2 = db.Table('link2',
    db.Column('song_rank',db.Integer,db.ForeignKey('song.rank')),
    db.Column('album_rank',db.Integer,db.ForeignKey('album.album_rank'))
    )

class Song(db.Model):
    """
    Song class has 8 attrbiutes
    song_name, rank, release_date, duration, artist, album_name, image_url, song_id
    """
    __tablename__ = 'song'

    # Primary key of pillar song
    rank = db.Column(db.Integer, primary_key=True)

    # Other attributes of pillar song
    song_name = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(80), nullable=False)
    album_name = db.Column(db.String(80), nullable=False)
    album_name_lower = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.String(80),nullable=True)
    song_id = db.Column(db.String([]),nullable=False)

    # Links songs to albums (one-to-many relation)
    album_rank = db.Column(db.Integer, db.ForeignKey('album.album_rank'))
    # artists = db.relationship('Artist', backref = 'song', uselist = False)
    image_url = db.Column(db.String(80),nullable=True)

class Artist(db.Model):
    """
    Artist class has 7 attrbiutes
    artist_name, artist_rank, artist_genre, followers, artist_id, popularity, image_url
    """
    __tablename__ = 'artist'

    # Primary key of pillar artist
    artist_rank = db.Column(db.Integer, primary_key=True)

    # Other attributes of pillar artist
    artist_name = db.Column(db.String(80), nullable=False)
    artist_genre = db.Column(db.String([]), nullable=False)
    followers = db.Column(db.Integer,nullable=False)
    popularity = db.Column(db.Integer)
    artist_id = db.Column(db.String([]),nullable=False)

    # Links artists to songs (many-to-many relation)
    songs = db.relationship('Song',secondary = 'link', backref = 'compose')
    # Links artists to albums (one-to-many relation)
    albums = db.relationship('Album', backref = 'release')
    # song_rank = db.Column(db.Integer, db.ForeignKey('song.rank'))
    image_url = db.Column(db.String(80), nullable=False)

class Album(db.Model):
    """
    Album class has 6 attrbiutes
    album_name, album_rank, album_release_date, artist, album_genre, album_id
    """
    __tablename__ = 'album'

    # Primary key of pillar album
    album_rank = db.Column(db.Integer, primary_key=True)

    # Other attributes of pillar album
    album_name = db.Column(db.String(80), nullable=False)
    album_release_date = db.Column(db.String(80), nullable=False)
    artist = db.Column(db.String(80), nullable=False)
    album_genre = db.Column(db.String([]))
    album_id = db.Column(db.String([]),nullable=False)

    songs = db.relationship('Song', secondary='link2', backref='contains')
    # Links artist to album (one-to-many relation)
    artist_rank = db.Column(db.Integer, db.ForeignKey('artist.artist_rank'))

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
