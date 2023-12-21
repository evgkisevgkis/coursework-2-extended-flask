from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    """Model for movies"""
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))  # reference to genres table
    genre = db.relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))  # reference to directors table
    director = db.relationship('Directors')


class MovieSchema(Schema):
    """Schema for movies"""

    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
