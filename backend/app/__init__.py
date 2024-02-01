from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from retry import retry  # Make sure to import the retry decorator
# Define the SQLAlchemy database object globally, without initializing it with an app
db = SQLAlchemy()
# Retry decorator with a simple exponential backoff strategy
@retry(OperationalError, delay=1, backoff=2, max_delay=16)
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysecretpassword@db:3306/machina_labs'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialize db with the app
    db.init_app(app)
    # You can add other configurations or initializations here
    print("Flask app created and database connection established.")
    return app