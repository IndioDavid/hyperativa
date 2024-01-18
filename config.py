from credetions import Credetions

SQLALCHEMY_DATABASE_URI = Credetions().__DB__
SQLALCHEMY_TRACK_MODIFICATIONS = False