python 3.11

Esta api faz conversões de algumas moedas. converte uma valor em determinada moeda para outra, segue relação a baixo:
    
    - USD
    - BRL
    - EUR
    - BTC
    - ETH


Como instalar e rodar a aplicação:

    1 - Criando o ambiente:
     - $ python -m venv .venv

    2 - Ativando o ambiente no linux:
     - $ source .venv/bin/activate

    3 - Instalando os requisitos:
     - $ pip install -r requierements.txt

    4 - Rodar a aplicação django, (será http://127.0.0.1:8000/)
     - $ python manage.py runserver

    5 - Teste unitario:
     - $ pytest
  
    6 - Cobertura de teste ( 98% ):
     - $ pytest --cov


Funcionalidades:
        
    - "api/v1/hello" -> retorna json { "msg": "Hello world" }, apenas para saber se esta aplicação esta funcionando;
    - "ap1/v1/converter" -> esta rota deve receber os seguir paramentro: from_coin que é uma string, to_coin que é uma string, amount que é um float. 
      E retornara um json com o valor original para o desejado. 
      - Ex.:  /api/v1/converter?from_coin=BTC&to_coin=eth&amount=1.0   
      - e retorna  {"from": { "BTC": 1.0 }, "to": { "ETH": 18.8365865 } }
    - "/api/v1/docs" -> nesta rota você vai poder ver todas as rotas e fazer as chamadas dos rotas


Para rodar a aplicação, no docker-compose.yml para subir um container, no terminal.

      $ docker-compose build
      $ docker-compose up


Decisões tecnicas:
- A api busca dados em tempo real, por esse motivo não foi necessário de um banco de dados;
- A escolha do django foi por estar no tema principal do teste, já o django-ninja para a construção da api foi 
   pela praticidade que é oferecida por essa tecnologia.
- Estruturei o projeto com a ideia de não deixar totalmente aclopada ao django, sendo possivel substituir 
  por outros frameworks como flask e fastApi (o que era a ideia inicial);
- A cobertura de deste foi básica, testando as funcionalidades principais e ao longo do desenvolvimento foi necessário 
  algumas alterações tanto no teste quanto no comportamento da aplicação;
- Foi incluido algumas tecnologias de padronização de codigo e um pré-commit para garantir a qualidade da aplicação,
  passando pelo black para formata o código, flake8 para checa o estilo e qualidade, validação dos requirements e por 
  fim validação dos testes;
- Ficou faltando tirar do código as variaveis de links externo e configurações, para passar para um
  arquivo .env ou um .tmol