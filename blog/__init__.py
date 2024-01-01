from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = "8970762fb1ac44061fd47e0182701a15"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db.init_app(app)
bcrypt = Bcrypt(app)

from blog import routes
