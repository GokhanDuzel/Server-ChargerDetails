from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

######################################################################
# RETURN HEALTH OF THE APP
######################################################################
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200