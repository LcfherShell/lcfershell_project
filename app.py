from flask import Flask, redirect, url_for, render_template, session, request, jsonify, json, flash, abort, send_file, make_response
from datetime import datetime
from random import randint
import os, sys, re, logging
from datetime import timedelta

#log = logging.getLogger('werkzeug')
#log.disabled = True

app = Flask(__name__)

app.config.update(dict( 
     SECRET_KEY = os.urandom(58),
    SECURITY_PASSWORD_SALT = os.urandom(128),
    PERMANENT_SESSION_LIFETIME = timedelta(days=2)
    ))

@app.route('/', methods=['GET', 'POST'])
@app.route('/<data>', methods=['GET', 'POST'])
def index(data=None):
    response = make_response(render_template('index.jinja', sessions=None))
    response.status_code = 200

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    #response.set_cookie('userID', sessions)
    return response