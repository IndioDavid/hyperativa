from flask import Flask
from flask_jwt_extended import JWTManager
from credentials import Credentials
from view import __blt__

__CRED_OBJ__ = Credentials()

class APP():
    def __init__(self):
        self.__app__ = Flask(__name__)
        self.__app__.config['JWT_SECRET_KEY'] = __CRED_OBJ__.__SECRET__
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