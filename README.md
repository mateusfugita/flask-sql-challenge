# Flask SQL Challenge

## Tecnologias
- Flask
- SQLAlchemy
- Flask-SQLAlchemy

## Como usar
1. Instale as dependências do projeto
```
$ pip install -r requirements.txt
```

2. Crie um arquivo .env
```
$ cp .env.example .env
```

3. Coloque a string de conexão do banco de dados que será usado (caso opte por utilizar o SQLite, coloque **sqlite:///database/shipay.db**)
4. Crie as tabelas do banco de dados
```
$ python database/migration.py
```

5. Execute a aplicação
```
$ python app.py
```

6. A aplicação estará sendo executada em **http://localhost:5000**

## Rodando em ambiente Docker
1. Execute os seguintes comandos no terminal
```
$ docker build -t <CONTAINER_NAME>:latest .
$ docker run -p 5000:5000 <CONTAINER_NAME>:latest
```

2. A aplicação estará sendo executada em **http://localhost:5000**
