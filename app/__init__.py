# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://your_username:your_password@your_host:your_port/your_database'
#
# mongo = PyMongo(app)
print("here")
# Import the routes blueprint
from app.routes import main_bp


# Register the blueprint with the app
app.register_blueprint(main_bp)
print("register?")


