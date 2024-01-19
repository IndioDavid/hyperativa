from models import Card, User
from typing import Dict
from flask_jwt_extended import create_access_token
from libs.cryp import encode_user_passwd, encode_generic
from datetime import timedelta

def add_card(card_number) -> Dict:
    obj = Card()
    values = []
    if isinstance(card_number, list):
        for value in card_number:
            values.append((encode_generic(value),))
    if isinstance(card_number, str):
        values.append((encode_generic(card_number),))

    return obj.insert('value', values)


def get_card_by_number(card_number):
    obj = Card()
    data = {
        'value': encode_generic(str(card_number))
    }
    
    value = obj.fetchall(data)

    if value:
        if isinstance(value, list):
            return value[0]
        else:
            return value

def auth_api(username, password):
    try:
        obj = User()

        user_data = {'token': encode_user_passwd(username,password)}

        resp = obj.fetchall(values=user_data)
        if isinstance(resp, list):
            resp = resp[0]

            token = create_access_token(identity=user_data['token'], expires_delta=timedelta(hours=1))
            return {'status_code': 200, 'state': 'SUCCESS', 'msg': {'token': token}}
        else:
            return {'status_code': 401, 'state': 'ERROR', 'msg': 'Invalid username or password'}

    except Exception as e:
        return {'status_code': 500, 'state': 'ERROR', 'msg': str(e)}

def valid(token):

    obj = User()

    user_data = {'token': token}
    resp = obj.fetchall(user_data)
    if isinstance(resp, list):
        resp = resp[0]

    if resp.get('id'):
        return True
    else:
        return False