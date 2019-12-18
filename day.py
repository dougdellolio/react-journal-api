from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Day(db.Model):
    id = db.Column(db.Date, primary_key=True)
    breakfast = db.Column(db.String(80), unique=False, nullable=False)
    lunch = db.Column(db.String(120), unique=False, nullable=False)
    dinner = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    notes = db.Column(db.String(max), unique=False, nullable=True)

    # def __repr__(self):
    #     return '<User %r>' % self.username