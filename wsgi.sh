#!/bin/bash
. .venv/bin/activate
gunicorn wsgi:app --bind=0.0.0.0:8000 --worker-class gevent --access-logfile logs/gunicorn.log