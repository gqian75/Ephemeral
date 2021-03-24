#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/main.py
# Fares Fraij
# ---------------------------

from flask import render_template
from create_db import app, db, Book, create_books

#books = [{'title': 'Software Engineering', 'id': '1'}, {'title':'Algorithm Design', 'id':'2'},{'title':'Python', 'id':'3'}]

# ------------
# index
# ------------
@app.route('/')
def index():
	return render_template('hello.html')

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
