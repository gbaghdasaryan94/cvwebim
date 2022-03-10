#!/bin/bash
# start.sh

FLASK_APP=wsgi.py
FLASK_DEBUG=1
APP_CONFIG_FILE=config.ini
SQLALCHEMY_DATABASE_URI=sqlite:///survey.db
SQLALCHEMY_TRACK_MODIFICATIONS=False
flask run
