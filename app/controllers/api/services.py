from flask import Blueprint, request, jsonify, make_response, abort
from app.errors import *
from app.models.service import Service
from app.models import db
from app.controllers.api import base

services = Blueprint('api_services', __name__)

@services.route('/', methods=['GET'])
def index():
  return base.index(Service)

@services.route('/<int:sid>', methods=['GET'])
def get_service(sid):
  return base.get(Service, sid)

@services.route('/', methods=['POST'])
def add_service():
  return base.add(Service, request.get_json())

@services.route('/<int:sid>', methods=['PATCH'])
def update_service(sid):
  return base.update(Service, sid, request.get_json())
