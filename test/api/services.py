def run(mega):
  # Make a service.
  sid, s = mega.services.post(name='test', url=':8080')
  assert s == 200, 'Service added'

  # Get a service
  r, s = mega.services[sid].get()
  assert r['name'] == 'test'
  assert r['url'] == ':8080'
  assert s == 200, 'Got a service'

  # Modify a service.
  r, s = mega.services[sid].patch(name='trest')
  assert s == 200, 'Update a service'
  r, s = mega.services[sid].get()
  assert r['name'] == 'trest', 'Service updates name'

  # Service name validation.
  sid, s = mega.services.post(name='__', url=':8080')
  assert s == 400, 'Service name validation'
  sid, s = mega.services.post(name='abc/def/', url=':8080')
  assert s == 400, 'Service name validation'
  sid, s = mega.services.post(name='bad name', url=':8080')
  assert s == 400, 'Service name validation'

  # Fail to make a service.
  r, s = mega.services.post(waffles='Waffles of service')
  assert s == 400, 'Failed to make service'

  # Get services
  r, s = mega.services.get()
  assert len(r) == 1, 'Should be one service'
  assert r[0]['name'] == 'trest'
  assert r[0]['url'] == ':8080'
  assert s == 200, 'Got services'
  services = r

  return services
