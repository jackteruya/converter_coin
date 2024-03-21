python 3.11

- Esta api faz conversões de algumas moedas. converte uma valor em determinada moeda para outra, segue relação a baixo:
    
    - USD
    - BRL
    - EUR
    - BTC
    - ETH


- Como instalar e rodar a aplicação:

    1 - Criando o ambiente:
     - $ python -m venv .venv

    2 - Ativando o ambiente no linux:
     - $ source .venv/bin/activate

    3 - Instalando os requisitos:
     - $ pip install -r requierements.txt

    4 - Rodar a aplicação django, (será http://127.0.0.1:8000/)
     - $ python manage.py runserver

    5-Teste unitario:
     - $ pytest


- Funcionalidades:
        
    - "api/v1/hello" -> retorna json { "msg": "Hello world" }, apenas para saber se esta aplicação esta funcionando;
    - "ap1/v1/converter" -> esta rota deve receber os seguir paramentro: from_coin que é uma string, to_coin que é uma string, amount que é um float. 
      E retornara um json com o valor original para o desejado. 
      - Ex.:  /api/v1/converter?from_coin=BTC&to_coin=eth&amount=1.0   
      - e retorna  {"from": { "BTC": 1.0 }, "to": { "ETH": 18.8365865 } }
    - "/api/v1/docs" -> nesta rota você vai poder ver todas as rotas e fazer as chamadas dos rotas


- Para rodar a aplicação, no docker-compose.yml para subir um container, no terminal.

      $ docker-compose build
      $ docker-compose up