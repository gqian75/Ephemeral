import os
from create_db import app, db, Song, Artist, Album, create_songs, create_artists, create_albums
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/static", template_folder="./frontend/templates")
CORS(app)

song_list = db.session.query(Song).all()
artist_list = db.session.query(Artist).all()
album_list = db.session.query(Album).all()

# artist_list = { "Olivia Rodrigo" : {
#     "name" : "Olivia Rodrigo",
#     "Genre" : "Pop",
#     "Age" : 18,
#     "Label" : "Interscope",
#     "Song" : {"name" : "driver's license", "link" : "drivers-license"},
#     "Albums" : {"name" : "driver's license", "link" : "drivers-license"}
#     },

#     "The Weeknd" : {
#     "name" : "The Weeknd",
#     "Genre" : "R&b/Soul",
#     "Age" : 31,
#     "Label" : "XO",
#     "Song" : {"name" : "Save Your Tears", "link" : "save-your-tears"},
#     "Albums" : {"name" : "After Hours", "link" : "after-hours"}
#     },

#     "Yung Bleu" : {
#     "name" : "Yung Bleu",
#     "Genre" : "Rap",
#     "Age" : 26,
#     "Label" : "Various",
#     "Song" : {"name" : "You're Mines Still", "link" : "youre-mines-still"},
#     "Albums" : {"name" : "Love Scars: The 5 Stages of Emotions", "link" : "love-scars-the-5-stages-of-emotions"}
#     }
# }

# song_list = { "driver's license" : {
#     "name" : "driver's license",
#     "artist" : {"name" : "Olivia Rodrigo", "link" : "olivia-rodrigo"},
#     "album" : {"name" : "driver's license", "link" : "drivers-license"},
#     "release" : "2021/01/08",
#     "length" : "4:02"
#     },

#     "Save Your Tears" : {
#     "name" : "Save Your Tears",
#     "artist" : {"name" : "The Weeknd", "link" : "the-weeknd"},
#     "album" : {"name" : "After Hours", "link" : "after-hours"},
#     "release" : "2020/08/09",
#     "length" : "6:01"
#     },

#     "You're Mines Still" : {
#     "name" : "You're Mines Still",
#     "artist" : {"name" : "Yung Bleu", "link" : "yung-bleu"},
#     "album" : {"name" : "Love Scars: The 5 Stages of Emotions", "link" : "love-scars-the-5-stages-of-emotions"},
#     "release" : "2020/10/02",
#     "length" : "3:46"
#     },

# }
# album_list = { "driver's license": {
#     "name" : "driver's license",
#     "release" : "2021/01/08",
#     "artist" : {"name" : "Olivia Rodrigo", "link" : "olivia-rodrigo"},
#     "type" : "Single",
#     "genre" : "Pop",
#     "song" : {"name" : "driver's license", "link" : "drivers-license"}
#     },

#     "After Hours": {
#     "name" : "After Hours",
#     "release" : "2020/03/20",
#     "artist" : {"name" : "The Weeknd", "link" : "the-weeknd"},
#     "type" : "LP",
#     "genre" : "R&b/Soul",
#     "song" : {"name" : "Save Your Tears", "link" : "save-your-tears"}
#     },

#     "Love Scars: The 5 Stages of Emotions": {
#     "name" : "Love Scars: The 5 Stages of Emotions",
#     "release" : "2020/10/02",
#     "artist" : {"name" : "Yung Bleu", "link" : "yung-bleu"},
#     "type" : "EP",
#     "genre" : "R&b",
#     "song" : {"name" : "You're Mines Still", "link" : "youre-mines-still"}
#     }
# }

# Part of the lecture video but we are not using it currently.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  return render_template("index.html")


@app.route("/api/test")
def test():
      return "TEST123456789"


# Index render that we did but commented because it's differnt from lecture video
#
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/albums/')
def albums():
    return render_template('albums.html')

@app.route('/artists/')
def artists():
    return render_template('artists.html')

@app.route('/songs/')
def songs():
    return render_template('songs.html')

# Static instances of the different pages
@app.route('/songs/song1/')
def song1():
    return render_template('./static_pages/song1.html', songs = song_list)

@app.route('/songs/song2/')
def song2():
    return render_template('./static_pages/song2.html', songs = song_list)

@app.route('/songs/song3/')
def song3():
    return render_template('./static_pages/song3.html', songs = song_list)

@app.route('/albums/album1/')
def album1():
    return render_template('./static_pages/album1.html', albums = album_list)

@app.route('/albums/album2/')
def album2():
    return render_template('./static_pages/album2.html', albums = album_list)

@app.route('/albums/album3/')
def album3():
    return render_template('./static_pages/album3.html', albums = album_list)

@app.route('/artists/artist1/')
def artist1():
    return render_template('./static_pages/artist1.html', artists = artist_list)

@app.route('/artists/artist2/')
def artist2():
    return render_template('./static_pages/artist2.html', artists = artist_list)

@app.route('/artists/artist3/')
def artist3():
    return render_template('./static_pages/artist3.html', artists = artist_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
    # app.run()
