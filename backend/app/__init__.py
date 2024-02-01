from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from retry import retry  # Make sure to import the retry decorator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysecretpassword@db:3306/customers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the SQLAlchemy database object
db = SQLAlchemy(app)

# Retry decorator with a simple exponential backoff strategy
@retry(OperationalError, delay=1, backoff=2, max_delay=16)
def create_app():
    # Your existing code to create the Flask app and database connection
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysecretpassword@db:3306/customers'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Other configurations...

    return app
