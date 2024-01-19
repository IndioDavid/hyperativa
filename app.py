from flask import Flask
from flask_jwt_extended import JWTManager
from credetions import Credetions
from view import __blt__

__CRED_OBJ__ = Credetions()

def create_app():
    app = Flask(__name__)
    configure_app(app)
    register_blueprints(app)
    configure_jwt(app)
    return app

def configure_app(app):
    app.config['JWT_SECRET_KEY'] = __CRED_OBJ__.__SECRET__

def register_blueprints(app):
    app.register_blueprint(__blt__)

def configure_jwt(app):
    jwt = JWTManager(app)

if __name__ == "__main__":
    app = create_app()
    app_config = __CRED_OBJ__.__APP__
    app.run(
        host=app_config['host'],
        port=app_config['port'],
        debug=True
    )