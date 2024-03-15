import pytest
from app import APP
from credentials import Credentials
import json 
import requests


@pytest.fixture
def client():
    app = APP().__app__
    app.testing = True
    with app.test_client() as client:
        yield client

def addres():
    cred = Credentials()
    host = cred.__APP__['host']
    port = cred.__APP__['port']
    return host, port

def test_get_card_valid_token(client):

    h, p = addres()
    resp = client.get(
        f'http://{h}:{p}/api/get_card',
        json={
            'card_numeber': '00000000'
        },
        headers={
            'Authorization': f'Bearer {auth()}',
            'Content-Type': 'application/json'}
    )

    assert resp.status_code == 200

def test_get_card_invalid_valid_token(client):
    h, p = addres()
    response = client.get(
        f'http://{h}:{p}/api/get_card', 
        json={
            'card_number': '1234567890'
        }
    )
    assert response.status_code == 401


def auth():
    h, p = addres()
    data = json.dumps(Credentials().__AUTH_TEST__)
    headers = {
    'Content-Type': 'application/json'
    }

    token = requests.post(
        url=f'http://{h}:{p}/api/auth',
        headers=headers,
        data=data
    )

    return token.json().get('msg')['token']
    