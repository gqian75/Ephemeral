from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

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
    app.debug = True
    app.run()
