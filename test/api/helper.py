import requests

class Api(object):
  def __init__(self, route, verbose=True):
    self.route = route
    self.verbose = verbose

  def process(self, response):
    if self.verbose:
      print('{} {} {} {}'.format(response.status_code,
                                 response.request.method,
                                 self.route,
                                 response.text))
    try:
      return response.json(), response.status_code
    except:
      return response.text, response.status_code

  def get(self, **kwargs):
    return self.process(requests.get(self.route, params=kwargs))

  def post(self, **kwargs):
    return self.process(requests.post(self.route, json=kwargs))

  def put(self, **kwargs):
    return self.process(requests.put(self.route, json=kwargs))

  def delete(self, **kwargs):
    return self.process(requests.delete(self.route, json=kwargs))

  def patch(self, **kwargs):
    return self.process(requests.patch(self.route, json=kwargs))

  def __call__(self, **kwargs):
    return self.get(**kwargs)

  def __getattr__(self, name):
    return Api(self.route + '/' + name, verbose=self.verbose)

  def __getitem__(self, name):
    return Api(self.route + '/' + str(name), verbose=self.verbose)
