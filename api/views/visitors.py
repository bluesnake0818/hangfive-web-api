import requests
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token
from api.middleware.calc_bchart_script import main

from api.models.db import db
from api.models.visitor import Visitor
from config import API_URL, API_KEY

visitors = Blueprint('visitors', 'visitors')


@visitors.route('/', methods=["POST"])
# @login_required
def create():
  data = request.get_json()
  # profile = read_token(request)
  # data["profile_id"] = profile["id"]

  # TODO: 프론트에서 넘어온 data['bday'] 를 19870625 로 변환 필요
  date = data["bday"]
  # ex)
  date = "19870625"
  header = {'x-api-key': API_KEY}
  response = requests.get(f'{API_URL}hangfive-web/birthchart', params={'date': date}, headers=header)

  data["d_zodiac"] = response.json()
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
