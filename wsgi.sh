#!/bin/bash
. $(pwd)/.venv/bin/activate
nohup python app/token/steps/all_steps.py &
gunicorn wsgi:app --bind=0.0.0.0:8000 --worker-class gevent --access-logfile logs/gunicorn.log