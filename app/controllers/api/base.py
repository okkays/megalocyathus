from flask import jsonify
from app.errors import *
from app.models import db

def index(Thing):
  return jsonify(Thing.query.all())

def do_get(Thing, tid):
  thing = Thing.query.get(tid)
  if thing is None:
    return 'No {} with id: {}'.format(Thing.singular, tid), 404
  return thing

def get(Thing, tid):
  thing = do_get(Thing, tid)
  return jsonify(thing)

def add(Thing, attrs):
  try:
    thing = Thing(**attrs)
  except TypeError as e:
    if 'is an invalid keyword argument for' in str(e):
      return 'Problem creating {}: {}'.format(Thing.singular, e), 400
    raise e
  except AssertionError as e:
    return 'Validation failed for {}: {}'.format(Thing.singular, e), 400
  db.session.add(thing)
  db.session.commit()
  return str(thing.id)

def update(Thing, tid, attrs):
  thing = do_get(Thing, tid)
  if not attrs:
    return "Must specify something to change", 400
  for attr, value in attrs.items():
    if not hasattr(thing, attr):
      return "{} has not attribute {}".format(thing, attr), 400
    try:
      setattr(thing, attr, value)
    except Exception as e:
      return "Problem updating {} {}: {}".format(Thing.singular, tid, e), 400
  db.session.add(thing)
  db.session.commit()
  return str(thing.id)

def associate_append(A, B, aid, bid):
  """Appends a B to A[B.plural]"""
  a = do_get(A, aid)
  b = do_get(B, bid)
  getattr(a, B.plural).append(b)
  db.session.add(a)
  db.session.commit()
  return "Added {} {} to {} {}".format(A.singular, aid, B.singular, bid)

def associate_remove(A, B, aid, bid):
  """Removes a B from A[B.plural]"""
  a = do_get(A, aid)
  b = do_get(B, bid)
  bs = getattr(a, B.plural)
  if b not in bs:
    return "The {} {} does not have a {} {}".format(A.singular, aid, B.singular, bid), 404
  bs.remove(b)
  db.session.add(a)
  db.session.commit()
  return "Removed {} {} from {} {}".format(A.singular, aid, B.singular, bid)
