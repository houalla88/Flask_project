# Lesson1
import pandas as pd
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

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
def habout():
    return render_template('about.html',title= 'about')

if __name__ == "__main__":
    app.debug = True
    app.run()