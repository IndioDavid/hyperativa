from .querys import Querys

class User(Querys):
    id = int
    username = str
    token = str
    __table__ = '"user"'
