
Instruções de Instalação:

Antes de executar o aplicativo, certifique-se de ter instalado a biblioteca de desenvolvimento do PostgreSQL usando o seguinte comando no terminal:

bash
Copy code
sudo apt-get install libpq-dev
Após a instalação das dependências, execute o seguinte comando para instalar os requisitos do projeto:

bash
Copy code
pip install -r requirements.txt
Configuração:

Edite o arquivo config.json para configurar o segredo do JWT, os detalhes do banco de dados PostgreSQL e as informações de IP e porta em que a API será executada.
Execução do Aplicativo:

Execute o aplicativo usando o seguinte comando no terminal:

bash
Copy code
python app.py
Endpoints:

api/auth (Método: POST):

Payload: {"username": "user", "password": "senha"}
Resposta de Sucesso:
json
Copy code
{
    "msg": {
        "token": "token"
    },
    "state": "SUCCESS",
    "status_code": 200
}
Método: POST
api/add_card (Método: POST):

Header: { "Authorization": "Bearer token", "Content-Type': 'application/json" }
Payload:
Para um único cartão: {"card_number": "Numero do cartão"}
Para vários cartões: {"card_number": ["Numero do cartão1", "Numero do cartão2", "Numero do cartão3"]}
Resposta de Sucesso:
json
Copy code
{
    "msg": "insert with success",
    "state": "SUCCESS",
    "status_code": 200
}
Resposta de Duplicidade:
json
Copy code
{
    "msg": "duplicate key value violates unique constraint \"idx_value\"\nDETAIL:  Key (value)=(1234522) already exists.\n",
    "state": "ERROR",
    "status_code": 409
}
Método: POST
api/get_card (Método: GET):

Header: { "Authorization": "Bearer token", "Content-Type': 'application/json" }
Payload: {"card_number": "Numero do cartão"}
Método: GET
Observações:

Em caso de sucesso ou duplicidade, será retornada uma mensagem informativa.
Em outros casos, será retornado um erro 500 com uma descrição.
Envio de Dados por Arquivo TXT:

Utilize o comando CURL para enviar dados de um arquivo TXT:

bash
Copy code
curl --location --request POST 'http://IP:PORTA/api/add_card' \
     --header 'Authorization: Bearer token' \
     --data-raw @card.txt
Estrutura do Arquivo TXT:

Copy code
63126356316584354
46465465412316988
22132868313543653
68126353213122143
Certifique-se de que o método seja POST.

Para consultar um cartão já cadastrado, utilize o endpoint api/get_card com o método GET, fornecendo o número do cartão no payload e incluindo o token de autorização no header.

Este README fornece instruções claras para a instalação, configuração e utilização da sua aplicação, facilitando a compreensão por parte dos usuários.

        
