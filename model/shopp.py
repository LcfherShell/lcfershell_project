from flask import Flask, redirect, url_for, render_template, session, request, jsonify, json, flash
from wtforms import SubmitField, BooleanField, StringField, PasswordField, SelectField, FileField, IntegerField, Form, TextField, TextAreaField, validators
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Email
from flask_recaptcha import ReCaptcha
from wtforms.fields.html5 import EmailField, SearchField, URLField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import MultipleFileField
from wtforms.validators import url
from flask_uploads import UploadSet, IMAGES

app = Flask(__name__)

class BuyProducts(FlaskForm):
  amount = IntegerField('Amount', [validators.NumberRange(min=0)])
  paymen = IntegerField('Payment', [validators.NumberRange(min=12)])
  submit = SubmitField('Buy Product')
