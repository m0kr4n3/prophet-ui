from flask import Flask
import api
import auth
from extensions import apispec
from extensions import db
from extensions import jwt
from flask_cors import CORS
from config import DEBUG




def create_app(testing=False):

    """Application factory, used to create application"""
    app = Flask("app")
    app.config.from_object("config")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    configure_extensions(app)
    configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """Configure flask extensions"""
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    jwt.init_app(app)
    


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """Register all blueprints for application"""
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=DEBUG)