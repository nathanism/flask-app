# Import Flask object
from flask import Flask

# Create instance of Flask
app = Flask(__name__)

# Get configuration from ../config.py
app.config.from_object('config')

# Instantiate SQLAlchemy object as db.
# Uncomment to use
# db = SQLAlchemy(app)

# Import views.py for routing
from app import views
