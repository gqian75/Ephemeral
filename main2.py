from flask import render_template
from create_db import app, db, Song, create_songs


@app.route('/')
def index():
	return render_template('hello.html')

# ------------
# song
# ------------	
@app.route('/songs/')
def song():
	book_list = db.session.query(Song).all()
	return render_template('books.html', book_list = book_list)

# ------------
# book
# ------------	
@app.route('/books/')
def book():
	book_list = db.session.query(Book).all()
	return render_template('books.html', book_list = book_list)

# debug=True activates the automatic reloader. Therefore, if you use it, make sure to add "db.drop_all()"
# right before "db.create_all()" in "models.py".
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
