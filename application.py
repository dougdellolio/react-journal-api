import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
db = SQLAlchemy(application)

from models import Day

application.config.from_object(os.environ['APP_SETTINGS'])
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(application)

@application.route('/add', methods=['POST'])
def add_day():

    date = request.json['date']
    breakfast = request.json['breakfast']
    lunch = request.json['lunch']
    dinner = request.json['dinner']
    rating = request.json['rating']
    gym = request.json['gym']
    notes = request.json['notes']

    day = Day(
        date = date,
        breakfast = breakfast,
        lunch = lunch,
        dinner = dinner, 
        rating = rating,
        notes = notes,
        gym = gym)

    db.session.add(day)
    db.session.commit()

    return "Added details for date={}".format(day.Date)

@application.route('/health')
def get_health():

    return jsonify(message="ok")

@application.route("/day/<date>", methods=['GET'])
def get_day(date):
    try:
        day = Day.query.filter_by(date=date).first()

        if day == None:
            return jsonify([])

        return  jsonify(day.serialize())
    except Exception as e:
	    return(str(e))
