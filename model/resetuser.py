from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Email
from flask_recaptcha import ReCaptcha
from wtforms.fields.html5 import EmailField

class ForgotPass(FlaskForm):
  email = EmailField('Email Address', [
             validators.DataRequired(), 
             validators.Email(),
             validators.Length(min=14, max=50)])
  recaptcha = RecaptchaField()
  submit = SubmitField('GET CODE')

class ResetPass(FlaskForm):
  code =  StringField('Code Confirm', [
             validators.DataRequired()               
        ])
  password = PasswordField('New Password', [
             validators.DataRequired(),
             validators.Length(min=8, max=100)                   
        ])
  confirm = PasswordField('Repeat Password', [
             DataRequired(),validators.EqualTo('password', 
             message='Passwords must match'),])
  submit = SubmitField('CONFIRM')