from flask import jsonify, request
from app import __blt__
from view.services import add_card, get_card_by_number

@__blt__.route('/api/add_card', methods=['POST'])
def add_card_route():

    resp = add_card(request.get_json().get('card_number'))

    return jsonify(resp ), resp.get('status_code')

@__blt__.route('/api/get_card/', methods=['GET'])
def get_card_route():

    card_number = request.get_json().get('card_number')

    resp = get_card_by_number(request.get_json().get('card_number'))
    if resp:
        return jsonify(resp), 200
    else:
        return jsonify({'message': f'Card {card_number} not found'}), 404
