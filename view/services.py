from models import Card, User
from flask import Request
from os import getcwd, remove, path
from typing import Dict
from flask_jwt_extended import create_access_token
from libs.cryp import encode_user_passwd, encode_generic
from datetime import timedelta
from werkzeug.utils import secure_filename
from libs.common import check_file

ALLOWED_EXTENSIONS = {'txt'}
DIR = getcwd()

def add_card(request: Request) -> Dict:
    card_number = None
    values = []

    if request.is_json:
        card_number = request.get_json().get('card_number')
        
    elif 'file' in request.files:
        file = request.files['file']

        if file and check_file(file.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(file.filename)
            file_path = path.join(DIR, 'files', filename)
            file.save(file_path)

            with open(file_path, 'r') as line:
                card_number = [x.strip() for x in line.readlines()]

            remove(file_path)
    
    if isinstance(card_number, list):
        values.append((encode_generic(x) for x in card_number))
    elif isinstance(card_number, str):
        values.append((encode_generic(card_number)))
    
    values = tuple(values)

    return Card().insert('value', values)


def get_card_by_number(request: Request):
    card_number = None
    try:
        card_number = request.get_json().get('card_number')

        data = {
            'value': encode_generic(str(card_number))
        }
        
        value = Card().fetchall(data)

        if value:
            if isinstance(value, list):
                return value[0]
            else:
                return value
    except Exception as e:
        return {
                'status_code': 400, 
                'state': 'ERROR', 
                'msg': e
            }

def auth_api(username, password):
    try:

        user_data = {
            'token': encode_user_passwd(
                username,
                password
                )
            }

        resp = User().fetchall(values=user_data)
        if isinstance(resp, list):
            resp = resp[0]

            token = create_access_token(
                identity=user_data['token'], 
                expires_delta=timedelta(hours=1)
            )
            return {
                'status_code': 200, 
                'state': 'SUCCESS', 
                'msg': {'token': token}
            }
        else:
            return {
                'status_code': 401, 
                'state': 'ERROR', 
                'msg': 'Invalid username or password'
            }

    except Exception as e:
        return {
            'status_code': 500, 
            'state': 'ERROR', 
            'msg': str(e)
        }