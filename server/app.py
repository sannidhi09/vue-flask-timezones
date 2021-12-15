from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
import pytz

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/timezones', methods=['GET'])
def get_timezones():
    print("Hello")
    timezones = []
    for timezone in pytz.all_timezones_set:
        timezones.append(timezone)
    return jsonify({'timezones': timezones})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)