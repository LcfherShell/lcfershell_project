from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Email
from flask_recaptcha import ReCaptcha
from wtforms.fields.html5 import EmailField
class RegForm(FlaskForm):
  name_first = StringField('First Name', 
             [validators.DataRequired()])
  name_last = StringField('Last Name', 
             [validators.DataRequired()])
  email = EmailField('Email Address', [validators.DataRequired(), 
             validators.DataRequired(), validators.Email(),validators.Length(min=14, max=50)])
  password = PasswordField('New Password', [
             validators.DataRequired(),
             validators.Length(min=8, max=100)                   
        ])
  confirm = PasswordField('Repeat Password', [DataRequired(),validators.EqualTo('password', 
             message='Passwords must match'),])
  recaptcha = RecaptchaField()
  submit = SubmitField('REGISTER')