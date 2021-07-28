import time
import os
import requests
from flask import jsonify
from app.token.validators import validate, not_valid

from app import app


@app.route("/api/enabletor/<token>", methods=['GET', 'POST'])
def enable_tor(token):
    if not validate(token):
        return not_valid()
    os.system('anonsurf stop')
    time.sleep(3)
    return jsonify({"success": False}), 501


@app.route("/api/disabletor/<token>", methods=['GET', 'POST'])
def disable_tor(token):
    if not validate(token):
        return not_valid()
    os.system('anonsurf start')
    time.sleep(3)
    return jsonify({"success": False}), 501


@app.route("/api/change/<token>", methods=['GET', 'POST'])
def changeip(token):
    os.system('anonsurf change')
    # time.sleep(2) # TODO verificar necessidade em teste de stress
    return jsonify({"success": True})


@app.route("/api/myip/<token>", methods=['GET'])
def myip(token):
    time.sleep(3)
    res = requests.get('https://api.my-ip.io/ip.json')
    if res.ok:
        return jsonify(res.json())


@app.route("/api/change_myip/<token>", methods=['GET', 'POST'])
def changeip_myip(token):
    changeip(token)
    return myip(token)
