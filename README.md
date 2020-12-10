# desafio-celero

Tecnologias
------
* `SQLite` como banco de dados;
* `Django REST framework` para criar as respostas e solicitações da API;


### Índice
1. [Instalação](#install)
2. [Como Rodar](#api)
3. [Como Usar](#use)

### Instalação <a name="install"></a>
Supondo que o python já está instalado na máquina, execute os seguintes comandos:
``` 
# Na pasta desafio-celero
$ python -m venv venv

# SO linux
$ source venv/bin/activate

# SO windows
$ venv\Scripts\activate

# Instala as dependencias
$ pip install -r requirements.txt

# Executa as alteracoes no banco de dados
$ python manage.py migrate

# Popula o banco de dados
$ python manage.py shell
$ exec(open('seed.py').read())
``` 

### Como rodar <a name="api"></a>
Para iniciar a API execute o comando:
``` 
python manage.py runserver
``` 

### Como usar <a name="use"></a>
Endereço padrão: localhost:8000/
```json
POST /games/ {"season":"Winter", "year":1998}
```
<span style="color:green">`201 {"id":106,"season":"Winter","year":1998}`</span>

```json
GET /games/{id}
```


Filtrando por url
```json
GET /games?year=1996
```
