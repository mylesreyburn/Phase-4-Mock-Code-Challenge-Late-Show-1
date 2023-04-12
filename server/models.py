from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    serialize_rules = ("-appearances.episode",)

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    appearances = db.relationship('Appearance', backref='game')


class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    serialize_rules = ("-appearances.guest",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    appearances = db.relationship("Appearance", backref = "episode")

class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    serialize_rules = ("-guest.appearances", "-episode.appearances",)

    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"))
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())