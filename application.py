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

    return jsonify(success=True)

@application.route('/day', methods=['PUT'])
def update_day():

    date = request.json['date']

    day = Day.query.filter_by(date=date).first()
    day.breakfast = request.json['breakfast']
    day.lunch = request.json['lunch']
    day.dinner = request.json['dinner']
    day.rating = request.json['rating']
    day.gym = request.json['gym']
    day.notes = request.json['notes']

    db.session.commit()

    return jsonify(success=True)

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

@application.route("/days", methods=['GET'])
def get_all_days():
    try:
        all_days = Day.query.all()

        return jsonify([day.serialize() for day in all_days])
    except Exception as e:
        return (str(e))
