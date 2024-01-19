from flask import jsonify, request
from flask_jwt_extended import jwt_required, decode_token
from view import __blt__
from view.services import add_card, get_card_by_number, auth_api, valid
from os import getcwd, remove
from libs.common import check_file
from os.path import join
from werkzeug.utils import secure_filename

# Obtém o diretório de trabalho atual
DIR = getcwd()

# Extensões de arquivo permitidas para upload
ALLOWED_EXTENSIONS = {'txt'}

@__blt__.route('/api/add_card', methods=['POST'])
@jwt_required()
def add_card_route():
    # Decodifica o token de autorização
    decoded_token = decode_token(
        request.headers.get('Authorization').split(' ')[1]
    )
    sub = decoded_token.get('sub')

    # Verifica a validade do token
    if valid(token=sub):
        # Se o conteúdo é JSON, adiciona o cartão usando os dados JSON
        if request.is_json:
            resp = add_card(request.get_json().get('card_number'))
            return jsonify(resp), resp.get('status_code')

        # Se há um arquivo no request.files, salva e processa os dados do arquivo
        elif 'file' in request.files:
            file = request.files['file']

            if file and check_file(file.filename, ALLOWED_EXTENSIONS):

                filename = secure_filename(file.filename)
                file_path = join(DIR, 'files', filename)
                file.save(file_path)

                # Abre o arquivo, lê as linhas e remove o arquivo
                with open(file_path, 'r+') as line:
                    values = [x.replace('\n', '') for x in line.readlines()]
                    line.close()

                # Ao final da leitura do arquivo ele é excluido
    
                remove(file_path)
                resp = add_card(values)
                return jsonify(resp), resp.get('status_code')
    else:
        return jsonify({
            'status_code': 401, 
            'state': 'ERROR', 
            'msg': 'token invalid'
            }
        ), 401

@__blt__.route('/api/get_card', methods=['GET'])
@jwt_required()
def get_card_route():
    # Decodifica o token de autorização
    decoded_token = decode_token(
        request.headers.get('Authorization').split(' ')[1])
    
    sub = decoded_token.get('sub')

    # Verifica a validade do token
    if valid(token=sub):
        # Obtém o cartão pelo número fornecido
        resp = get_card_by_number(request.get_json().get('card_number'))
        return jsonify(resp), resp.get('status_code')
    else:
        return jsonify({
            'status_code': 401, 
            'state': 'ERROR', 
            'msg': 'token invalid'
            }
        ), 401

@__blt__.route('/api/auth', methods=['POST'])
def auth():
    # Autentica o usuário

    data = request.get_json()

    resp = auth_api(
        username=data.get('username'),
        password=data.get('password')
    )

    return jsonify(resp), resp.get('status_code')
