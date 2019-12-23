import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from day import Day

application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
CORS(application)

@application.route('/')
def get_day():
    date = request.args.get('date')

    day = Day(
        date = date,
        breakfast = "breakfast",
        lunch = "lunch",
        dinner = "dinner",
        rating = 4,
        notes = "notes")

    db.session.add(day)
    db.session.commit()

    return jsonify(date=date)

@application.route('/health')
def get_health():

    return jsonify(message="ok")

@application.route("/getall")
def get_all():
    try:
        days=Day.query.all()

        return  jsonify([e.serialize() for e in days])
    except Exception as e:
	    return(str(e))
