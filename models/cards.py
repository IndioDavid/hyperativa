from .querys import Querys

class Card(Querys):
    id = int
    value = str
    __table__ = 'cards'