"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
import random
#from models import Person

api = Blueprint('api', __name__)


@api.route('/excuse', methods=['POST', 'GET'])
def get_excuse():
    who = ["the dog", "My brother", "A nail"]
    action = ["ate", "ripped", "slashed"]
    what = ["my homework", "my rent check", "my tire"]
    when = ["yesterday", "two days ago", "when I was on my way to work"]
    excuse = who[random.randint(0,2)] + " " + action[random.randint(0,2)] + " " + what[random.randint(0,2)] + " " + when[random.randint(0,2)]
   
    return jsonify(excuse), 200