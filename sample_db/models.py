#!/usr/bin/env python3

# ---------------------------
# projects/IDB3/models.py
# Fares Fraij
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING", 'postgres://postgres:jake@localhost:5432/bookdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # to suppress a warning message
db = SQLAlchemy(app)


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

    title = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)


db.drop_all()
db.create_all()
