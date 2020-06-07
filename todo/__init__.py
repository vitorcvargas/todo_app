from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder = 'templates')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'

db = SQLAlchemy(app)

from todo import routes
