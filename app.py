from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_day():
    date = request.args.get('date')

    return jsonify(date=date)

if __name__ == '__main__':
    app.run()