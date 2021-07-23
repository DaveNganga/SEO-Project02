from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class InputForm(FlaskForm):
      billing_cycle = StringField('Billing Cycle (in days)', 
                                validators = [DataRequired()]) 
      cost = StringField('Cost of Subscription', 
                       validators = [DataRequired()])
      name_of_subscription = StringField('Name of Subscription', 
                                       validators = [DataRequired()])
      email = StringField('Email', 
                        validators = [DataRequired(), Email()])
      submit = SubmitField('Remind Me!')

      
class RegistrationForm(FlaskForm):
      username = StringField('Username', 
                             validators=[DataRequired(), Length(min=2, max=20)])
      email = StringField('Email',
                         validators=[DataRequired(), Email()])
      password = PasswordField('Password', validators=[DataRequired()])
      confirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired(), EqualTo('password')])
      submit = SubmitField('Sign up')
      
      
class LoginForm(FlaskForm):
      username = StringField('Username', 
                              validators=[DataRequired(), Length(min=2, max=20)])
      password = PasswordField('Password',
                               validators=[DataRequired()])
      submit = SubmitField('Login')