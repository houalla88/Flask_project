# Lesson1
import pandas as pd
import numpy as np
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dc8b94831bd1b72db187b828b960cca6'

posts = [ 
    {
        'author':'Houbayda Oualla',
        'title':'Data Optimization G',
        'content':'First Data Optimization Post', 
        'date_posted':'December 29, 2023'
    },
    {
        'author':'Houbayda Oualla',
        'title':'Data Optimization L',
        'content':'Second Data Optimization Post', 
        'date_posted':'December 29, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title= 'about')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)

@app.route('/login')
def login():
    form = RegistrationForm()
    return render_template('login.html',title='Login', form=form)

if __name__ == "__main__":
    app.debug = True
    app.run()