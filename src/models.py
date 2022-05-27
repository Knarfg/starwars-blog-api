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


class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    planets_id = db.Column(db.Integer, db.ForeignKey("Planets.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
    

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_planets = db.relationship('FavoritePlanets', lazy=True)


class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    people_id = db.Column(db.Integer, db.ForeignKey("People.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
    

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_people = db.relationship('FavoritePeople', lazy=True)