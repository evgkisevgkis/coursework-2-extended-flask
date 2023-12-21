from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    """Model for genres"""
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)


class GenreSchema(Schema):
    """Schema for genres"""

    id = fields.Int(dump_only=True)
    name = fields.Str()
