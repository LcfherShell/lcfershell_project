from wtforms import SubmitField, BooleanField, StringField, PasswordField, SelectField, validators
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Email
from flask_recaptcha import ReCaptcha
from wtforms.fields.html5 import EmailField


class SearchEngine(FlaskForm):
  search = StringField('search', 
             [validators.DataRequired()])
  

class CategorySearch(FlaskForm):
  category = SelectField(u'Category', choices=[('clothing', 'clothing'), ('vehicles', 'vehicles'),
                                              ('drinks and food', 'drinks and food'), ('daily needs', 'daily needs'),
                                              ('fashion', 'fashion'), ('electronic', 'electronic'), 
                                              ('snack', 'snack'), ('services', 'services'),
                                              ('tools', 'tools'), ('herbs and spices', 'herbs and spices'),
                                              ('healthy', 'healthy'), ('kitchen', 'kitchen'),
                                              ('others', 'others')
                                              ])
  submit = SubmitField('GO')

class BrandsSearch(FlaskForm):
  brand  = SelectField(u'Category', choices=[])