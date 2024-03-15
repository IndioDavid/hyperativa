from flask import Flask
from flask_jwt_extended import JWTManager
from credentials import Credentials
from view import __blt__

__CRED_OBJ__ = Credentials()

class APP():
    def __init__(self):
        self.__app__ = Flask(__name__)
        self.__app__.config['JWT_SECRET_KEY'] = "eyJhbGciOiJIUzI1NiJ9.ew0KICAic3ViIjogIjEyMzQ1Njc4OTAiLA0KICAibmFtZSI6ICJBbmlzaCBOYXRoIiwNCiAgImlhdCI6IDE1MTYyMzkwMjINCn0.OApQugx0HxMcTT-rSc-D_t_p399edsu4Bz8FRTSM0qE"
        self.__app__.config["JWT_ALGORITHM"] = "HS256"
        self.__app__.register_blueprint(
            __blt__,
            name='hy'
        )
        jwt = JWTManager(self.__app__)

if __name__ == "__main__":
    app = APP().__app__
    app_config = __CRED_OBJ__.__APP__
    app.run(
        host=app_config['host'],
        port=app_config['port'],
        debug=True
    )