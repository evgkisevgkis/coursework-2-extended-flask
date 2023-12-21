from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    """Model for directors"""
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)


class DirectorSchema(Schema):
    """Schema for directors"""

    id = fields.Int(dump_only=True)
    name = fields.Str()
