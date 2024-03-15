from credentials import Credetions

SQLALCHEMY_DATABASE_URI = Credetions().__DB__
SQLALCHEMY_TRACK_MODIFICATIONS = False