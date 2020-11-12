from wtforms import SubmitField, BooleanField, StringField, PasswordField, SelectField, validators
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Email
from flask_recaptcha import ReCaptcha
from wtforms.fields.html5 import EmailField

class AddProduct(FlaskForm):
  picture = 
  product = StringField('First Name', 
             [validators.DataRequired()])
  brand = StringField('Last Name', 
             [validators.DataRequired()])
  category = EmailField('Email Address', [validators.DataRequired(), 
             validators.DataRequired(), validators.Email(),validators.Length(min=14, max=50)])
  sol = PasswordField('New Password', [
             validators.DataRequired(),
             validators.Length(min=8, max=100)                   
        ])
  confirm = PasswordField('Repeat Password', [DataRequired(),validators.EqualTo('password', 
             message='Passwords must match'),])
  recaptcha = RecaptchaField()
  submit = SubmitField('REGISTER')