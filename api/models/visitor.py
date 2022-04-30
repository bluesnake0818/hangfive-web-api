from datetime import datetime
from api.models.db import db

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    bday = db.Column(db.DateTime)
    d_zodiac = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
      return f"Visitor('{self.id}', '{self.email}'"

    def serialize(self):
      visitor = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return visitor


