from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# initialize config variables for application
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# bootstrap instance
bootstrap = Bootstrap(app)

# models is for the structure of the database 
from app import routes, models
