from flask_wtf import FlaskForm
from wtforms import StringField, passwordField, submitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
   username = StringField('Username', 
                          validators=[DataRequired(), Length(min=2, max=20)])
   password = PasswordField('Password', validators=[DataRequired()])
   
   submit = SubmitField('Login')