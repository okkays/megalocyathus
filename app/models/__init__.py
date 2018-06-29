# Set up the DB
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Load model classes
from . import service
