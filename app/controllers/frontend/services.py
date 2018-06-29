from flask import Blueprint, render_template

services = Blueprint('services', __name__)

@services.route('/')
def index():
  return render_template('services/index.jinja')
