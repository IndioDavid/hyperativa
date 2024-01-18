from flask import Flask
from credetions import Credetions
from view import __blt__


app = Flask(__name__)
app.register_blueprint(__blt__)

if __name__ == "__main__":
    app_config = Credetions().__APP__
    app.run(
        host=app_config['host'], 
        port=app_config['port'], 
        debug=True
    )