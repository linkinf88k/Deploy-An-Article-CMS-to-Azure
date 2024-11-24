"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger

# Set the logging level
app.logger.setLevel(logging.DEBUG)

# Create a file handler to log messages to a file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)  # Log messages of level INFO and above

# Create a console handler to log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # Log messages of level ERROR and above

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the app's logger
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
