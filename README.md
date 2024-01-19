
# Setup e Uso

1. Rode no terminal sudo apt-get install libpq-dev.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure no arquivo json `confi.json` o secret do JWT, os dados do DB (postgresql), e o IP e a porta em que a API ira rodar.
4. Execute o aplicativo com `python app.py`.
5. Endpoints: 
    `api/auth` envia do payload = {"username": "user", "password": "senha"}
        esse endpoint ira envia o token da aplicação ex: {
            "msg": {
                "token": "token"
            },
            "state": "SUCCESS",
            "status_code": 200
        }
        methodo = POST
    `api/add_card` cadastro do cartão sera feito nesse endpoint, enviar no header {
            "Authorization": "Bearer token",
            "Content-Type': 'application/json"
            }
            e o palyload
            {
            "card_number": "Numero do cartão"
            }
            ou varios de uma vez
            {
            "card_number": ["Numero do cartão1", "Numero do cartão2", ""Numero do cartão3"]
            }

        caso o cadastro seja feito com sucesso receberar uma resposta : {
            "msg": "insert with success",
            "state": "SUCCESS",
            "status_code": 200
        }
        encaso de cartão ja cadastrado : {
            "msg": "duplicate key value violates unique constraint \"idx_value\"\nDETAIL:  Key (value)=(1234522) already exists.\n",
            "state": "ERROR",
            "status_code": 409
        }
        em outros casos retornar erro 500 com uma descretiva
        pode ser enviado por um arquivo txt

        curl --location --request POST 'http://IP:PORTA/api/add_card' \
            --header 'Authorization: Bearer token' \
            --data-raw card.txt

        estrutura do TXT

        63126356316584354
        46465465412316988
        22132868313543653
        68126353213122143

        Methodo=POST
    `api/get_card` consulta no banco se o numero do cartão ja esta cadastrado
        header {
            "Authorization": "Bearer token",
            "Content-Type': 'application/json"
            }
        palyload {"card_number": "Numero do cartão"}
        Methodo = GET

    

        