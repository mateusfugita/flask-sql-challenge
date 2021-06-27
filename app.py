import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

from controllers import buyer_controller, address_city_controller, address_state_controller

#buyers
@app.route('/buyers', methods=['POST'])
def createBuyer():
    body = request.get_json()
    response = buyer_controller.create(body)
    return response

@app.route('/buyers/<id>', methods=['GET'])
def getBuyer(id):
    response = buyer_controller.selectOne(id)
    return response

#address_cities
@app.route('/city', methods=['POST'])
def createCity():
    body = request.get_json()
    response = address_city_controller.create(body)
    return response

#address_states
@app.route('/states', methods=['POST'])
def createState():
    body = request.get_json()
    response = address_state_controller.create(body)
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
