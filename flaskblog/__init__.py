from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import email_validator


app = Flask(__name__)
app.config['SECRET_KEY'] = '94256c982054236688cce428bcb32f3f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
