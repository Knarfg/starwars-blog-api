from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planets = db.relationship('FavoritePlanets', lazy=True)
    favorite_people = db.relationship('FavoritePeople', lazy=True)

    def __repr__(self):
        return f'El user es {self.email}'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_planets = db.relationship('FavoritePlanets', lazy=True)
    diameter = db.Column(db.String(120), nullable=False)
    rotation_period = db.Column(db.String(120), nullable=False)
    orbital_period = db.Column(db.String(120), nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(120), nullable=False)
    surface_water = db.Column(db.String(120), nullable=False)
    created = db.Column(db.String(120), nullable=False)
    edited = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    _id = db.Column(db.String(120), nullable=True)
    uid = db.Column(db.String(120), nullable=True)


    def __init__(self, diameter, rotation_period, orbital_period,
                 gravity, population, climate, terrain,
                 surface_water, created, edited, name, url,
                 description=None, _id=None, uid=None):
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.created = created
        self.edited = edited
        self.name = name
        self.url = url
        self.description = description
        self._id = _id
        self.uid = uid


# {
#     "properties": {
#         "diameter": "10200",
#         "rotation_period": "24",
#         "orbital_period": "4818",
#         "gravity": "1 standard",
#         "population": "1000",
#         "climate": "temperate, tropical",
#         "terrain": "jungle, rainforests",
#         "surface_water": "8",
#         "created": "2022-05-28T05:31:07.852Z",
#         "edited": "2022-05-28T05:31:07.852Z",
#         "name": "Yavin IV",
#         "url": "https://www.swapi.tech/api/planets/3"
#     },
#     "description": "A planet.",
#     "_id": "5f7254c11b7dfa00041c6fb0",
#     "uid": "3",
#     "__v": 0
# }


class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
    

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_people = db.relationship('FavoritePeople', lazy=True)


class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
    

