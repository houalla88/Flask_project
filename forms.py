from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


#Registration Form

class RegistrationForm(FlaskForm): 
    username = StringField('Username', validators=[
                                    DataRequired(), 
                                    Length(min=5,max=20)
                                    ])
    
    email = StringField('Email', validators=[
                                    DataRequired(), 
                                    Email()
                                    ])

    password = StringField('Password', validators=[
                                    DataRequired(),
                                    Length(min=8),
                                    Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]', 
                                           message="Password must contain an uppercase letter, a lowercase letter, a number, and a special character")
                                    ])
    
    confirm_password = StringField('Confirm Password', validators=[
                                    DataRequired(), 
                                    EqualTo('password', message='Passwords must match')
                                    ])
    
    submit=SubmitField('Sign Up')
    

#Login Form

class LoginForm(FlaskForm): 
    
    email = StringField('Email', validators=[
                                    DataRequired(), 
                                    Email()
                                    ])

    password = StringField('Password', validators=[
                                    DataRequired()
                                    ])
    
    remember = BooleanField('Remember Me')
    
    submit=SubmitField('Login')
    