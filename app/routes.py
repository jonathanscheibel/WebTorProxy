from flask import jsonify
import time
import os
import requests

from app import app


@app.route("/api/changeip/<token>", methods=['GET'])
def changeip(token):
    os.system('anonsurf changeid')
    # time.sleep(2) # TODO verificar necessidade em teste de stress
    return jsonify({"success": True})


@app.route("/api/myip/<token>", methods=['GET'])
def myip(token):
    time.sleep(3)
    res = requests.get('https://api.my-ip.io/ip.json')
    if res.ok:
        return jsonify(res.json())


@app.route("/api/changeip_myip/<token>", methods=['GET'])
def changeip_myip(token):
    changeip(token)
    return myip(token)
