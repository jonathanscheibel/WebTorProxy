#!/bin/bash
. $(pwd)/.venv/bin/activate
nohup python app/check_licence.py &
gunicorn wsgi:app --bind=0.0.0.0:8000 --worker-class gevent --access-logfile logs/gunicorn.log