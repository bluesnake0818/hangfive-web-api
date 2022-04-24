from datetime import datetime
from api.models.db import db

class Visitor(db.Model):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    bday = db.Column(db.String(100))
    d_zodiac = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
      return f"Visitor('{self.id}', '{self.email}'"

    def serialize(self):
      visitor = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return visitor

    # def serialize(self):
    #   return {
    #     "id": self.id,
    #     "email": self.email,
    #     "bday": self.bday.date.strftime('%Y-%m-%d'),
    #     "d_zodiac": self.d_zodiac,
    #   }
    
    # Refactored serialize method:
    # def serialize(self):
    #   visitor = {c.email: getattr(self, c.email) for c in self.__table__.columns}
    #   feedings = [feeding.serialize() for feeding in self.feedings] 
    #   toys = [toy.serialize() for toy in self.toys]
    #   cat['feedings'] = feedings
    #   cat['toys'] = toys
    #   return cat

    # def serialize(self):
    #   visitor = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #   return visitor