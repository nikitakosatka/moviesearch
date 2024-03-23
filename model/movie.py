from sqlalchemy import inspect
from sqlalchemy.orm import validates

from app import app
from base import db
from exception import RatingValidationException, YearValidationException


class Movie(db.Model):
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    director = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    length = db.Column(db.String(12), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    @validates("rating")
    def validate_rating(self, key, value):
        if value > 10 or value < 0:
            raise RatingValidationException()
        if value is None:
            return 0
        return value

    @validates("year")
    def validate_year(self, key, value):
        if value > 2100 or value < 1900:
            raise YearValidationException()
        if value is None:
            return 0
        return value

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return f"{self.id}"


with app.app_context():
    db.create_all()
