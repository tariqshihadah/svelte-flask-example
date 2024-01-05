from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


#
# INITIALIZE DATABASE CLASS
#

# Define base class
class Base(DeclarativeBase):
  pass

# Initialize
db = SQLAlchemy(model_class=Base)