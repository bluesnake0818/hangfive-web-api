from datetime import datetime
from api.models.db import db

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    bday = db.Column(db.DateTime, nullable=False)
    d_zodiac = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
      return f"Visitor('{self.id}', '{self.email}'"

    def serialize(self):
      visitor = {c.email: getattr(self, c.email) for c in self.__table__.columns}
      return visitor