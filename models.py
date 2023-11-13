from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Event(db.Model, SerializerMixin):
    __tablename__ = "events"

    serialize_only = ('id', 'title', 'description', 'event_type', 'people_needed', 'space_available', 'location_id', 'date_id')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    event_type = db.Column(db.String)
    people_needed = db.Column(db.Integer)
    space_available = db.Column(db.Integer)

    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # location = db.relationship('Location', back_populates="events")
    
    

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "title": self.title,
    #         "description": self.description,
    #         "event_type": self.event_type,
    #         "people_needed": self.people_needed,
    #         "space_available": self.space_available,
    #         "location_id": self.location_id,
    #     }

 

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password_hash = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    age = db.Column(db.Integer)

    events = db.relationship('Event', backref='user')

    def to_dict(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "address" : self.address,
            "age" : self.age
        }

    @validates('address')
    def validate_day(self, key, address):
        if not address:
            raise ValueError
        else:
            return address
    
  

class Location(db.Model, SerializerMixin):
    __tablename__ = 'locations'

    serialize_rules = ('name', 'address', 'lat', 'long', 'img', 'events', 'location_type')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    lat = db.Column(db.String)
    long = db.Column(db.Integer)
    img = db.Column(db.String)
    location_type = db.Column(db.String)

    events = db.relationship('Event', backref="location")
    

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'address' : self.address,
            'lat' : self.lat,
            'long' : self.long,
            'img' : self.img,
            'location_type' : self.location_type,
            'events': [event.to_dict() for event in self.events]
        }



class Date(db.Model, SerializerMixin):
    __tablename__ = 'dates'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String)
    day = db.Column(db.String)

    # event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    # user_id = db.Column(db.Intger, db.ForeignKey('users.id'))

    events = db.relationship('Event', backref='date')
    # user = db.relationship('User', backref="dates")

    def to_dict(self):
        return {
            "id": self.id,
            "time": self.time,
            "day": self.day
        }

    @validates('day')
    def validate_day(self, key, day):
        if not day:
            raise ValueError
        else:
            return day