from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token
from api.middleware.calc_bchart_script import main

from api.models.db import db
from api.models.visitor import Visitor


visitors = Blueprint('visitors', 'visitors')


@visitors.route('/', methods=["POST"])
# @login_required
def create():
  data = request.get_json()
  # profile = read_token(request)
  # data["profile_id"] = profile["id"]
  data["d_zodiac"] = main(data["bday"])
  visitor = Visitor(**data)
  db.session.add(visitor)
  db.session.commit()
  return jsonify(visitor.serialize()), 201


@visitors.route('/', methods=["GET"])
def index():
  visitors = Visitor.query.all()
  return jsonify([visitor.serialize() for visitor in visitors]), 200


@visitors.route('/<id>', methods=["GET"])
def show(id):
  visitor = Visitor.query.filter_by(id=id).first()
  visitor_data = visitor.serialize()
  return jsonify(visitor=visitor_data), 200

@visitors.route('/<id>', methods=["PUT"]) 
# @login_required
def update(id):
  data = request.get_json()
  # profile = read_token(request)
  visitor = Visitor.query.filter_by(id=id).first()

  # if visitor.profile_id != profile["id"]:
  #   return 'Forbidden', 403

  for key in data:
    setattr(visitor, key, data[key])

  db.session.commit()
  return jsonify(visitor.serialize()), 200

@visitors.route('/<id>', methods=["DELETE"]) 
# @login_required
def delete(id):
  # profile = read_token(request)
  visitor = Visitor.query.filter_by(id=id).first()

  # if visitor.profile_id != profile["id"]:
  #   return 'Forbidden', 403

  db.session.delete(visitor)
  db.session.commit()
  return jsonify(message="Success"), 200
