#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from models import db, Location, Event, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nuekid.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)
CORS(app)

# CORS(app)

api = Api(app)

bcrypt = Bcrypt(app)

def get_current_user():
    return User.query.where( User.id == session.get("user_id") ).first()

def logged_in():
    return bool( get_current_user() )

class Locations(Resource):

    def get(self):
        locations = Location.query.all()

        response_body = []

        for location in locations:
            response_body.append(location.to_dict())

        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            new_location = Location(name=request.get_json().get('name'), address=request.get_json().get('address'))
            db.session.add(new_location)
            db.session.commit()

            response_body = new_location.to_dict()
            
            return make_response(jsonify(response_body), 201)
        except ValueError as error:
            response_body = {
                "error": error.args
            }
            return make_response(jsonify(response_body), 422)


api.add_resource(Locations, '/locations')

class LocationById(Resource):

    def get(self, id):
        location = Location.query.filter(Location.id == id).first()

        if not location:
            response_body = {
                "error": "Location not found"
            }
            status = 404

        else:
            response_body = location.to_dict()


        return make_response(jsonify(response_body), 200)
    
    def patch(self, id):
        location = Location.query.filter(Location.id == id).first()

        if not location:
            response_body = {
                "error": "Location not found"
            }
            return make_response(jsonify(response_body), 404)

        else:
            try:
                json_data = request.get_json()
                for key in json_data:
                    setattr(location, key, json_data.get(key))
                db.session.commit()

                response_body = location.to_dict()
                return make_response(jsonify(response_body), 200)
            
            except ValueError as error:
                
                response_body = {
                    "error": error.args
                }
                
                return make_response(jsonify(response_body), 422)
    
    def delete(self, id):
        location = Location.query.filter(Location.id == id).first()

        if not location:
            response_body = {
                "error": "Location not found"
            }
            status = 404

        else:
            db.session.delete(location)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)


api.add_resource(LocationById, '/locations/<int:id>')

class Events(Resource):

    def get(self):
        events = Event.query.all()
        response_body = []
        for event in events:
            event.location_name = event.location.name
            response_body.append(event.to_dict(rules=("location.name", "date.day", "date.time")))
        
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            new_event = Event(
                title=request.get_json().get('title'), 
                description=request.get_json().get('description'), 
                event_type=request.get_json().get('event_type'), 
                people_needed=request.get_json().get('people_needed'),
                space_available=request.get_json().get('people_needed'),
                location_id=request.get_json().get('location_id'),
                date_id=request.get_json().get('date_id'),
                user_id=request.get_json().get('user_id')
                )
            


            db.session.add(new_event)
            db.session.commit()

            response_body = new_event.to_dict()
            response_body.update({
                "location": new_event.location.to_dict(),
                "date": new_event.date.to_dict()

            })
            
            return make_response(jsonify(response_body), 201)
        except ValueError as error:
            response_body = {
                "error": error.args
            }
            return make_response(jsonify(response_body), 422)

api.add_resource(Events, '/events')

class EventById(Resource):

    def get(self, id):
        event = Event.query.filter(Event.id == id).first()

        if not event:
            response_body = {
                "error": "event not found"
            }
            status = 404
        else:
            # location_list = []
            # for location in location_list(set(event.locations)):
            #     location_list.append({
            #         "id": location.id,
            #         "name": location.name,
            #         "address": location.address,
            #         "lat": location.lat,
            #         "long":location.long,
            #         "img": location.img
            #     })
            # response_body.update({"customers": customer_list})
            # status = 200
            response_body = event.to_dict()
            status = 200
        return make_response(jsonify(response_body), status)
    
    def patch(self, id):
        event = Event.query.filter(Event.id == id).first()

        if not event:
            response_body = {
                "error": "Event not found"
            }
            return make_response(jsonify(response_body), 404)
        else:
            try:
                json_data = request.get_json()
                
                for key in json_data:
                    setattr(event, key, json_data.get(key))

                db.session.commit()

                response_body = event.to_dict()

                return make_response(jsonify(response_body), 200)
            except ValueError as error:
                response_body = {
                    "error": error.args
                }
                return make_response(jsonify(response_body), 422)
    
    def delete(self, id):
        event = Event.query.filter(Event.id == id).first()
        
        if not event:

            response_body = {
                "error": "Event not found"
            }
            status = 404
        
        else:
            
            db.session.delete(event)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(EventById, '/events/<int:id>')

class Users(Resource):

    def get(self):
        users = User.query.all()

        response_body = []

        for user in users:
            response_body.append(user.to_dict())

        return make_response(jsonify(response_body), 200)
    
    def post(self):
        json_data = request.get_json()

        new_user = User(
            username=json_data.get('username'), 
            password_hash=json_data.get('password'), 
            first_name=json_data.get('first_name'),
            last_name=json_data.get('last_name'),
            address=json_data.get('address'),
            age = json_data.get('age'), 
            )
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id

        response_body = new_user.to_dict()
        
        return make_response(jsonify(response_body), 201)
    
api.add_resource(Users, '/users')

class UserById(Resource):

    def get(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            response_body = {
                "error": "User not found"
            }
            status = 404
        else:
            response_body = user.to_dict()
            status = 200

        return make_response(jsonify(response_body), 200)
    
    def patch(self, id):
        user = User.query.filter(User.id == id).first()

        if not user:
            response_body = {
                "error": "User not found"
            }
            status = 404
        else:
            json_data = request.get_json()

            for key in json_data:
                setattr(user, key, json_data.get(key))

            db.session.commit()

            response_body = user.to_dict()
            status = 200

        return make_response(jsonify(response_body), status)
    
    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        
        if not user:

            response_body = {
                "error": "User not found"
            }
            status = 404
        
        else:
            
            db.session.delete(user)
            db.session.commit()

            response_body = {}
            status = 204

        return make_response(jsonify(response_body), status)

api.add_resource(UserById, '/users/<int:id>')

class Login(Resource):
    def post(self):
        user = User.query.filter(User.username == request.json.get('username')).first()

        if not user:
            response_body = {
                "error": "Invalid username"
            }
            status = 401

        else:
            session['user_id'] = user.id
            response_body = user.to_dict()
            status = 201

        return make_response(jsonify(response_body), status)

api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return {}, 204
        return {'error': '401 Unauthorized'}, 401

api.add_resource(Logout, '/logout')


class CurrentSession(Resource):
    def get(self):
        if session.get('user_id'):

            user = User.query.filter(User.id == session['user_id']).first()
            return make_response(jsonify(user.to_dict()), 200)

        return {'error': '401 Unauthorized'}, 401

api.add_resource(CurrentSession, '/current_session')

if __name__ == '__main__':
    app.run(port=7000, debug=True)