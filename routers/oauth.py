import sys
import os
import requests
import json 

GOOGLE   = {
            'name'  : str('google'),
            'key'   : str('48161273198-k268u9r7n5mlhrbdrpj8qss56vqht9qp.apps.googleusercontent.com'),
            'secret': str('65vVDEjHu4si0BMoEKiWIRKs')
           }

FACEBOOK = {
            'name'  : str('facebook'),
            'key'   : str(''),
            'secret': str('')
           }

GITHUB   = {
            'name'  : str('github'),
            'key'   : str('b4441aac9278439c72ed'),
            'secret': str('efee60300dd6c1810f37f3f970c069e7e1f6ea62')
           }


TWITTER  = {
            'name'  : str('twitter'),
            'key'   : str(''),
            'secret': str('')
           }

DROOPAL  = {
            'name'  : str('droopal'),
            'key'   : str(''),
            'secret': str('')
           }


DISCORD  = {
            'name'  : str('discord'),
            'key'   : str(''),
            'secret': str('')
           }

PAYPAL = {
            'name'  : str('paypal'),
            'key'   : str(''),
            'secret': str('')
           }

RECAPTCHA = {
            'key'   : str('6Lfci9QZAAAAAJdzaCsQjOZ6od3Jhr4cNjPxDMUE'), 
            'secret': str('6Lfci9QZAAAAAC8SHmti-WgDfqdvr4LbSl2xYrwb'), 
            'enabled': True
            }


#RECAPTCHA_ENABLED
#from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
#from flask_dance.contrib.github import make_github_blueprint, github

#githubs = make_github_blueprint(client_id='b4441aac9278439c72ed', client_secret='c06f0615464423ce78bd54de9717923ccf5be737')
#app.register_blueprint(githubs, url_prefix='/access')
#@app.route('/login/github')
#def github():
#    if not github.authorized:
#        return redirect(url_for('github.login'))
#    userinfo = github.get('/user')
#    if userinfo.ok:
#        parsejson =  userinfo.json()
#        return 'your name {}'.format(parsejson['login'])
