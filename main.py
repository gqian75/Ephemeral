import os
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/static", template_folder="./frontend/templates")
CORS(app)




artist_list = { "olivia-rodrigo" : {
    "name" : "Olivia Rodrigo",
    "id" : "olivia-rodrigo",
    "genre" : "Pop",
    "age" : 18,
    "label" : "Interscope",
    "song" : {"name" : "driver's license", "link" : "drivers-license"},
    "albums" : {"name" : "driver's license", "link" : "drivers-license"}
    },

    "the-weeknd" : {
    "name" : "The Weeknd",
    "id": "the-weeknd",
    "genre" : "R&b/Soul",
    "age" : 31,
    "label" : "XO",
    "song" : {"name" : "Save Your Tears", "link" : "save-your-tears"},
    "albums" : {"name" : "After Hours", "link" : "after-hours"}
    },

    "yung-bleu" : {
    "name" : "Yung Bleu",
    "id": "yung-bleu",
    "genre" : "Rap",
    "age" : 26,
    "label" : "Various",
    "song" : {"name" : "You're Mines Still", "link" : "youre-mines-still"},
    "albums" : {"name" : "Love Scars: The 5 Stages of Emotions", "link" : "love-scars-the-5-stages-of-emotions"}
    }
}

song_list = { "drivers-license" : {
    "name" : "driver's license",
    "id": "drivers-license",
    "artist" : {"name" : "Olivia Rodrigo", "link" : "olivia-rodrigo"},
    "album" : {"name" : "driver's license", "link" : "drivers-license"},
    "release" : "2021/01/08",
    "length" : "4:02"
    },

    "save-your-tears" : {
    "name" : "Save Your Tears",
    "id" : "save-your-tears",
    "artist" : {"name" : "The Weeknd", "link" : "the-weeknd"},
    "album" : {"name" : "After Hours", "link" : "after-hours"},
    "release" : "2020/08/09",
    "length" : "6:01"
    },

    "youre-mines-still" : {
    "name" : "You're Mines Still",
    "id" : "youre-mines-still",
    "artist" : {"name" : "Yung Bleu", "link" : "yung-bleu"},
    "album" : {"name" : "Love Scars: The 5 Stages of Emotions", "link" : "love-scars-the-5-stages-of-emotions"},
    "release" : "2020/10/02",
    "length" : "3:46"
    },

}
album_list = { "drivers-license": {
    "name" : "Driver's License",
    "id" : "drivers-license",
    "release" : "2021/01/08",
    "artist" : {"name" : "Olivia Rodrigo", "link" : "olivia-rodrigo"},
    "type" : "Single",
    "genre" : "Pop",
    "song" : {"name" : "driver's license", "link" : "drivers-license"}
    },

    "after-hours": {
    "name" : "After Hours",
    "id": "after-hours",
    "release" : "2020/03/20",
    "artist" : {"name" : "The Weeknd", "link" : "the-weeknd"},
    "type" : "LP",
    "genre" : "R&b/Soul",
    "song" : {"name" : "Save Your Tears", "link" : "save-your-tears"}
    },

    "love-scars-the-5-stages-of-emotions": {
    "name" : "Love Scars: The 5 Stages of Emotions",
    "id" : "love-scars-the-5-stages-of-emotions",
    "release" : "2020/10/02",
    "artist" : {"name" : "Yung Bleu", "link" : "yung-bleu"},
    "type" : "EP",
    "genre" : "R&b",
    "song" : {"name" : "You're Mines Still", "link" : "youre-mines-still"}
    }
}



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
    return render_template('albums.html',albums=album_list)

@app.route('/artists/')
def artists():
    return render_template('artists.html',artists=artist_list)

@app.route('/songs/')
def songs():
    return render_template('songs.html',songs=song_list)

#Dynamic instances of different types
def id(string):
    string = string.replace(" ","-").lower()
    string = string.replace("'","")
    return string


@app.route('/albums/<string:_album>')
def album(_album):
    #_album = id(_album)
    return render_template('album.html', album=album_list.get(_album,None))

@app.route('/artists/<string:_artist>')
def artist(_artist):
    _artist = id(_artist)
    return render_template('artist.html', artist=artist_list.get(_artist,None))

@app.route('/songs/<string:_song>')
def song(_song):
    _song = id(_song)
    return render_template('song.html', song=song_list.get(_song,None))


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
    #app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
    app.run(debug=True)
