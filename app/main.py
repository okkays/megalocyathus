import os

from flask import Flask

from app.controllers import api, frontend
from app.models import db
from app.util.encodable import Encoder

# Setup app
app = Flask(__name__)
app.json_encoder = Encoder

app.url_map.strict_slashes = False

app.config['DATABASE'] = os.environ['DATABASE']

# DB Settings
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE']
print("Using database {}".format(app.config['SQLALCHEMY_DATABASE_URI']))

db.init_app(app)

# Blueprints - Api
app.register_blueprint(api.admin, url_prefix='/__/api/admin')
app.register_blueprint(api.services, url_prefix='/__/api/services')

# Blueprints - Frontend
app.register_blueprint(frontend.home, url_prefix='/')
app.register_blueprint(frontend.services, url_prefix='/__/services')
