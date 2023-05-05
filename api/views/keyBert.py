import requests
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token
from api.middleware.calc_bchart_script import main

from api.models.db import db
from api.models.visitor import Visitor
from config import API_URL, API_KEY

from keybert import KeyBERT

keybert = Blueprint('keybert', 'keybert')

@keybert.route('/', methods=["POST"])
def createKeywords():
  doc = request.get_json()
  kw_model = KeyBERT()
  keywords = kw_model.extract_keywords(doc)

  print(keywords)
  return jsonify(keywords), 201
  # return doc