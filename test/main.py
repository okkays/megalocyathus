from api import services
from api.helper import Api

mega = Api('http://127.0.0.1:5000/__')
api = mega.api

# Clear the database.
_, s = api.admin.create_database()
assert s == 200, 'Create database'

services = services.run(api)

print("Tests passed!")
