#!/usr/bin/env bash

source venv/bin.activate
../venv/bin/flask db upgrade

exec gunicorn -b:5000 --access-logfile - --error-logfile - projectblog:app
