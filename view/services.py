from models import Card
from typing import Dict


def add_card(card_number) -> Dict:
    obj = Card()
    return obj.insert('value', [card_number])

def get_card_by_number(card_number):
    obj = Card()
    data = {
        'value': str(card_number)
    }
    print(data)
    value = obj.fetchall(data)

    if value:
        if isinstance(value, list):
            return value[0]
        else:
            return value
