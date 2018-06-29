from app.models import db
from flask import Blueprint

admin = Blueprint('api_admin', __name__)

@admin.route('/')
def index():
  return "Everyone's an admin!"

@admin.route('/create_database')
def create_database():
  db.drop_all()
  db.create_all()
  return "OK"
