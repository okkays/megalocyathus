#!/bin/bash
export FLASK_DEBUG=1
export FLASK_APP=app/main.py
export HOST=0.0.0.0
export PORT=5000
export DATABASE='postgres://mega_admin:superduperpassword@localhost:5432/mega'

psql -U postgres < ./setup.sql

python -m flask run --host=$HOST --port=$PORT
