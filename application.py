from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
CORS(application)

@application.route('/')
def get_day():
    date = request.args.get('date')

    return jsonify(date=date)

@application.route('/health')
def get_health():

    return jsonify(message="ok")

if __name__ == '__main__':
    application.run()