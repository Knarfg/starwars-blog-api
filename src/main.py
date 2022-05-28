"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets
# from models import db, User, Planets, FavoritePlanets, People, FavoritePeople
#from models import Person
# import urllib.request, json
import requests
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    users = User.query.all()
    users_serialize = list(map(lambda user: user.serialize(), users))

    response_body = {
        "msg": "Hello, this is your GET /users response ",
        "results": users_serialize
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def handle_people():
    response = requests.get("https://www.swapi.tech/api/people")
    return response.json(), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def handle_one_people(people_id):
    response = requests.get(f"https://www.swapi.tech/api/people/{people_id}")
    return response.json(), 200


@app.route('/planets', methods=['GET'])
def handle_planets():
    response = requests.get("https://www.swapi.tech/api/planets")
    response_decoded = response.json()
    planets = Planets.query.all()
    if len(planets) == 0:
        for planet in response_decoded["results"]:
            response_one_planet = requests.get(planet["url"])
            response_one_planet_decoded = response_one_planet.json()
            response_one_planet_decoded["result"] 
            one_planet = Planets(**response_one_planet_decoded["result"]["properties"])
            db.session.add(one_planet)
        db.session.commit()

    return response_decoded, 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_one_planet(planet_id):
    response = requests.get(f"https://www.swapi.tech/api/planets/{planet_id}")
    return response.json(), 200


@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def favorite_planet(planet_id):
    user = User.query.filter_by(is_active=True)
    planet = Planets.query.all()
    print(user[0], planet[0])
    return "Holax", 200
    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
