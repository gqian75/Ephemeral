import os
import datetime
from create_db import app, db, Song, Artist, Album
#from models import db
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/static", template_folder="./frontend/templates")
CORS(app)

song_list = db.session.query(Song).all()
artist_list = db.session.query(Artist).all()
album_list = db.session.query(Album).all()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  return render_template("index.html")


@app.route("/api/test")
def test():
      return "TEST123456789"

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/albums/')
def albums():
    return render_template('albums.html',albums=album_list)

@app.route('/artists/')
def artists():
    
    return render_template('artists.html',artists=artist_list)

@app.route('/songs/')
def songs():
    return render_template('songs.html',songs=song_list)

#Dynamic instances of different types
def id(string):
    string = string.replace(" ","-").lower().strip()
    string = string.replace("'","")
    string = string.replace("/","")
    return string

def find(name, data, list_type):
    
    for list_item in data:
        if(list_type == "album"):
            if(list_item.album_id == name):
                return list_item
        elif(list_type == "artist"):
            if(list_item.artist_id == name):
                return list_item
        elif(list_type == "song"):
            if(list_item.song_id == name):
                return list_item
    return None

@app.route('/albums/<string:_album>')
def album(_album):
    #_album = id(_album)
    #album_list.get(_album,None)
    return render_template('album.html', album=find(_album,album_list,'album'))

@app.route('/artists/<string:_artist>')
def artist(_artist):
    #_artist = id(_artist)
    return render_template('artist.html', artist=find(_artist,artist_list,'artist'))

@app.route('/songs/<string:_song>')
def song(_song):
    #_song = id(_song)
    return render_template('song.html', song=find(_song,song_list,'song'))

def format_strings(string):
    new_string = ""
    for char in string:
        if (char == "{" or char == "}" or char == '"'):
            new_string += ""
            
        elif (char == ","):
            new_string += ", "
        else:
            new_string += char
    new_string = new_string.title()
    return new_string

def format_lists():
    for artist in artist_list:
        artist.artist_genre = format_strings(artist.artist_genre)
    for album in album_list:
        album.album_genre = format_strings(album.album_genre)
        #print(album.album_genre)
    for song in song_list:
        seconds = str(int((int(song.duration)//1000.0)%60))
        song.duration = str(int((int(song.duration)//1000.0)//60)) + ":"
        if(len(seconds) == 1):
            song.duration += "0" + seconds
        else:
            song.duration += seconds
        

if __name__ == "__main__":
    format_lists()
    app.jinja_env.globals.update(id=id) 
    app.run(host='0.0.0.0', port=80, threaded=True)
    #app.run()
    
   