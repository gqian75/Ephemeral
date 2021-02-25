import os
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/build/static", template_folder="./frontend/build")
CORS(app)


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
    # app.run()