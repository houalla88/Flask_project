# Lesson1
import pandas as pd
import numpy as np
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

