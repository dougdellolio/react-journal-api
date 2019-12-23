from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Day(db.Model):

    __tablename__ = 'Days'

    date = db.Column(db.Date, primary_key=True)
    breakfast = db.Column(db.String(80), unique=False, nullable=False)
    lunch = db.Column(db.String(120), unique=False, nullable=False)
    dinner = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    notes = db.Column(db.String(max), unique=False, nullable=True)

    def __init__(self, date, breakfast, lunch, dinner, rating, notes):
        self.date = date
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.rating = rating
        self.notes = notes

    def __repr__(self):
        return '<Date {}>'.format(self.Date)

    def serialize(self):
        return {
            'date': self.date,
            'breakfast': self.breakfast,
            'lunch': self.lunch,
            'dinner': self.dinner,
            'rating': self.rating,
            'notes': self.notes
        }
