import os
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/static", template_folder="./frontend/templates")
CORS(app)




artist_list = { "Olivia Rodrigo" : {
    "name" : "Olivia Rodrigo",
    "Genre" : "Pop",
    "Age" : 18,
    "Label" : "Interscope",
    "Top Song" : {"name" : "driver's license", "link" : "drivers-license"},
    "Albums" : [{"name" : "driver's license", "link" : "drivers-license"}]
    },

    "The Weeknd" : {
    "name" : "The Weeknd",
    "Genre" : "R&b/Soul",
    "Age" : 31,
    "Label" : "XO",
    "Top Song" : {"name" : "Save Your Tears", "link" : "save-your-tears"},
    "Albums" : [{"name" : "After Hours", "link" : "after-hours"}]
    },

    "Yung Bleu" : {
    "name" : "Yung Bleu",
    "Genre" : "Rap",
    "Age" : 26,
    "Label" : "Various",
    "Top Song" : {"name" : "You're Mines Still", "link" : "youre-mines-still"},
    "Albums" : [{"name" : "Love Scars: The 5 Stages of Emotions", "link" : "love-scars-the-5-stages-of-emotions"}]
    }
}

song_list = { "driver's license" : {
    "name" : "driver's license",
    "artist" : {"name" : "Olivia Rodrigo", "link" : "olivia-rodrigo"},
    "album" : {"name" : "driver's license", "link" : "drivers-license"},
    "release date" : "2021/01/08",
    "song length" : "4:02"
    },

    "Save Your Tears" : {
    "name" : "Save Your Tears",
    "artist" : {"name" : "The Weeknd", "link" : "the-weeknd"},
    "album" : {"name" : "After Hours", "link" : "after-hours"},
    "release date" : "2020/08/09",
    "song length" : "6:01"
    },

    "You're Mines Still" : {
    "name" : "You're Mines Still",
    "artist" : {"name" : "Yung Bleu", "link" : "yung-bleu"},
    "album" : {"name" : "Love Scars: The 5 Stages of Emotions", "link" : "love-scars-the-5-stages-of-emotions"},
    "release date" : "2020/10/02",
    "song length" : "3:46"
    },

}
album_list = { "drivers license": {
    "name" : "drivers license",
    "release date" : "2021/01/08",
    "artist" : {"name" : "Olivia Rodrigo", "link" : "olivia-rodrigo"},
    "type" : "Single",
    "genre" : "Pop",
    "songs" : [{"name" : "driver's license", "link" : "drivers-license"}]
    },

    "After Hours": {
    "name" : "After Hours",
    "release date" : "2020/03/20",
    "artist" : {"name" : "The Weeknd", "link" : "the-weeknd"},
    "type" : "LP",
    "genre" : "R&b/Soul",
    "songs" : [{"name" : "Save Your Tears", "link" : "save-your-tears"}]
    },

    "Love Scars: The 5 Stages of Emotions": {
    "name" : "Love Scars: The 5 Stages of Emotions",
    "release date" : "2020/10/02",
    "artist" : {"name" : "Yung Bleu", "link" : "yung-bleu"},
    "type" : "EP",
    "genre" : "R&b",
    "songs" : [{"name" : "You're Mines Still", "link" : "youre-mines-still"}]
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
    return render_template('albums.html')

@app.route('/artists/')
def artists():
    return render_template('artists.html')

@app.route('/songs/')
def songs():
    return render_template('songs.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
    #app.run()