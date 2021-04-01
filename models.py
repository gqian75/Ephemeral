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

class Song(db.Model):
    """
    Song class has 4 attrbiutes 
    song_name, rank, artist, release_date
    """
    __tablename__ = 'song'
	
    song_name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(80), nullable=False)

class Artist(db.Model):
    """
    Artist class has 4 attrbiutes 
    artist_name, artist_rank, artist_genre, followers
    """
    __tablename__ = 'artist'

    artist_name = db.Column(db.String(80), nullable=False)
    artist_rank = db.Column(db.Integer, primary_key=True)
    artist_genre = db.Column(db.String(80), nullable=False)
    followers = db.Column(db.Integer)

class Album(db.Model):
    pass

db.drop_all()
db.create_all()