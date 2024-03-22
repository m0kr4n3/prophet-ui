"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask.cli import with_appcontext
from commons.apispec import APISpecExt
from dotenv import load_dotenv
import os
from sqlalchemy_utils import database_exists, create_database

load_dotenv()
db_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
if not database_exists(db_uri): create_database(db_uri)
db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
apispec = APISpecExt()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")



@with_appcontext
def init():
    """Create a new admin user"""
    from app.extensions import db
    from app.models import User

    user = User(username=os.getenv('ADMIN_USERNAME'), email=os.getenv('ADMIN_EMAIL'), password=os.getenv('ADMIN_PASSWORD'), active=True)
    print(user)
    db.session.add(user)
    db.session.commit()
