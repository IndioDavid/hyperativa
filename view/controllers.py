from flask import jsonify, request
from flask_jwt_extended import jwt_required
from view import __blt__
from view.services import add_card, get_card_by_number, auth_api


@__blt__.route('/api/add_card', methods=['POST'])
@jwt_required()
def add_card_route():
    resp = add_card(request)
    return jsonify(resp), resp.get('status_code')


@__blt__.route('/api/get_card', methods=['GET'])
@jwt_required()
def get_card_route():
    resp = get_card_by_number(request)
    return jsonify(resp), resp.get('status_code')


@__blt__.route('/api/auth', methods=['POST'])
def auth():
    data = request.get_json()

    resp = auth_api(
        username=data.get('username'),
        password=data.get('password')
    )

    return jsonify(resp), resp.get('status_code')
