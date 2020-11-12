from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired
from flask_recaptcha import ReCaptcha

class LogForm(FlaskForm):
  user = StringField('Username or Email', [validators.DataRequired(), 
        validators.DataRequired(), validators.Length(min=6, max=35)])
  password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=100)                   
        ])
  recaptcha = RecaptchaField()
  submit = SubmitField('LOGIN')


  