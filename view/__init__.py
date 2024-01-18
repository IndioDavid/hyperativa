from flask import Blueprint

__blt__ = Blueprint(
    'api',
    __name__
)

from . import controllers
