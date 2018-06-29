import re
import urllib

from sqlalchemy.orm import validates

from app.models import db
from app.util.encodable import Encodable

class Service(db.Model, Encodable):
  """Represents a web services that mega can redirect to."""
  singular = 'service'
  plural = 'services'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  url = db.Column(db.String, nullable=False)

  @validates("name")
  def validate_name(self, key, name):
    if name == "__":
      raise AssertionError("__ is reserved")
    if '/' in name:
      raise AssertionError("names can't contain '/'")
    quoted = urllib.quote(name)
    if quoted != name:
      raise AssertionError("names must be url-safe (e.g. {})".format(quoted))
    return name

  def jsonify(self):
    return {
        "id": self.id,
        "name": self.name,
        "url": self.url,
    }
