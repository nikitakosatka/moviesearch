from sqlalchemy import inspect

from app import app
from base import db


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    fio = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return f"{self.id}"


with app.app_context():
    db.create_all()
