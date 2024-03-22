import os

ENV = os.getenv("FLASK_DEBUG")
DEBUG = ENV == "development"

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
if not SQLALCHEMY_DATABASE_URI:
    raise ValueError("SQLALCHEMY_DATABASE_URI is not set")

SQLALCHEMY_TRACK_MODIFICATIONS = False