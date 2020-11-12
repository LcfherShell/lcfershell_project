import os
import sys
import re
from flask import Flask, redirect, url_for, render_template, session, request, jsonify, json, flash, abort
from flask_oauthlib.client import OAuth
import speedtest
#from flask_bootstrap import Bootstrap
from datetime import datetime
from random import randint
import requests
from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer, SignatureExpired, BadTimeSignature, BadSignature#import URLSafeSerializer
from datetime import timedelta
from flask_security import Security, current_user, auth_required, hash_password, SQLAlchemySessionUserDatastore
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message 
from flask_avatars import Avatars
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from model.register import *
from model.login import *
from model.userupdate import *
from model.resetuser import *
from model.search import *
from model.shopp import *
from helper.tirtiparty.config import *



if XSS == 'BLOCK':
    from library.MasterSecurity import *
    from library.HashMaster import *
    from library.MasterValidations import clean, mclean, nclean, spaclean
    from helper.Converst import ConvertMany, Digits
    from library.ImagesSec import *

else:
    print(' * Please Set String in folder helper/thirtiparty/config.py to Enabled')

if DEVELOPER_MODE == False or DB == 'DISCONNECT' or OAUTH == False:
    print(' * Please Set String in folder helper/thirtiparty/config.py to Enabled')

else:
    from model.covid import global_confirm, global_totalConfirm, global_newDeaths, global_totalDeaths, global_newRecovered, global_totalRecovered, wcovid,countries
    from helper.Weather import weather, ip4, loc, country_code, coordinate, temperatur, description, pressure, humidity, clouds
    from helper.SpeedConnect import checkconnect, download, upload, ping, client, country
    from flask_recaptcha import ReCaptcha
    from flask_wtf import FlaskForm, RecaptchaField
    from routers.database import *
    from routers.oauth import *

    print(' * Developer Mode: ON')