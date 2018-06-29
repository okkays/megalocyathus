import json

from app.models import db

class Encodable(object):
  def jsonify(self):
    raise NotImplementedError()

class Encoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Encodable):
      return obj.jsonify()
    return json.JSONEncoder.default(self, obj)

