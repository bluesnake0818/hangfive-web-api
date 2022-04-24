from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.visitor import Visitor

visitors = Blueprint('visitors', 'visitors')


@visitors.route('/', methods=["POST"])
# @login_required
def create():
  data = request.get_json()
  # profile = read_token(request)
  # data["profile_id"] = profile["id"]
  visitor = Visitor(**data)
  db.session.add(visitor)
  db.session.commit()
  return jsonify(visitor.serialize()), 201