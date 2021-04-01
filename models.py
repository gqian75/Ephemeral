#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/models.py
# Fares Fraij
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
    Song class has two attrbiutes 
    title
    id
    """
    __tablename__ = 'song'
	
    song_name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(80), nullable=False)


# ------------
# Book
# ------------
class Book(db.Model):
    """
    Book class has two attrbiutes 
    title
    id
    """
    __tablename__ = 'book'
	
    title = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)

db.drop_all()
db.create_all()